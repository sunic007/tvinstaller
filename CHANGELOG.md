# Changelog / История изменений

[Download the latest APK / Скачать последнюю версию](https://github.com/sunic007/tvinstaller/releases/latest/download/SunicTvInstaller.apk)

## 2.3.1 — cleaner TV list / список телевизоров без лишнего
- **EN:** setup steps (1–4) and the phone's address are shown only while a TV is being set up; with ready TVs the screen goes straight to the list.
- **RU:** шаги настройки (1–4) и адрес телефона видны только при настройке телевизора; когда ТВ готовы, экран сразу показывает список.

## 2.3.0 — new app ID / новое имя приложения
- **EN:** the app is now `com.sunicapps.tvinstaller` (registered with Android developer verification). Existing installs move over by themselves: TV Installer updates to 2.2.9, installs the new app and hands over Samsung certificates, TVs, saved packages and settings; then you can remove the old one. Each TV asks once more to allow the connection.
- **RU:** приложение теперь `com.sunicapps.tvinstaller` (зарегистрировано в проверке разработчиков Android). Установленные переезжают сами: TV Installer обновится до 2.2.9, поставит новое приложение и передаст ему сертификаты Samsung, телевизоры, сохранённые пакеты и настройки; старое затем можно удалить. Каждый ТВ один раз заново спросит разрешение на подключение.

## 2.2.8 — remote buttons / кнопки пульта
- **EN:** the installer no longer strips `tv.inputdevice`, `tv.audio`, `tv.display`, `tv.channel` — Play/Pause, rewind, Channel ± and colour buttons reach installed apps again (reinstall the app to get them).
- **RU:** установщик больше не удаляет `tv.inputdevice`, `tv.audio`, `tv.display`, `tv.channel` — Play/Pause, перемотка, «Канал ±» и цветные кнопки снова доходят до приложений (переустановите приложение).

## 2.2.6 — big update / большое обновление
- **EN:**
  - **O'zbekcha** — the app now speaks Uzbek too (Settings → Language).
  - **"Can't connect?" wizard** and a clear hint when the TV is set up for another device's address
    (only one phone/PC can install on a Samsung TV at a time).
  - **Certificate reminder** a month before it expires, one-tap renewal, and **restore from backup**.
  - **"Update all"** for apps on the TV, a daily notification about updates, **Recommended** starter apps,
    **Open / Remove** right in the "On TV" list.
  - **TV remote** in the menu, **turn the TV on** from the phone (Wake-on-LAN), installing on **several TVs**.
  - **Self-update without the browser**: the app downloads its new version itself, checks it and opens Android's installer.
  - Security hardening after an audit; many fixes after testing on a real TV.
- **RU:**
  - **O'zbekcha** — приложение теперь и на узбекском (Настройки → Язык).
  - **Мастер «Не подключается?»** и понятная подсказка, когда ТВ настроен на адрес другого устройства
    (ставить приложения на Samsung может только один телефон или компьютер за раз).
  - **Напоминание о сертификате** за месяц до окончания, продление в одно нажатие, **восстановление из резервной копии**.
  - **«Обновить всё»** для приложений на ТВ, уведомление об обновлениях раз в день, подборка **«Рекомендуем»**,
    **«Открыть / Удалить»** прямо в списке «На ТВ».
  - **Пульт** в меню, **включение ТВ с телефона** (Wake-on-LAN), установка на **несколько телевизоров**.
  - **Самообновление без браузера**: приложение само скачивает новую версию, проверяет её и открывает установку Android.
  - Усиление безопасности по итогам аудита; много исправлений после тестирования на настоящем ТВ.

## 2.2.5 — always the newest build / всегда свежая сборка
- **EN:** right before installing, the app checks GitHub for a newer release than the one in the list and installs it
  (verified by the SHA-256 GitHub publishes). No internet or GitHub doesn't answer in 6 s — the build from the list is
  installed as before. If the TV doesn't let the app in right after start, it retries by itself for two minutes.
- **RU:** перед установкой приложение проверяет на GitHub, нет ли сборки новее, чем в списке, и ставит её (с проверкой
  SHA-256 от GitHub). Нет интернета или GitHub не ответил за 6 с — ставится сборка из списка, как раньше. Если сразу
  после запуска телевизор не пустил, приложение само пробует подключиться снова в течение двух минут.

## 2.2.4 — simpler settings, self-updating app list / проще настройки, список обновляется сам
- **EN:** the app list now comes from this repository and refreshes every week, so new builds of Jellyfin, Moonlight and
  others arrive without a TV Installer update (the copy inside the app is the offline fallback). Settings are simpler:
  server addresses and catalog sources moved to developer settings (tap the version line 7 times). Your own .wgt:
  Apps → ⋮ → "Install .wgt" or "Download a .wgt from a link"; remove it from the list on its card.
- **RU:** список приложений берётся из этого репозитория и обновляется раз в неделю — новые сборки Jellyfin, Moonlight и
  других приходят без обновления TV Installer (копия внутри приложения — запасная, без интернета). Настройки проще:
  адреса серверов и источники каталога — в настройках для разработчика (7 нажатий на строку версии). Свой .wgt:
  «Приложения» → ⋮ → «Установить .wgt» или «Скачать .wgt по ссылке»; убрать из списка — в его карточке.

## 2.2.3 — clearer and more reliable / понятнее и надёжнее
- **EN:** variants of one app (Jellyfin, Moonlight, TizenBrew builds) are told apart — only the one really on the TV shows
  as installed, the others say "Another variant is on the TV" and explain what each build is for. A lost connection to
  the TV is noticed right away and restored automatically. A TV you have used before is no longer sent back to
  "prepare this TV" when it is just slow to answer. Uninstall asks for confirmation. After installing: "Open on TV".
  Installed queue items leave the queue. Lampa updates via "Update to …". Temporary packages are removed from the TV.
  Descriptions follow the app language; TVs are named by model instead of codes or IPs.
- **RU:** варианты одного приложения (сборки Jellyfin, Moonlight, TizenBrew) больше не путаются: «Установлено» только у
  того, что реально стоит, у остальных — «На ТВ стоит другой вариант» и пояснение, чем сборки отличаются. Потеря связи
  с ТВ видна сразу и восстанавливается сама. Уже подготовленный ТВ, который просто медленно ответил, больше не
  отправляет «подготовить телевизор». Удаление — с подтверждением. После установки — «Открыть на ТВ». Установленное
  уходит из очереди. Lampa обновляется кнопкой «Обновить до …». Временные пакеты удаляются с ТВ. Описания — на языке
  интерфейса; телевизоры названы моделью, а не кодом или IP.

## 2.2.2 — reinstall fix / исправление переустановки
- **EN:** «Reinstall over it» now really removes an app installed from another source (e.g. Tizen Studio) before
  installing: the TV's uninstaller needs the full application id. Previously the old app stayed and the install failed
  with «Author certificate not match».
- **RU:** «Установить поверх» теперь действительно удаляет приложение, поставленное из другого источника (например, из
  Tizen Studio): удалению на ТВ нужен полный id приложения. Раньше старая версия оставалась, и установка падала с
  «Author certificate not match».

## 2.2.1 — security update / обновление безопасности
- **EN:** BouncyCastle 1.86 (fixes CVE-2026-17508), JSch 2.28.8, kotlinx-coroutines 1.11, build toolchain update (Gradle 9.8.1, AGP 9.4.1, Kotlin 2.4.21).
  Samsung browser sign-in accepts the token only from Samsung's page (Origin check, HTTPS only). HTTPS downloads can't be
  redirected to HTTP. Catalog entries with unsafe ids are skipped. The home-screen widget opens the remote only for known TVs.
  Backup password is protected from screenshots.
- **RU:** BouncyCastle 1.86 (уязвимость CVE-2026-17508), обновлены JSch, корутины и инструменты сборки. Вход Samsung через
  браузер — только со страницы Samsung. Загрузки по HTTPS не переходят на HTTP. Проверка записей каталога. Пульт с виджета —
  только для известных ТВ. Пароль резервной копии защищён от скриншотов.

## 2.2.0 — English & Russian / два языка
- **EN:** the app is available in English and Russian (follows the phone language; switch in Settings → Language).
  The TV card shows the TV name instead of its IP; the certificate button is no longer cut off.
- **RU:** интерфейс на русском и английском (как язык телефона, сменить — Настройки → Язык). На карточке ТВ — название
  вместо IP; кнопка «Получить сертификат» не обрезается.

## 2.1.0
- **EN:** short version numbers; the app checks GitHub for updates by itself (every 12 hours) and offers to download them.
- **RU:** короткие номера версий; приложение само проверяет обновления на GitHub (раз в 12 часов) и предлагает скачать.

## 2.0 (builds 277–298) / сборки 277–298
- **EN:** Samsung-only app; animated step-by-step Developer Mode guide (following Samsung's official guide); Lampa installed
  from its latest GitHub release with an update badge; bottom bar TV / Apps / Settings; certificate step on the TV card;
  automatic switch to Apps when the TV is ready; plain-language texts; GitHub Sponsors link.
- **RU:** только Samsung; анимированная инструкция режима разработчика по официальной инструкции Samsung; Lampa — из
  последнего релиза на GitHub с меткой «Есть обновление»; нижняя панель Телевизор / Приложения / Настройки; сертификат —
  шагом на карточке ТВ; переход в «Приложения», когда ТВ готов; понятные тексты; «Поддержать проект».
