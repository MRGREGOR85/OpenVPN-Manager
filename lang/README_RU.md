<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN через CMD: выбираешь страну, вводишь сервер — и ты подключён. 19 VPN-провайдеров, kill switch и speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Скачать GHOST-NET" width="380"></a>

**Windows 10 и 11 · работает с GhostVPN**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Главный экран GHOST-NET" width="100%">

📸 **Главный экран.** Вверху: страны, где у твоего провайдера есть серверы. Под ними: коды стран для ввода, например `pl` = Польша. Ниже: состояние kill switch и 19 VPN-провайдеров, выделенный — тот, что используется. В самом низу вводишь код страны.

<br>

---

## 💀 Что такое GHOST-NET?

Менеджер VPN в обычном окне CMD. Он подключает тебя через OpenVPN к серверу твоего собственного VPN-провайдера, и сайты видят IP сервера вместо твоего. Использует те же файлы серверов, что и [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Программа говорит на 29 языках. Язык меняется клавишей `TAB` на главном экране.

<br>

---

## ✨ Возможности

| Возможность | Что делает |
|---|---|
| **19 VPN-провайдеров** | NordVPN, ProtonVPN, Surfshark, Mullvad и другие. Переключение стрелками или номером. |
| **Пинг в реальном времени** | Список серверов показывает, какой самый быстрый. |
| **Kill switch** | Брандмауэр Windows блокирует интернет вне VPN. Если туннель упадёт, твой IP не утечёт. Домашняя сеть продолжает работать. |
| **Защита DNS** | DNS-запросы не выходят за пределы туннеля. |
| **Экран подключения** | Новый IP, город, провайдер, пинг и шифр. |
| **Speedtest** | Тест скорости на файле 1 ГБ, результат в Мбит/с. |
| **Умные ошибки** | Отчёт в Блокноте, предложение следующего сервера и автоматическая загрузка новых серверов NordVPN. |
| **29 языков** | Программа говорит на 29 языках. Язык меняется клавишей `TAB` на главном экране. |

<br>

---

## 📋 Что нужно

**Windows 10 или 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (или [OpenVPN](https://openvpn.net/community-downloads/)) · **аккаунт у VPN-провайдера** · **права администратора** (скрипт сам их запросит)

<br>

---

## 📖 Инструкция

<br>

### 1️⃣ Скачай

Нажми **Скачать GHOST-NET**. Перемести **GhostNet.exe** в отдельную папку, например `C:\GHOST-NET`, потому что скрипт хранит рядом с собой настройки и логины.

<br>

### 2️⃣ Запусти

Дважды щёлкни **GhostNet.exe** и нажми **Да**, когда Windows попросит разрешение. Если Windows покажет предупреждение: **Подробнее** → **Выполнить в любом случае**. При первом запуске выбери свой язык.

<img src="../screenshots/language-select.png" alt="29 языков" width="100%">

📸 **29 языков.** Программа говорит на 29 языках. Язык меняется клавишей `TAB` на главном экране.

<br>

### 3️⃣ Выбери страну

Введи код страны и нажми **Enter**, например `pl`, `de` или `us`. Провайдера меняешь стрелками или номером от `1` до `19`.

<br>

### 4️⃣ Выбери сервер

Введи имя сервера из списка или только его начало, например `pl1273`, и нажми **Enter**.

<img src="../screenshots/server-ping.png" alt="Список серверов с пингом" width="100%">

📸 **Список серверов.** У каждого сервера в скобках пинг, то есть время ответа: чем меньше `ms`, тем быстрее. `udp` обычно быстрее, `tcp` лучше проходит блокировки. Внизу вводишь выбранный сервер.

<br>

### 5️⃣ Введи логин (только в первый раз)

Скрипт спросит имя пользователя и пароль OpenVPN и подскажет, где их найти. У NordVPN и Surfshark отдельные *Service credentials*, а не e-mail и пароль от аккаунта.

<img src="../screenshots/login.png" alt="Первый вход" width="100%">

📸 **Первый вход.** Скрипт показывает, для какого провайдера данные и где их взять. Пароль скрыт звёздочками. Логин сохраняется один раз, и в следующий раз его не нужно вводить.

<br>

### 6️⃣ Готово

<img src="../screenshots/connected.png" alt="Экран подключения" width="100%">

📸 **Подключено.** `NODE_IP` — твой новый IP, который видят сайты. `PING` — скорость туннеля, `ENCRYPTION` — шифр, а `KILL_SWITCH` показывает, заблокирован ли интернет вне VPN. `LOCATION` и `PROVIDER` — город и компания сервера. Внизу: `1` speedtest, `2` отключить, `3` kill switch.

<br>

---

## ⌨️ Команды

| Введи | Что делает |
|---|---|
| `pl`, `de`, `us`… | серверы в этой стране |
| `1` … `19` | смена VPN-провайдера |
| `TAB` | смена языка |
| `ks` | включить или выключить kill switch |
| `fs` | полный экран или окно |
| `Alt+C` | отключить VPN (работает везде) |
| `1` / `2` / `3` после подключения | speedtest / отключить / kill switch |

<br>

---

## 🌍 Провайдеры

`NordVPN` (в списке как **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET не продаёт VPN: ты пользуешься своим аккаунтом. Файлы серверов добавляешь в GhostVPN.

<br>

---

## 🆘 Что-то не работает?

| Что я вижу | Что делать |
|---|---|
| **OpenVPN**: не установлен | Установи [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) или [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: нет файлов серверов | Добавь серверы этого провайдера в GhostVPN или выбери другого провайдера. |
| **AUTH_FAILED** | Выбери `1`, чтобы попробовать следующий сервер. Если не работает ни один, выбери `2` и введи логин заново. |
| **TUNNEL FAILED** | Прочитай отчёт в Блокноте. Выбери другой сервер. |
| Нет интернета после закрытия окна | Запусти скрипт и выбери **СНЯТЬ БЛОКИРОВКУ** или введи `ks`. |

> 🔒 Логины остаются только на твоём компьютере, в папке рядом со скриптом. Никому не давай эту папку.

<br>

---

## 📜 Лицензия

### Только для частного домашнего использования. GHOST-NET принадлежит исключительно автору, MRGREGOR85.

**Запрещено** продавать его, давать или отправлять другим, выкладывать на другие сайты, форумы или в Discord, использовать в компании, изменять или копировать его код. Каждый скачивает свою копию с этой страницы. Полный текст: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Автор

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Если GHOST-NET тебе помогает, оставь ⭐

</div>
