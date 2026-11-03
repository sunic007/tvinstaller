#!/usr/bin/env python3
"""Refresh docs/catalog.json: newest GitHub release of every app in the list.

The app downloads its app list from this file (GitHub Pages), so new builds of
Jellyfin, Moonlight and others reach users without a new TV Installer release.

For each entry whose package lives in GitHub releases the script looks at the
latest release of the same repository and picks the asset that matches the old
file name with only the numbers changed (version, build). GitHub publishes the
SHA-256 of every asset ("digest"), so nothing has to be downloaded; an asset
without a digest is skipped and the entry keeps its previous, verified build.

It also stamps "downloads": the sum of GitHub download_count of that file over all
releases (the same shape of name), like Apps2Samsung's "Most downloaded". The app
shows the most downloaded apps first in their own section.

Entries are never added or removed here - only refreshed. Everything else
(title, description, category, package id, icon) stays as it was.

Usage: GITHUB_TOKEN=... python .github/scripts/update_catalog.py [docs/catalog.json]
"""
import hashlib
import io
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = "https://api.github.com"
ASSET_URL = re.compile(r"^https://github\.com/([^/]+/[^/]+)/releases/download/([^/]+)/([^/]+)$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
MAX_PACKAGE = 220 * 1024 * 1024  # = MAX_INSTALLABLE_BYTES in the app


def read_config(url, sha):
    """app_id and package_version from config.xml of a .wgt, checked against its SHA-256; None on any doubt."""
    import zipfile
    req = urllib.request.Request(url, headers={"User-Agent": "tvinstaller-catalog"})
    blob = io.BytesIO()
    with urllib.request.urlopen(req, timeout=300) as r:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            blob.write(chunk)
            if blob.tell() > MAX_PACKAGE:
                return None
    data = blob.getvalue()
    if hashlib.sha256(data).hexdigest() != sha:
        return None
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        name = next((n for n in z.namelist() if n.lower() == "config.xml"), None)
        if not name:
            return None
        xml = z.read(name).decode("utf-8", "replace")
    widget = re.search(r"<widget\b[^>]*>", xml)
    app = re.search(r"<tizen:application\b[^>]*>", xml)
    version = re.search(r'\bversion\s*=\s*"([^"]+)"', widget.group(0)) if widget else None
    app_id = re.search(r'\bid\s*=\s*"([^"]+)"', app.group(0)) if app else None
    if not version or not app_id or not re.match(r"^[A-Za-z0-9]{10}\.[A-Za-z0-9_-]+$", app_id.group(1)):
        return None
    return app_id.group(1), version.group(1)


def api(path):
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "tvinstaller-catalog",
        **({"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"]} if os.environ.get("GITHUB_TOKEN") else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def shape(name):
    """File name with every run of digits replaced: 'app_1.2.3.wgt' -> 'app_#.#.#.wgt'."""
    return re.sub(r"\d+", "#", name)


def latest_release(repo, cache):
    if repo not in cache:
        rel = api(f"/repos/{repo}/releases/latest")
        if rel is None:  # only pre-releases - take the newest non-draft one
            rels = api(f"/repos/{repo}/releases?per_page=10") or []
            rel = next((r for r in rels if not r.get("draft")), None)
        cache[repo] = rel
    return cache[repo]


def all_releases(repo, cache):
    """Every release of the repository (up to 500), cached per run."""
    if repo not in cache:
        out = []
        for page in range(1, 6):
            rels = api(f"/repos/{repo}/releases?per_page=100&page={page}") or []
            out += rels
            if len(rels) < 100:
                break
        cache[repo] = out
    return cache[repo]


def downloads(entry, cache):
    """Total downloads of this entry's file over all releases; None when not on GitHub."""
    m = ASSET_URL.match(entry.get("package_url") or "")
    if not m:
        return None
    repo, _, name = m.groups()
    want = shape(name)
    return sum(a.get("download_count") or 0
               for r in all_releases(repo, cache) if not r.get("draft")
               for a in r.get("assets", []) if a.get("name") == name or shape(a.get("name", "")) == want)


def refresh(entry, cache, taken=()):
    m = ASSET_URL.match(entry.get("package_url") or "")
    if not m:
        return "not on GitHub"
    repo, old_tag, old_name = m.groups()
    rel = latest_release(repo, cache)
    if not rel:
        return "no releases"
    tag = rel.get("tag_name") or ""
    if tag == old_tag:
        return "up to date"
    assets = rel.get("assets", [])
    # Same name first; otherwise numbers may change - but never take a file another entry uses
    # (upstream dropped "Jellyfin-10.10.z.wgt", and "10.11.z" has the same shape).
    candidates = [a for a in assets if a["name"] == old_name] or \
        [a for a in assets if shape(a["name"]) == shape(old_name) and (repo, a["name"]) not in taken]
    if len(candidates) != 1:
        return f"{tag}: no single matching file ({len(candidates)})"
    asset = candidates[0]
    sha = (asset.get("digest") or "").removeprefix("sha256:").lower()
    if not SHA256.match(sha):
        return f"{tag}: GitHub gave no SHA-256, kept the old build"
    url = asset["browser_download_url"]
    if not url.startswith("https://"):
        return "not https"
    entry["package_url"] = url
    entry["sha256"] = sha
    entry["size_bytes"] = asset.get("size") or entry.get("size_bytes")
    entry["version"] = tag[1:] if re.match(r"^v\d", tag) else tag
    # Версия внутри нового пакета - из его config.xml; не прочли - старая была бы неправдой, убираем.
    entry.pop("package_version", None)
    if entry.get("platform", "tizen") == "tizen" and url.lower().endswith(".wgt"):
        try:
            found = read_config(url, sha)
        except Exception:
            found = None
        if found:
            entry["app_id"], entry["package_version"] = found
    return f"updated {old_tag} -> {tag}"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "docs/catalog.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    cache, changed, counts, every = {}, 0, 0, {}
    for entry in data["services"]:
        others = [ASSET_URL.match(e.get("package_url") or "") for e in data["services"] if e is not entry]
        taken = {(m.group(1), m.group(3)) for m in others if m}
        try:
            result = refresh(entry, cache, taken)
        except Exception as e:  # one broken repository must not stop the rest
            result = f"error: {e}"
        if result.startswith("updated"):
            changed += 1
        try:
            total = downloads(entry, every)
        except Exception as e:
            total = None
            print(f"{entry['id']}: downloads not read ({e})")
        if total and total != entry.get("downloads"):
            entry["downloads"] = total
            counts += 1
        print(f"{entry['id']}: {result}" + (f", downloads {total}" if total else ""))
    if changed or counts:
        data["generated"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print(f"changed: {changed}, download counts: {counts}")


if __name__ == "__main__":
    main()
