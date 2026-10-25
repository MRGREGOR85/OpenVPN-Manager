<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN из CMD-а: изабереш државу, упишеш сервер и повезан си. 19 VPN провајдера, kill switch и тест брзине.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Преузми GHOST-NET" width="380"></a>

**Windows 10 и 11 · ради са GhostVPN-ом**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · 🇷🇸 Српски · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Главни екран GHOST-NET-а" width="100%">

📸 **Главни екран.** Горе: државе у којима твој провајдер има сервере. Испод њих: кодови држава за упис, на пример `pl` = Пољска. Ниже: стање kill switch-а и 19 VPN провајдера, истакнути је онај који користиш. Скроз доле уписујеш код државе.

<br>

---

## 💀 Шта је GHOST-NET?

VPN менаџер у обичном CMD прозору. Преко OpenVPN-а те повезује са сервером твог сопственог VPN провајдера, па сајтови виде IP сервера уместо твог. Користи исте фајлове сервера као [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Програм говори 29 језика. Језик мењаш тастером `TAB` на главном екрану.

<br>

---

## ✨ Функције

| Функција | Шта ради |
|---|---|
| **19 VPN провајдера** | NordVPN, ProtonVPN, Surfshark, Mullvad и други. Мењаш стрелицама или бројем. |
| **Пинг уживо** | Листа сервера показује који је најбржи. |
| **Kill switch** | Windows заштитни зид блокира интернет ван VPN-а. Ако тунел падне, твој IP не цури. Кућна мрежа и даље ради. |
| **DNS заштита** | DNS упити не излазе из тунела. |
| **Екран везе** | Нови IP, град, провајдер, пинг и шифра. |
| **Тест брзине** | Тест брзине са фајлом од 1 GB, резултат у Mbit/s. |
| **Паметне грешке** | Извештај у Notepad-у, предлог следећег сервера и аутоматско преузимање нових NordVPN сервера. |
| **29 језика** | Програм говори 29 језика. Језик мењаш тастером `TAB` на главном екрану. |

<br>

---

## 📋 Шта ти треба

**Windows 10 или 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (или [OpenVPN](https://openvpn.net/community-downloads/)) · **налог код VPN провајдера** · **администраторска права** (скрипта их сама тражи)

<br>

---

## 📖 Упутство

<br>

### 1️⃣ Преузми

Кликни **Преузми GHOST-NET**. Премести **GhostNet.exe** у засебну фасциклу, на пример `C:\GHOST-NET`, јер скрипта поред себе чува подешавања и пријаве.

<br>

### 2️⃣ Покрени

Двапут кликни **GhostNet.exe** и кликни **Да** када Windows затражи дозволу. Ако Windows прикаже упозорење: **Више информација** → **Ипак покрени**. При првом покретању изабери свој језик.

<img src="../screenshots/language-select.png" alt="29 језика" width="100%">

📸 **29 језика.** Програм говори 29 језика. Језик мењаш тастером `TAB` на главном екрану.

<br>

### 3️⃣ Изабери државу

Упиши код државе и притисни **Enter**, на пример `pl`, `de` или `us`. Провајдера мењаш стрелицама или бројем од `1` до `19`.

<br>

### 4️⃣ Изабери сервер

Упиши назив сервера са листе или само његов почетак, на пример `pl1273`, и притисни **Enter**.

<img src="../screenshots/server-ping.png" alt="Листа сервера са пингом" width="100%">

📸 **Листа сервера.** Поред сваког сервера у загради је пинг, односно време одзива: што мање `ms`, то брже. `udp` је обично бржи, `tcp` лакше пролази кроз блокаде. На дну уписујеш изабрани сервер.

<br>

### 5️⃣ Упиши пријаву (само први пут)

Скрипта ће тражити OpenVPN корисничко име и лозинку и рећи ти где да их нађеш. NordVPN и Surfshark користе засебне *Service credentials*, а не имејл и лозинку налога.

<br>

### 6️⃣ Готово

<img src="../screenshots/connected.png" alt="Екран везе" width="100%">

📸 **Повезано.** `NODE_IP` је твој нови IP који виде сајтови. `PING` је брзина тунела, `ENCRYPTION` шифра, а `KILL_SWITCH` показује да ли је интернет ван VPN-а блокиран. `LOCATION` и `PROVIDER` су град и фирма сервера. Доле: `1` тест брзине, `2` прекини везу, `3` kill switch.

<br>

---

## ⌨️ Команде

| Упиши | Шта ради |
|---|---|
| `pl`, `de`, `us`… | сервери у тој држави |
| `1` … `19` | промена VPN провајдера |
| `TAB` | промена језика |
| `ks` | kill switch укључен или искључен |
| `fs` | цео екран или прозор |
| `Alt+C` | прекини VPN (ради свуда) |
| `1` / `2` / `3` када си повезан | тест брзине / прекини везу / kill switch |

<br>

---

## 🌍 Провајдери

`NordVPN` (на листи као **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET не продаје VPN: користиш свој налог. Фајлове сервера додајеш у GhostVPN-у.

<br>

---

## 🆘 Нешто не ради?

| Шта видим | Шта да урадим |
|---|---|
| **OpenVPN**: није инсталиран | Инсталирај [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) или [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: нема фајлова сервера | Додај сервере тог провајдера у GhostVPN-у или изабери другог провајдера. |
| **AUTH_FAILED** | Изабери `1` за следећи сервер. Ако ниједан не ради, изабери `2` и поново упиши пријаву. |
| **TUNNEL FAILED** | Прочитај извештај у Notepad-у. Изабери други сервер. |
| Нема интернета после затварања прозора | Покрени скрипту и изабери **УКЛОНИ БЛОКАДУ** или упиши `ks`. |

> 🔒 Пријаве остају само на твом рачунару, у фасцикли поред скрипте. Никоме не дај ту фасциклу.

<br>

---

## 📜 Лиценца

### Само за приватну кућну употребу. GHOST-NET припада искључиво аутору, MRGREGOR85.

**Забрањено је** продавати га, давати или слати другима, постављати на друге сајтове, форуме или Discord, користити у фирми, мењати га или копирати његов код. Свако преузима сопствену копију са ове странице. Цео текст: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Аутор

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Ако ти GHOST-NET помаже, остави ⭐

</div>
