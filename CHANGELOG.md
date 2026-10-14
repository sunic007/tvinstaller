# Changelog / История изменений

[Download the latest APK / Скачать последнюю версию](https://github.com/sunic007/tvinstaller/releases/latest/download/TvInstaller.apk)

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
