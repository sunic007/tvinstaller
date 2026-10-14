#!/usr/bin/env python3
"""Refresh docs/catalog.json: newest GitHub release of every app in the list.

The app downloads its app list from this file (GitHub Pages), so new builds of
Jellyfin, Moonlight and others reach users without a new TV Installer release.

For each entry whose package lives in GitHub releases the script looks at the
latest release of the same repository and picks the asset that matches the old
file name with only the numbers changed (version, build). GitHub publishes the
SHA-256 of every asset ("digest"), so nothing has to be downloaded; an asset
without a digest is skipped and the entry keeps its previous, verified build.

Entries are never added or removed here - only refreshed. Everything else
(title, description, category, package id, icon) stays as it was.

Usage: GITHUB_TOKEN=... python tools/update_catalog.py [docs/catalog.json]
"""
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


def refresh(entry, cache):
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
    candidates = [a for a in rel.get("assets", []) if shape(a["name"]) == shape(old_name)]
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
    return f"updated {old_tag} -> {tag}"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "docs/catalog.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    cache, changed = {}, 0
    for entry in data["services"]:
        try:
            result = refresh(entry, cache)
        except Exception as e:  # one broken repository must not stop the rest
            result = f"error: {e}"
        if result.startswith("updated"):
            changed += 1
        print(f"{entry['id']}: {result}")
    if changed:
        data["generated"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print(f"changed: {changed}")


if __name__ == "__main__":
    main()
