**English** · [Русский](README.ru.md) · [O'zbekcha](README.uz.md)

# TV Installer — install apps on Samsung Smart TV from your phone

[![Release](https://img.shields.io/github/v/release/sunic007/tvinstaller?label=release&color=3d8bff)](https://github.com/sunic007/tvinstaller/releases/latest) [![Downloads](https://img.shields.io/github/downloads/sunic007/tvinstaller/total?color=2ea043)](https://github.com/sunic007/tvinstaller/releases) ![Android](https://img.shields.io/badge/Android-7.0%2B-3ddc84?logo=android&logoColor=white) ![Tizen TV](https://img.shields.io/badge/Tizen-TV-1428a0) ![Languages](https://img.shields.io/badge/UI-English%20%7C%20Русский%20%7C%20O'zbekcha-8a63d2)

An Android app that installs `.wgt` apps on **Samsung (Tizen)** Smart TVs straight from your phone — no PC, no
Tizen Studio. It finds the TV on your Wi‑Fi, gets the Samsung certificate for it, signs the package and installs it.

**⬇️ [Download TvInstaller.apk](https://github.com/sunic007/tvinstaller/releases/latest/download/TvInstaller.apk)** — latest version
· all versions — [Releases](https://github.com/sunic007/tvinstaller/releases)
· what's new — [CHANGELOG.md](CHANGELOG.md)
· [privacy policy](https://sunic007.github.io/tvinstaller/privacy.html)
· ❤️ [sponsor the project](https://github.com/sponsors/sunic007)

> The app speaks **English, Russian and Uzbek (O'zbekcha)** — it follows your phone language; switch in Settings → Language.

<p align="center">
  <img src="docs/screenshots/en/01.png" width="30%">
  <img src="docs/screenshots/en/02.png" width="30%">
  <img src="docs/screenshots/en/03.png" width="30%">
</p>
<details>
<summary>More screenshots</summary>

<p align="center">
  <img src="docs/screenshots/en/04.png" width="30%">
  <img src="docs/screenshots/en/05.png" width="30%">
  <img src="docs/screenshots/en/06.png" width="30%">
</p>
<p align="center">
  <img src="docs/screenshots/en/07.png" width="30%">
  <img src="docs/screenshots/en/08.png" width="30%">
  <img src="docs/screenshots/en/09.png" width="30%">
</p>
</details>

## Features

- **Finds your TV automatically** on the same Wi‑Fi network; several TVs are supported.
- **"Can't connect?" wizard** checks Wi‑Fi, the TV, Developer Mode and the address set on the TV step by step — and
  tells you clearly when the TV is set up for another device (only one phone or PC can install on a Samsung TV at a time).
- **Video guide** on enabling Developer Mode on the TV, in English, Russian and Uzbek.
- **Samsung certificate just once** — sign in with your Samsung account; no PC or Tizen Studio. A reminder comes a
  month before it expires, renewal is one tap, and certificates can be backed up and **restored from a backup**.
- **Catalog of 40+ TV apps** — media centers, players, streaming, IPTV — with **Recommended** starter picks; or install
  your own `.wgt` file or link. Variants of one app (Jellyfin, Moonlight builds) are explained.
- **One tap to install**, every step visible, then **"Open on TV"**. The **On TV** list has **Open / Remove** and
  **Update all**; a daily notification tells you when updates are out.
- **TV remote** in the phone and **turning the TV on** from the phone (Wake-on-LAN).
- **[Lampa for Samsung](https://github.com/sunic007/lampa-samsung)** is installed straight from its latest GitHub
  release and then keeps itself up to date on the TV.
- **Updates itself without a browser**: downloads its new version, verifies it and opens Android's installer.

## Requirements

- An Android 7.0+ phone and a Samsung Smart TV with Tizen, on the same Wi‑Fi network (not a guest network).
- A free Samsung account (for the installation certificate).

## How to install an app on the TV
<table>
<tr>
<td valign="top" width="260">

<p align="center"><a href="https://youtu.be/L6nK4SBWKP0"><img src="docs/video/thumbnails/thumbnail-en.jpg" width="220" alt="English"></a></p>

</td>
<td valign="top">

1. **Enable Developer Mode on the TV:** open the **Apps** tab → scroll down to **App Settings** → press `1 2 3 4 5`
   on the remote → switch **Developer mode** to **On**, enter your phone's IP address (TV Installer shows it at the
   top of the TV screen) and press **OK**.
2. **Restart the TV:** hold the power button for about 2 seconds, then turn it on again. If your remote is not an
   original Samsung one, unplug the TV for 10 seconds instead. After the restart, **App Settings** shows
   **DEVELOP MODE** at the top.
3. **Install TV Installer** on your phone: download the APK and open it (Android will ask you to allow installs from
   this source).
4. In TV Installer pick your **TV**, sign in to **Samsung** once to get the certificate, then choose an app from the
   catalog or your own `.wgt` file.
5. Updates install over the previous version; the app's settings on the TV are kept.

</td>
</tr>
</table>

<details>
<summary>Other languages</summary>

<p align="center"><a href="https://youtu.be/U4VGa0fGYUI"><img src="docs/video/thumbnails/thumbnail-ru.jpg" width="220" alt="Русский"></a> <a href="https://youtu.be/AB0fsIuFSII"><img src="docs/video/thumbnails/thumbnail-uz.jpg" width="220" alt="O'zbekcha"></a></p>

</details>





## FAQ

**The TV is not found or won't connect.** Open the ⋮ menu → "Can't connect?" — the wizard checks everything step
by step. Also make sure the phone and the TV are on the same network and that Developer Mode on the TV has
*this phone's* IP. If the phone's IP changed, enter it again and restart the TV.

**Signing or installation error.** Remove the old version of the app from the TV and install again.

**Is it safe?** The app talks to the TV only inside your home network. It contacts Samsung only to issue the
certificate and GitHub only to download apps — see the [privacy policy](https://sunic007.github.io/tvinstaller/privacy.html).

## Disclaimer

TV Installer is an independent project and is not affiliated with or endorsed by Samsung. Samsung and Tizen are
trademarks of Samsung Electronics. The app uses the same certificate flow as Samsung's Tizen Studio: you sign in to
your own Samsung account, and the certificate is issued by Samsung for your TV. You are responsible for the apps you
install; the app does not host or provide any media content.

## Support the project

TV Installer is free. If it is useful to you, you can support its development on
**[GitHub Sponsors](https://github.com/sponsors/sunic007)** (in the app: Settings → Support the project).
