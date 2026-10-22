# Changelog / История изменений

[Download the latest APK / Скачать последнюю версию](https://github.com/sunic007/tvinstaller/releases/latest/download/SunicTvInstaller.apk)

## 2.3.11 — надёжнее на слабых телефонах / more reliable on low-end phones
- **EN:** Re-signing an app no longer loads the whole package into memory — large apps install on phones with little RAM. The remote stops all its background work when you close it. Cancelling an install on an LG TV stops right away. The «News» item is removed (news are in the Telegram group now).
- **RU:** Пересборка приложения больше не загружает весь пакет в память — большие приложения ставятся и на телефонах с малым объёмом памяти. Пульт полностью останавливает свою фоновую работу, когда его закрыли. Отмена установки на ТВ LG срабатывает сразу. Пункт «Новости» убран — новости теперь в группе Telegram.

## 2.3.10 — точное управление пультом Samsung / exact remote control for Samsung
- **EN:** Remote → More → «Exact control»: on Samsung models that accept the usual remote's buttons but ignore them, the buttons are pressed by code on the TV itself (arrows, OK, Back, Home, volume, channels). Off by default. While it's on, Lampa on the TV runs with a debug port visible on your home network, so the mode switches itself off after 15 minutes without presses. «Check the remote» tells whether you need it at all.
- **RU:** Пульт → Ещё → «Точное управление»: на моделях Samsung, которые кнопки обычного пульта принимают, но не выполняют, кнопки нажимает код на самом телевизоре (стрелки, OK, «Назад», «Домой», громкость, каналы). По умолчанию выключено. Пока режим включён, Lampa на ТВ работает с портом отладки, который виден в домашней сети, — поэтому режим сам выключается через 15 минут без нажатий. «Проверить пульт» подскажет, нужно ли оно вообще.

## 2.3.9 — без ложных ошибок установки / no false install errors
- **EN:** TV Installer reads the installer's own result line first: harmless words in the TV's log no longer turn a successful install into an error. After deleting a distributor certificate the list refreshes right away. An oversized answer from the certificate server is a clear error, not a crash.
- **RU:** TV Installer сначала смотрит на итог самого установщика: безобидные слова в журнале ТВ больше не превращают удачную установку в ошибку. После удаления сертификата дистрибьютора список сразу обновляется. Слишком большой ответ сервера сертификатов — понятная ошибка, а не вылет.

## 2.3.8 — без тихих удалений, ключ сохраняется, свежие библиотеки / no silent uninstall, key kept, fresh libraries
- **EN:** TV Installer never removes an app from the TV by itself anymore: if the TV refuses an update, you're asked first (the app's data on the TV would be deleted). Your Samsung author key is kept when you add another TV or renew — updates install over the old version. Cancel stops an install right away; a TV that hangs is no longer taken for success. The "no background service" fallback is only used on old TVs. Fresh libraries (Compose, OkHttp).
- **RU:** TV Installer больше никогда сам не удаляет приложение с ТВ: если телевизор не принял обновление, сначала спросит (данные приложения на ТВ пропали бы). Ключ автора Samsung сохраняется при подключении нового ТВ и продлении — обновления ставятся поверх. «Отмена» сразу прерывает установку, зависание ТВ больше не считается успехом. Установка «без фоновой службы» — только для старых ТВ. Свежие библиотеки (Compose, OkHttp).

## 2.3.6 — privacy and reliability / приватность и надёжность
- **EN:** "Report a problem" now hides email addresses and the last part of IP addresses in the log. The system Back gesture shows the predictive-back preview on Android 13+. The privacy policy is updated: what stays on your home network and what goes over the internet. Nothing else changes in how the app works.
- **RU:** «Сообщить о проблеме» теперь скрывает в журнале адреса почты и последнюю часть IP-адресов. Жест «Назад» на Android 13+ показывает предпросмотр. Обновлена политика конфиденциальности: что остаётся в домашней сети, а что идёт через интернет. В остальном приложение работает как раньше.

## 2.3.5 — понятный каталог и помощь в Telegram / clear catalog and Telegram help
- **EN:** every Samsung app in the catalog now explains what it is and what you need for it ("Details"). New in Settings: "Questions and help" (Telegram group), "News" (channel) and "Report a problem" — sends the log to the developer.
- **RU:** у каждого приложения в каталоге понятное описание: что это и что для него нужно («Подробнее»). В настройках — «Вопросы и помощь» (группа в Telegram), «Новости» (канал) и «Сообщить о проблеме» — журнал разработчику.

## 2.3.4 — clearer wording / понятные тексты
- **EN:** all texts in English, Russian and Uzbek reviewed: same terms everywhere, no jargon. The TV list header now says what to do with the address: "Enter on your TV: <IP>". Fixed: the sign-in screen could be skipped when a broken saved sign-in was left from before.
- **RU:** все тексты на русском, английском и узбекском проверены: единые термины, без жаргона. В шапке списка телевизоров теперь понятно, что делать с адресом: «Введите на ТВ: <IP>». Исправлено: экран входа мог не появиться, если от прошлых версий остался повреждённый сохранённый вход.

## 2.3.3 — sign-in screen and new splash / экран входа и новая заставка
- **EN:**
  - **Sign-in screen at launch:** sign in to your Samsung account in one tap, or choose "I'll sign in later".
  - **New splash:** the TV switches on, the caption goes English → Russian → Uzbek; the app opens faster, without a long dark screen.
  - **Setup steps:** finished steps disappear (numbers 1–4 stay), and the bar hides once the TV is ready.
  - TVs that are off no longer show as "not found" cards; labels shrink to fit instead of breaking mid-word.
- **RU:**
  - **Экран входа при запуске:** вход в аккаунт Samsung в одно нажатие или «Авторизуюсь позже».
  - **Новая заставка:** телевизор «включается», подпись по очереди на английском, русском и узбекском; приложение открывается быстрее, без долгого тёмного экрана.
  - **Шаги настройки:** выполненные шаги исчезают (номера 1–4 сохраняются), а когда ТВ готов, полосы нет.
  - Выключенные телевизоры больше не показываются карточками «Не найден»; подписи уменьшаются, а не рвутся посреди слова.

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
