<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN через CMD: обираєш країну, вводиш сервер, і ти підключений. 19 VPN-провайдерів, kill switch і speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Завантажити GHOST-NET" width="380"></a>

**Windows 10 і 11 · працює з GhostVPN**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · 🇺🇦 Українська · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Головний екран GHOST-NET" width="100%">

📸 **Головний екран.** Угорі: країни, де твій провайдер має сервери. Під ними: коди країн для введення, наприклад `pl` = Польща. Нижче: стан kill switch і 19 VPN-провайдерів, виділений — той, що використовується. У самому низу вводиш код країни.

<br>

---

## 💀 Що таке GHOST-NET?

Менеджер VPN у звичайному вікні CMD. Він підключає тебе через OpenVPN до сервера твого власного VPN-провайдера, тож сайти бачать IP сервера замість твого. Використовує ті самі файли серверів, що й [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Програма розмовляє 29 мовами. Мову змінюєш клавішею `TAB` на головному екрані.

<br>

---

## ✨ Можливості

| Можливість | Що робить |
|---|---|
| **19 VPN-провайдерів** | NordVPN, ProtonVPN, Surfshark, Mullvad та інші. Перемикання стрілками або номером. |
| **Пінг наживо** | Список серверів показує, який найшвидший. |
| **Kill switch** | Брандмауер Windows блокує інтернет поза VPN. Якщо тунель впаде, твій IP не витече. Домашня мережа працює далі. |
| **Захист DNS** | DNS-запити не виходять за межі тунелю. |
| **Екран підключення** | Новий IP, місто, провайдер, пінг і шифр. |
| **Speedtest** | Тест швидкості на файлі 1 ГБ, результат у Мбіт/с. |
| **Розумні помилки** | Звіт у Блокноті, пропозиція наступного сервера та автоматичне завантаження нових серверів NordVPN. |
| **29 мов** | Програма розмовляє 29 мовами. Мову змінюєш клавішею `TAB` на головному екрані. |

<br>

---

## 📋 Що потрібно

**Windows 10 або 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (або [OpenVPN](https://openvpn.net/community-downloads/)) · **обліковий запис у VPN-провайдера** · **права адміністратора** (скрипт сам їх попросить)

<br>

---

## 📖 Інструкція

<br>

### 1️⃣ Завантаж

Натисни **Завантажити GHOST-NET**. Перемісти **GhostNet.exe** в окрему папку, наприклад `C:\GHOST-NET`, бо скрипт зберігає поруч із собою налаштування й логіни.

<br>

### 2️⃣ Запусти

Двічі клацни **GhostNet.exe** і натисни **Так**, коли Windows попросить дозвіл. Якщо Windows покаже попередження: **Докладніше** → **Усе одно запустити**. Під час першого запуску обери свою мову.

<img src="../screenshots/language-select.png" alt="29 мов" width="100%">

📸 **29 мов.** Програма розмовляє 29 мовами. Мову змінюєш клавішею `TAB` на головному екрані.

<br>

### 3️⃣ Обери країну

Введи код країни й натисни **Enter**, наприклад `pl`, `de` або `us`. Провайдера змінюєш стрілками або номером від `1` до `19`.

<br>

### 4️⃣ Обери сервер

Введи назву сервера зі списку або лише її початок, наприклад `pl1273`, і натисни **Enter**.

<img src="../screenshots/server-ping.png" alt="Список серверів із пінгом" width="100%">

📸 **Список серверів.** Біля кожного сервера в дужках пінг, тобто час відповіді: що менше `ms`, то швидше. `udp` зазвичай швидший, `tcp` краще проходить блокування. Унизу вводиш обраний сервер.

<br>

### 5️⃣ Введи логін (лише першого разу)

Скрипт попросить ім'я користувача й пароль OpenVPN і підкаже, де їх знайти. NordVPN і Surfshark мають окремі *Service credentials*, а не e-mail і пароль від облікового запису.

<img src="../screenshots/login.png" alt="Перший вхід" width="100%">

📸 **Перший вхід.** Скрипт показує, для якого провайдера дані й де їх узяти. Пароль приховано зірочками. Логін зберігається один раз, і наступного разу його не треба вводити.

<br>

### 6️⃣ Готово

<img src="../screenshots/connected.png" alt="Екран підключення" width="100%">

📸 **Підключено.** `NODE_IP` — твій новий IP, який бачать сайти. `PING` — швидкість тунелю, `ENCRYPTION` — шифр, а `KILL_SWITCH` показує, чи заблоковано інтернет поза VPN. `LOCATION` і `PROVIDER` — місто й компанія сервера. Унизу: `1` speedtest, `2` відключити, `3` kill switch.

<br>

---

## ⌨️ Команди

| Введи | Що робить |
|---|---|
| `pl`, `de`, `us`… | сервери в цій країні |
| `1` … `19` | зміна VPN-провайдера |
| `TAB` | зміна мови |
| `ks` | увімкнути або вимкнути kill switch |
| `fs` | повний екран або вікно |
| `Alt+C` | відключити VPN (працює всюди) |
| `1` / `2` / `3` після підключення | speedtest / відключити / kill switch |

<br>

---

## 🌍 Провайдери

`NordVPN` (у списку як **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET не продає VPN: ти користуєшся власним обліковим записом. Файли серверів додаєш у GhostVPN.

<br>

---

## 🆘 Щось не працює?

| Що я бачу | Що робити |
|---|---|
| **OpenVPN**: не встановлено | Встанови [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) або [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: немає файлів серверів | Додай сервери цього провайдера в GhostVPN або обери іншого провайдера. |
| **AUTH_FAILED** | Обери `1`, щоб спробувати наступний сервер. Якщо жоден не працює, обери `2` і введи логін ще раз. |
| **TUNNEL FAILED** | Прочитай звіт у Блокноті. Обери інший сервер. |
| Немає інтернету після закриття вікна | Запусти скрипт і обери **ЗНЯТИ БЛОКУВАННЯ** або введи `ks`. |

> 🔒 Логіни залишаються лише на твоєму комп'ютері, у папці поруч зі скриптом. Нікому не давай цю папку.

<br>

---

## 📜 Ліцензія

### Лише для приватного домашнього використання. GHOST-NET належить виключно автору, MRGREGOR85.

**Заборонено** продавати його, давати чи надсилати іншим, викладати на інші сайти, форуми чи в Discord, використовувати у фірмі, змінювати або копіювати його код. Кожен завантажує власну копію з цієї сторінки. Повний текст: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Автор

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Якщо GHOST-NET тобі допомагає, залиш ⭐

</div>
