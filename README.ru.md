[English](README.md) · **Русский** · [O'zbekcha](README.uz.md)

# TV Installer — установка приложений на Samsung Smart TV с телефона

[![Release](https://img.shields.io/github/v/release/sunic007/tvinstaller?label=release&color=3d8bff)](https://github.com/sunic007/tvinstaller/releases/latest) [![Downloads](https://img.shields.io/github/downloads/sunic007/tvinstaller/total?color=2ea043)](https://github.com/sunic007/tvinstaller/releases) ![Android](https://img.shields.io/badge/Android-7.0%2B-3ddc84?logo=android&logoColor=white) ![Tizen TV](https://img.shields.io/badge/Tizen-TV-1428a0) ![Languages](https://img.shields.io/badge/UI-English%20%7C%20Русский%20%7C%20O'zbekcha-8a63d2)

Android-приложение для установки приложений `.wgt` на телевизоры **Samsung (Tizen)** прямо с телефона — без компьютера
и Tizen Studio. Подписывает пакет само и ставит его на ТВ по Wi-Fi.

**⬇️ [Скачать TvInstaller.apk](https://github.com/sunic007/tvinstaller/releases/latest/download/TvInstaller.apk)** — последняя версия
· все версии — [Releases](https://github.com/sunic007/tvinstaller/releases)
· что нового — [CHANGELOG.md](CHANGELOG.md)
· [политика конфиденциальности](https://sunic007.github.io/tvinstaller/privacy.html)
· ❤️ [поддержать проект](https://github.com/sponsors/sunic007)

Главное приложение в каталоге — **[Lampa для Samsung](https://github.com/sunic007/lampa-samsung)**: TV Installer
ставит её последнюю версию прямо из релизов GitHub, дальше она обновляется на телевизоре сама.

<p align="center">
  <img src="docs/screenshots/01.png" width="30%">
  <img src="docs/screenshots/02.png" width="30%">
  <img src="docs/screenshots/03.png" width="30%">
</p>
<details>
<summary>Ещё скриншоты</summary>

<p align="center">
  <img src="docs/screenshots/04.png" width="30%">
  <img src="docs/screenshots/05.png" width="30%">
  <img src="docs/screenshots/06.png" width="30%">
</p>
<p align="center">
  <img src="docs/screenshots/07.png" width="30%">
  <img src="docs/screenshots/08.png" width="30%">
  <img src="docs/screenshots/09.png" width="30%">
</p>
</details>

## Возможности

- **Сам находит телевизор** в той же сети Wi-Fi; можно работать с несколькими ТВ.
- **Мастер «Не подключается?»** по шагам проверяет Wi-Fi, телевизор, режим разработчика и адрес, указанный на ТВ, и
  прямо говорит, если ТВ настроен на другое устройство (ставить приложения на Samsung может только один телефон или
  компьютер за раз).
- **Видео-инструкция** по включению режима разработчика на ТВ — на русском, English и O'zbekcha.
- **Сертификат Samsung один раз** — вход в аккаунт Samsung, без компьютера и Tizen Studio. За месяц до окончания
  придёт напоминание, продление — в одно нажатие; есть резервная копия и **восстановление из неё**.
- **Каталог из 40+ приложений** — медиатеки, плееры, стриминг, IPTV — и подборка **«Рекомендуем»**; можно поставить
  и свой `.wgt` из файла или по ссылке. Для вариантов одного приложения
  (сборки Jellyfin, Moonlight) объяснено, чем они отличаются.
- **Установка в одно касание**, каждый шаг виден, потом — **«Открыть на ТВ»**. В списке **«На ТВ»** — **«Открыть /
  Удалить»** и **«Обновить всё»**; раз в день приходит уведомление, если вышли обновления.
- **Пульт** в телефоне и **включение телевизора с телефона** (Wake-on-LAN).
- **[Lampa для Samsung](https://github.com/sunic007/lampa-samsung)** ставится из последнего релиза на GitHub и дальше
  обновляется на телевизоре сама.
- **Самообновление без браузера**: приложение само скачивает новую версию, проверяет её и открывает установку Android.

## Что нужно

- Телефон на Android 7.0+ и телевизор Samsung с Tizen — в одной Wi-Fi сети (не гостевой).
- Бесплатный аккаунт Samsung (для сертификата установки).

## Как установить приложение на ТВ
<table>
<tr>
<td valign="top" width="260">

<p align="center"><a href="https://youtu.be/U4VGa0fGYUI"><img src="docs/video/thumbnails/thumbnail-ru.jpg" width="220" alt="Русский"></a></p>

</td>
<td valign="top">

1. **IP телефона** TV Installer показывает сам — вверху экрана «Телевизоры».
2. **Включите режим разработчика на ТВ:** откройте вкладку **Apps** (Приложения) → внизу **App Settings** →
   наберите на пульте `1 2 3 4 5` → включите **Developer mode**, впишите IP телефона и нажмите **OK**.
   Перезагрузите телевизор (кнопку питания держать ~2 секунды). Как это выглядит, показано в видео выше.
3. **Установите TV Installer** на телефон: скачайте APK и откройте его (Android попросит разрешить установку из
   этого источника).
4. В TV Installer выберите **телевизор**, один раз войдите в **Samsung** за сертификатом и выберите приложение из
   каталога или свой **файл `.wgt`** — TV Installer подпишет пакет и установит его.
5. Новые версии ставятся поверх старых, настройки приложения на ТВ сохраняются.

</td>
</tr>
</table>

<details>
<summary>Другие языки</summary>

<p align="center"><a href="https://youtu.be/L6nK4SBWKP0"><img src="docs/video/thumbnails/thumbnail-en.jpg" width="220" alt="English"></a> <a href="https://youtu.be/AB0fsIuFSII"><img src="docs/video/thumbnails/thumbnail-uz.jpg" width="220" alt="O'zbekcha"></a></p>

</details>




## Частые вопросы

**ТВ не находится или не подключается.** Откройте меню ⋮ → «Не подключается?» — мастер проверит всё по
шагам. Проверьте также, что телефон и ТВ в одной сети, а в режиме разработчика на ТВ указан IP именно
телефона. После смены IP — снова перезагрузите ТВ.

**Ошибка подписи или установки.** Удалите старую версию приложения на ТВ и установите заново.

**Безопасно ли.** С телевизором приложение общается только внутри домашней сети; к Samsung обращается только за
сертификатом, к GitHub — за приложениями. Подробнее — в
[политике конфиденциальности](https://sunic007.github.io/tvinstaller/privacy.html).

## Отказ от ответственности

TV Installer — независимый проект, не связан с Samsung и не одобрен ею. Samsung и Tizen — товарные знаки Samsung
Electronics. Приложение использует тот же способ получения сертификата, что и Tizen Studio от Samsung: вы входите в
свой аккаунт Samsung, и сертификат для вашего ТВ выдаёт Samsung. За устанавливаемые приложения отвечает пользователь;
само приложение не хранит и не предоставляет медиаконтент.

## Поддержать проект
TV Installer бесплатный. Поддержать развитие можно на **[GitHub Sponsors](https://github.com/sponsors/sunic007)**
(в приложении: «Настройки → Поддержать проект»).
