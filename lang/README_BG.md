<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN от CMD: избираш държава, въвеждаш сървър и си свързан. 19 VPN доставчици, kill switch и тест на скоростта.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Изтегли GHOST-NET" width="380"></a>

**Windows 10 и 11 · работи с GhostVPN**

## [🇵🇱 Polski](../README_PL.md) &nbsp; [🇬🇧 English](../README.md) &nbsp; [🇩🇪 Deutsch](README_DE.md) &nbsp; [🇨🇿 Čeština](README_CS.md) &nbsp; [🇸🇰 Slovenčina](README_SK.md) &nbsp; [🇺🇦 Українська](README_UK.md) &nbsp; [🇷🇺 Русский](README_RU.md) &nbsp; [🇱🇹 Lietuvių](README_LT.md) &nbsp; [🇱🇻 Latviešu](README_LV.md) &nbsp; [🇪🇪 Eesti](README_ET.md) &nbsp; [🇪🇸 Español](README_ES.md) &nbsp; [🇫🇷 Français](README_FR.md) &nbsp; [🇮🇹 Italiano](README_IT.md) &nbsp; [🇵🇹 Português](README_PT.md) &nbsp; [🇳🇱 Nederlands](README_NL.md) &nbsp; [🇸🇪 Svenska](README_SV.md) &nbsp; [🇩🇰 Dansk](README_DA.md) &nbsp; [🇳🇴 Norsk](README_NO.md) &nbsp; [🇫🇮 Suomi](README_FI.md) &nbsp; [🇭🇺 Magyar](README_HU.md) &nbsp; [🇷🇴 Română](README_RO.md) &nbsp; [🇧🇬 Български](README_BG.md) &nbsp; [🇬🇷 Ελληνικά](README_EL.md) &nbsp; [🇭🇷 Hrvatski](README_HR.md) &nbsp; [🇷🇸 Српски](README_SR.md) &nbsp; [🇸🇮 Slovenščina](README_SL.md) &nbsp; [🇹🇷 Türkçe](README_TR.md) &nbsp; [🇻🇳 Tiếng Việt](README_VI.md) &nbsp; [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Главен екран на GHOST-NET" width="100%">

📸 **Главен екран.** Горе: държавите, в които доставчикът ти има сървъри. Под тях: кодовете на държавите за въвеждане, например `pl` = Полша. По-надолу: състоянието на kill switch и 19-те VPN доставчици, маркираният е използваният. Най-долу въвеждаш код на държава.

<br>

---

## 💀 Какво е GHOST-NET?

VPN мениджър в обикновен CMD прозорец. Свързва те чрез OpenVPN със сървър на твоя собствен VPN доставчик, така че сайтовете виждат IP адреса на сървъра вместо твоя. Използва същите сървърни файлове като [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Програмата говори 29 езика. Сменяш езика с `TAB` на главния екран.

<br>

---

## ✨ Функции

| Функция | Какво прави |
|---|---|
| **19 VPN доставчици** | NordVPN, ProtonVPN, Surfshark, Mullvad и други. Сменяш със стрелките или с номер. |
| **Пинг на живо** | Списъкът със сървъри показва кой е най-бърз. |
| **Kill switch** | Защитната стена на Windows блокира интернета извън VPN. Ако тунелът падне, IP адресът ти не изтича. Домашната мрежа продължава да работи. |
| **DNS защита** | DNS заявките не излизат извън тунела. |
| **Екран на връзката** | Нов IP, град, доставчик, пинг и шифър. |
| **Тест на скоростта** | Тест със файл от 1 GB, резултат в Mbit/s. |
| **Умни грешки** | Отчет в Notepad, предложение за следващ сървър и автоматично изтегляне на нови сървъри на NordVPN. |
| **29 езика** | Програмата говори 29 езика. Сменяш езика с `TAB` на главния екран. |

<br>

---

## 📋 Какво ти трябва

**Windows 10 или 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (или [OpenVPN](https://openvpn.net/community-downloads/)) · **акаунт при VPN доставчик** · **администраторски права** (скриптът сам ги иска)

<br>

---

## 📖 Ръководство

<br>

### 1️⃣ Изтегли

Натисни **Изтегли GHOST-NET**. Премести **GhostNet.exe** в отделна папка, например `C:\GHOST-NET`, защото скриптът записва настройките и данните за вход до себе си.

<br>

### 2️⃣ Стартирай

Щракни два пъти върху **GhostNet.exe** и натисни **Да**, когато Windows поиска разрешение. Ако Windows покаже предупреждение: **Повече информация** → **Изпълни въпреки това**. При първото стартиране избери своя език.

<img src="../screenshots/language-select.png" alt="29 езика" width="100%">

📸 **29 езика.** Програмата говори 29 езика. Сменяш езика с `TAB` на главния екран.

<br>

### 3️⃣ Избери държава

Въведи код на държава и натисни **Enter**, например `pl`, `de` или `us`. Доставчика сменяш със стрелките или с номер от `1` до `19`.

<br>

### 4️⃣ Избери сървър

Въведи името на сървъра от списъка или само началото му, например `pl1273`, и натисни **Enter**.

<img src="../screenshots/server-ping.png" alt="Списък със сървъри с пинг" width="100%">

📸 **Списък със сървъри.** До всеки сървър в скоби е пингът, т.е. времето за отговор: колкото по-малко `ms`, толкова по-бързо. `udp` обикновено е по-бърз, `tcp` по-лесно минава през блокировки. Най-долу въвеждаш избрания сървър.

<br>

### 5️⃣ Въведи данни за вход (само първия път)

Скриптът ще поиска потребителско име и парола за OpenVPN и ще ти каже къде да ги намериш. NordVPN и Surfshark използват отделни *Service credentials*, а не имейла и паролата на акаунта.

<img src="../screenshots/login.png" alt="Първо влизане" width="100%">

📸 **Първо влизане.** Скриптът показва за кой доставчик са данните и откъде да ги вземеш. Паролата е скрита със звездички. Данните се записват веднъж и следващия път не трябва да ги въвеждаш.

<br>

### 6️⃣ Готово

<img src="../screenshots/connected.png" alt="Екран на връзката" width="100%">

📸 **Свързан.** `NODE_IP` е новият ти IP адрес, който сайтовете виждат. `PING` е скоростта на тунела, `ENCRYPTION` е шифърът, а `KILL_SWITCH` показва дали интернетът извън VPN е блокиран. `LOCATION` и `PROVIDER` са градът и фирмата на сървъра. Долу: `1` тест на скоростта, `2` прекъсни, `3` kill switch.

<br>

---

## ⌨️ Команди

| Въведи | Какво прави |
|---|---|
| `pl`, `de`, `us`… | сървъри в тази държава |
| `1` … `19` | смяна на VPN доставчик |
| `TAB` | смяна на езика |
| `ks` | kill switch включен или изключен |
| `fs` | цял екран или прозорец |
| `Alt+C` | прекъсни VPN (работи навсякъде) |
| `1` / `2` / `3` при свързване | тест на скоростта / прекъсни / kill switch |

<br>

---

## 🌍 Доставчици

`NordVPN` (в списъка като **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET не продава VPN: използваш собствения си акаунт. Сървърните файлове добавяш в GhostVPN.

<br>

---

## 🆘 Нещо не работи?

| Какво виждам | Какво да направя |
|---|---|
| **OpenVPN**: не е инсталиран | Инсталирай [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) или [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: няма сървърни файлове | Добави сървърите на този доставчик в GhostVPN или избери друг доставчик. |
| **AUTH_FAILED** | Избери `1`, за да опиташ следващия сървър. Ако никой не работи, избери `2` и въведи данните отново. |
| **TUNNEL FAILED** | Прочети отчета в Notepad. Избери друг сървър. |
| Няма интернет след затваряне на прозореца | Стартирай скрипта и избери **ПРЕМАХНИ БЛОКИРОВКАТА** или въведи `ks`. |

> 🔒 Данните за вход остават само на твоя компютър, в папката до скрипта. Не давай тази папка на никого.

<br>

---

## 📜 Лиценз

### Само за лична домашна употреба. GHOST-NET принадлежи изцяло на автора, MRGREGOR85.

**Забранено е** да го продаваш, да го даваш или изпращаш на други, да го качваш на други сайтове, форуми или Discord, да го използваш във фирма, да го променяш или да копираш кода му. Всеки изтегля собствено копие от тази страница. Пълен текст: [LICENSE](../LICENSE).

<br>

---

## 🎬 YouTube

<a href="https://youtu.be/Fb_61rHk95Y"><img src="../docs/images/video.jpg" alt="Пълно видео ръководство в YouTube" width="480"></a>

<br>

---

## 👨‍💻 Автор

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Ако GHOST-NET ти помага, остави ⭐

</div>
