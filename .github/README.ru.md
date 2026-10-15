<div align="center">

<img src="../docs/icon.png" width="96" alt="TV Installer">

# TV Installer

Установка приложений на <b>Samsung Smart TV</b> прямо с телефона — без компьютера и Tizen Studio

[![Release](https://img.shields.io/github/v/release/sunic007/tvinstaller?label=release&color=3d8bff)](https://github.com/sunic007/tvinstaller/releases/latest) [![Downloads](https://img.shields.io/github/downloads/sunic007/tvinstaller/total?color=2ea043)](https://github.com/sunic007/tvinstaller/releases) ![Android](https://img.shields.io/badge/Android-7.0%2B-3ddc84?logo=android&logoColor=white) ![Tizen TV](https://img.shields.io/badge/Tizen-TV-1428a0)

<a href="https://github.com/sunic007/tvinstaller/releases/latest/download/SunicTvInstaller.apk"><img src="https://img.shields.io/badge/Скачать-SunicTvInstaller.apk-3d8bff?style=for-the-badge&logo=android&logoColor=white" alt="Скачать SunicTvInstaller.apk"></a>

[Что нового](CHANGELOG.md) · [Все версии](https://github.com/sunic007/tvinstaller/releases) · [Конфиденциальность](https://sunic007.github.io/tvinstaller/privacy.html) · ❤️ [Поддержать](https://github.com/sponsors/sunic007)

[English](README.md) · **Русский** · [O'zbekcha](README.uz.md)

</div>

## Как это работает

<table>
<tr>
<td width="300" align="center" valign="top"><img src="../docs/demo/demo-ru.gif" width="280" alt="Вход, видеоинструкция, подключение телевизора и установка приложения"></td>
<td valign="top">

📲 <b>1. Установите приложение</b><br>Скачайте <b>SunicTvInstaller.apk</b> и откройте его на Android-телефоне.

🔑 <b>2. Войдите в аккаунт Samsung</b><br>Один раз. Сертификат для телевизора Samsung выдаст сам.

📺 <b>3. Подготовьте телевизор</b><br>Включите режим разработчика с адресом телефона — в приложении есть видео на 1 минуту.

🔍 <b>4. Подключитесь</b><br>Приложение само найдёт телевизор в вашей сети Wi‑Fi.

✅ <b>5. Установите</b><br>Выберите приложение из каталога (40+) и нажмите <b>Установить</b>.

Интерфейс на <b>русском, английском и узбекском</b> — по языку телефона.

<p><a href="https://youtu.be/U4VGa0fGYUI"><img src="../docs/video/thumbnails/thumbnail-ru.jpg" width="160" align="left" alt="video"></a>
▶ <b>Режим разработчика</b> — видео 1 мин<br>
<sub>Apps → App Settings<br>→ <code>1 2 3 4 5</code> → Developer mode <b>On</b><br>→ IP телефона → <b>OK</b> → перезагрузите ТВ</sub></p>

<br clear="left">

</td>
</tr>
</table>

<p align="center">
  <img src="../docs/screenshots/01.png" width="30%">
  <img src="../docs/screenshots/02.png" width="30%">
  <img src="../docs/screenshots/03.png" width="30%">
</p>
<details>
<summary>Ещё скриншоты</summary>

<p align="center">
  <img src="../docs/screenshots/04.png" width="30%">
  <img src="../docs/screenshots/05.png" width="30%">
  <img src="../docs/screenshots/06.png" width="30%">
</p>
<p align="center">
  <img src="../docs/screenshots/07.png" width="30%">
  <img src="../docs/screenshots/08.png" width="30%">
  <img src="../docs/screenshots/09.png" width="30%">
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
