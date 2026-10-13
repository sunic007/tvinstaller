# TV Installer — install apps on Samsung Smart TV from your phone

**English** · [Русский](README.ru.md)

An Android app that installs `.wgt` apps on **Samsung (Tizen)** Smart TVs straight from your phone — no PC, no
Tizen Studio. It finds the TV on your Wi‑Fi, gets the Samsung certificate for it, signs the package and installs it.

**⬇️ [Download TvInstaller.apk](https://github.com/sunic007/tvinstaller/releases/latest/download/TvInstaller.apk)** — latest version
· all versions — [Releases](https://github.com/sunic007/tvinstaller/releases)
· [privacy policy](https://sunic007.github.io/tvinstaller-privacy/)
· ❤️ [sponsor the project](https://github.com/sponsors/sunic007)

> The app interface is currently in Russian. The steps below and the built-in animation show exactly what to press.

<p align="center">
  <img src="docs/screenshots/en/01.png" width="23%">
  <img src="docs/screenshots/en/02.png" width="23%">
  <img src="docs/screenshots/en/03.png" width="23%">
  <img src="docs/screenshots/en/04.png" width="23%">
</p>
<p align="center">
  <img src="docs/screenshots/en/05.png" width="23%">
  <img src="docs/screenshots/en/06.png" width="23%">
  <img src="docs/screenshots/en/07.png" width="23%">
</p>

## Features

- **Finds your TV automatically** on the same Wi‑Fi network.
- **Step-by-step animation** of how to enable Developer Mode on the TV, following Samsung's official guide.
- **Samsung certificate in one tap** — sign in with your Samsung account; no PC or Tizen Studio needed.
- **Catalog of 45+ TV apps** — media centers, players, streaming, IPTV — or install your own `.wgt` file or link.
- **[Lampa for Samsung](https://github.com/sunic007/lampa-samsung)** is installed straight from its latest GitHub
  release and then keeps itself up to date on the TV.
- **Install log** — every step is visible; certificates can be backed up to a file.

## Requirements

- An Android phone and a Samsung Smart TV with Tizen, on the same Wi‑Fi network (not a guest network).
- A free Samsung account (for the installation certificate).

## How to install an app on the TV

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

## FAQ

**The TV is not found.** Make sure the phone and the TV are on the same network and that Developer Mode on the TV has
*this phone's* IP. If the phone's IP changed, enter it again and restart the TV.

**Signing or installation error.** Remove the old version of the app from the TV and install again.

**Is it safe?** The app talks to the TV only inside your home network. It contacts Samsung only to issue the
certificate and GitHub only to download apps — see the [privacy policy](https://sunic007.github.io/tvinstaller-privacy/).

## Support the project

TV Installer is free. If it is useful to you, you can support its development on
**[GitHub Sponsors](https://github.com/sponsors/sunic007)** (in the app: Settings → «Поддержать проект»).
