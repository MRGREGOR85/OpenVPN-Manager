<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN a CMD-ből: válassz országot, írd be a szervert, és már csatlakoztál is. 19 VPN-szolgáltató, kill switch és sebességteszt.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="GHOST-NET letöltése" width="380"></a>

**Windows 10 és 11 · a GhostVPN-nel működik**

## [🇵🇱 Polski](../README_PL.md) &nbsp; [🇬🇧 English](../README.md) &nbsp; [🇩🇪 Deutsch](README_DE.md) &nbsp; [🇨🇿 Čeština](README_CS.md) &nbsp; [🇸🇰 Slovenčina](README_SK.md) &nbsp; [🇺🇦 Українська](README_UK.md) &nbsp; [🇷🇺 Русский](README_RU.md) &nbsp; [🇱🇹 Lietuvių](README_LT.md) &nbsp; [🇱🇻 Latviešu](README_LV.md) &nbsp; [🇪🇪 Eesti](README_ET.md) &nbsp; [🇪🇸 Español](README_ES.md) &nbsp; [🇫🇷 Français](README_FR.md) &nbsp; [🇮🇹 Italiano](README_IT.md) &nbsp; [🇵🇹 Português](README_PT.md) &nbsp; [🇳🇱 Nederlands](README_NL.md) &nbsp; [🇸🇪 Svenska](README_SV.md) &nbsp; [🇩🇰 Dansk](README_DA.md) &nbsp; [🇳🇴 Norsk](README_NO.md) &nbsp; [🇫🇮 Suomi](README_FI.md) &nbsp; [🇭🇺 Magyar](README_HU.md) &nbsp; [🇷🇴 Română](README_RO.md) &nbsp; [🇧🇬 Български](README_BG.md) &nbsp; [🇬🇷 Ελληνικά](README_EL.md) &nbsp; [🇭🇷 Hrvatski](README_HR.md) &nbsp; [🇷🇸 Српски](README_SR.md) &nbsp; [🇸🇮 Slovenščina](README_SL.md) &nbsp; [🇹🇷 Türkçe](README_TR.md) &nbsp; [🇻🇳 Tiếng Việt](README_VI.md) &nbsp; [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="A GHOST-NET főképernyője" width="100%">

📸 **Főképernyő.** Fent: azok az országok, ahol a szolgáltatódnak szervere van. Alattuk: a beírandó országkódok, például `pl` = Lengyelország. Lejjebb: a kill switch állapota és a 19 VPN-szolgáltató, a kiemelt az éppen használt. Legalul írod be az országkódot.

<br>

---

## 💀 Mi az a GHOST-NET?

VPN-kezelő egy egyszerű CMD-ablakban. OpenVPN-en keresztül csatlakoztat a saját VPN-szolgáltatód szerveréhez, így a weboldalak a szerver IP-címét látják a tiéd helyett. Ugyanazokat a szerverfájlokat használja, mint a [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). A program 29 nyelven beszél. A nyelvet a főképernyőn a `TAB` billentyűvel váltod.

<br>

---

## ✨ Funkciók

| Funkció | Mit csinál |
|---|---|
| **19 VPN-szolgáltató** | NordVPN, ProtonVPN, Surfshark, Mullvad és mások. Váltás a nyilakkal vagy számmal. |
| **Élő ping** | A szerverlista megmutatja, melyik szerver a leggyorsabb. |
| **Kill switch** | A Windows tűzfal blokkolja az internetet a VPN-en kívül. Ha az alagút megszakad, az IP-címed nem szivárog ki. Az otthoni hálózat továbbra is működik. |
| **DNS-védelem** | A DNS-lekérdezések nem hagyják el az alagutat. |
| **Kapcsolati képernyő** | Új IP, város, szolgáltató, ping és titkosítás. |
| **Sebességteszt** | Sebességteszt egy 1 GB-os fájllal, eredmény Mbit/s-ban. |
| **Okos hibakezelés** | Jelentés a Jegyzettömbben, a következő szerver javaslata és az új NordVPN-szerverek automatikus letöltése. |
| **29 nyelv** | A program 29 nyelven beszél. A nyelvet a főképernyőn a `TAB` billentyűvel váltod. |

<br>

---

## 📋 Amire szükséged van

**Windows 10 vagy 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (vagy [OpenVPN](https://openvpn.net/community-downloads/)) · **fiók egy VPN-szolgáltatónál** · **rendszergazdai jogok** (a szkript maga kéri őket)

<br>

---

## 📖 Útmutató

<br>

### 1️⃣ Letöltés

Kattints a **GHOST-NET letöltése** gombra. Tedd a **GhostNet.exe** fájlt egy saját mappába, például `C:\GHOST-NET`, mert a szkript maga mellé menti a beállításokat és a bejelentkezéseket.

<br>

### 2️⃣ Indítás

Kattints duplán a **GhostNet.exe** fájlra, és kattints az **Igen** gombra, amikor a Windows engedélyt kér. Ha a Windows figyelmeztetést mutat: **További információ** → **Futtatás mindenképp**. Az első indításkor válaszd ki a nyelvedet.

<img src="../screenshots/language-select.png" alt="29 nyelv" width="100%">

📸 **29 nyelv.** A program 29 nyelven beszél. A nyelvet a főképernyőn a `TAB` billentyűvel váltod.

<br>

### 3️⃣ Válassz országot

Írj be egy országkódot, és nyomj **Entert**, például `pl`, `de` vagy `us`. A szolgáltatót a nyilakkal vagy `1` és `19` közötti számmal váltod.

<br>

### 4️⃣ Válassz szervert

Írd be a szerver nevét a listából, vagy csak az elejét, például `pl1273`, és nyomj **Entert**.

<img src="../screenshots/server-ping.png" alt="Szerverlista pinggel" width="100%">

📸 **Szerverlista.** Minden szerver mellett zárójelben a ping, vagyis a válaszidő látható: minél kevesebb `ms`, annál gyorsabb. Az `udp` általában gyorsabb, a `tcp` könnyebben átjut a blokkolásokon. Alul írod be a választott szervert.

<br>

### 5️⃣ Add meg a bejelentkezést (csak először)

A szkript elkéri az OpenVPN felhasználónevet és jelszót, és megmondja, hol találod őket. A NordVPN és a Surfshark külön *Service credentials* adatokat használ, nem a fiók e-mail-címét és jelszavát.

<img src="../screenshots/login.png" alt="Első bejelentkezés" width="100%">

📸 **Első bejelentkezés.** A szkript megmutatja, melyik szolgáltatóhoz kellenek az adatok, és honnan szerezheted be őket. A jelszót csillagok rejtik. A bejelentkezés egyszer mentődik, legközelebb nem kell újra beírni.

<br>

### 6️⃣ Kész

<img src="../screenshots/connected.png" alt="Kapcsolati képernyő" width="100%">

📸 **Csatlakozva.** A `NODE_IP` az új IP-címed, amit a weboldalak látnak. A `PING` az alagút sebessége, az `ENCRYPTION` a titkosítás, a `KILL_SWITCH` pedig megmutatja, hogy blokkolva van-e az internet a VPN-en kívül. A `LOCATION` és a `PROVIDER` a szerver városa és cége. Alul: `1` sebességteszt, `2` bontás, `3` kill switch.

<br>

---

## ⌨️ Parancsok

| Írd be | Mit csinál |
|---|---|
| `pl`, `de`, `us`… | szerverek abban az országban |
| `1` … `19` | VPN-szolgáltató váltása |
| `TAB` | nyelv váltása |
| `ks` | kill switch be vagy ki |
| `fs` | teljes képernyő vagy ablak |
| `Alt+C` | VPN bontása (mindenhol működik) |
| `1` / `2` / `3` csatlakozás után | sebességteszt / bontás / kill switch |

<br>

---

## 🌍 Szolgáltatók

`NordVPN` (a listában így: **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

A GHOST-NET nem árul VPN-t: a saját fiókodat használod. A szerverfájlokat a GhostVPN-ben adod hozzá.

<br>

---

## 🆘 Valami nem működik?

| Amit látok | Mit tegyek |
|---|---|
| **OpenVPN**: nincs telepítve | Telepítsd a [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)-t vagy az [OpenVPN](https://openvpn.net/community-downloads/)-t. |
| **.ovpn**: nincsenek szerverfájlok | Add hozzá a szolgáltató szervereit a GhostVPN-ben, vagy válassz másik szolgáltatót. |
| **AUTH_FAILED** | Válaszd az `1`-et a következő szerver kipróbálásához. Ha egyik sem működik, válaszd a `2`-t, és add meg újra a bejelentkezést. |
| **TUNNEL FAILED** | Olvasd el a jelentést a Jegyzettömbben. Válassz másik szervert. |
| Nincs internet az ablak bezárása után | Indítsd el a szkriptet, és válaszd a **BLOKKOLÁS FELOLDÁSA** lehetőséget, vagy írd be: `ks`. |

> 🔒 A bejelentkezések csak a gépeden maradnak, a szkript melletti mappában. Ezt a mappát senkinek ne add oda.

<br>

---

## 📜 Licenc

### Csak otthoni magánhasználatra. A GHOST-NET kizárólag a szerzőé, MRGREGOR85-é.

**Tilos** eladni, másoknak odaadni vagy elküldeni, más weboldalakra, fórumokra vagy Discordra feltölteni, cégnél használni, módosítani vagy a kódját másolni. Mindenki a saját példányát tölti le erről az oldalról. Teljes szöveg: [LICENSE](../LICENSE).

<br>

---

## 🎬 YouTube

<a href="https://youtu.be/Fb_61rHk95Y"><img src="../docs/images/video.jpg" alt="Teljes videós útmutató a YouTube-on" width="100%"></a>

<br>

---

## 👨‍💻 Szerző

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Ha a GHOST-NET segít, hagyj egy ⭐-t

</div>
