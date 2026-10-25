<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN fra CMD: velg et land, skriv en server, og du er tilkoblet. 19 VPN-leverandører, kill switch og hastighetstest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Last ned GHOST-NET" width="380"></a>

**Windows 10 og 11 · fungerer med GhostVPN**

## [🇵🇱 Polski](../README_PL.md) &nbsp; [🇬🇧 English](../README.md) &nbsp; [🇩🇪 Deutsch](README_DE.md) &nbsp; [🇨🇿 Čeština](README_CS.md) &nbsp; [🇸🇰 Slovenčina](README_SK.md) &nbsp; [🇺🇦 Українська](README_UK.md) &nbsp; [🇷🇺 Русский](README_RU.md) &nbsp; [🇱🇹 Lietuvių](README_LT.md) &nbsp; [🇱🇻 Latviešu](README_LV.md) &nbsp; [🇪🇪 Eesti](README_ET.md) &nbsp; [🇪🇸 Español](README_ES.md) &nbsp; [🇫🇷 Français](README_FR.md) &nbsp; [🇮🇹 Italiano](README_IT.md) &nbsp; [🇵🇹 Português](README_PT.md) &nbsp; [🇳🇱 Nederlands](README_NL.md) &nbsp; [🇸🇪 Svenska](README_SV.md) &nbsp; [🇩🇰 Dansk](README_DA.md) &nbsp; [🇳🇴 Norsk](README_NO.md) &nbsp; [🇫🇮 Suomi](README_FI.md) &nbsp; [🇭🇺 Magyar](README_HU.md) &nbsp; [🇷🇴 Română](README_RO.md) &nbsp; [🇧🇬 Български](README_BG.md) &nbsp; [🇬🇷 Ελληνικά](README_EL.md) &nbsp; [🇭🇷 Hrvatski](README_HR.md) &nbsp; [🇷🇸 Српски](README_SR.md) &nbsp; [🇸🇮 Slovenščina](README_SL.md) &nbsp; [🇹🇷 Türkçe](README_TR.md) &nbsp; [🇻🇳 Tiếng Việt](README_VI.md) &nbsp; [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="GHOST-NET hovedskjerm" width="100%">

📸 **Hovedskjerm.** Øverst: landene der leverandøren din har servere. Under dem: landskodene du skriver, for eksempel `pl` = Polen. Lenger ned: kill switch-status og de 19 VPN-leverandørene, den uthevede er den som brukes. Helt nederst skriver du en landskode.

<br>

---

## 💀 Hva er GHOST-NET?

En VPN-behandler i et vanlig CMD-vindu. Den kobler deg via OpenVPN til en server hos din egen VPN-leverandør, slik at nettsider ser serverens IP i stedet for din. Den bruker de samme serverfilene som [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Programmet snakker 29 språk. Trykk `TAB` på hovedskjermen for å bytte språk.

<br>

---

## ✨ Funksjoner

| Funksjon | Hva den gjør |
|---|---|
| **19 VPN-leverandører** | NordVPN, ProtonVPN, Surfshark, Mullvad og flere. Bytt med piltastene eller et nummer. |
| **Live-ping** | Serverlisten viser hvilken server som er raskest. |
| **Kill switch** | Windows-brannmuren blokkerer internett utenfor VPN. Hvis tunnelen faller ut, lekker ikke IP-en din. Hjemmenettverket fungerer fortsatt. |
| **DNS-beskyttelse** | DNS-forespørsler forlater ikke tunnelen. |
| **Tilkoblingsskjerm** | Ny IP, by, leverandør, ping og kryptering. |
| **Hastighetstest** | Hastighetstest med en fil på 1 GB, resultat i Mbit/s. |
| **Smarte feil** | Rapport i Notisblokk, forslag til neste server og automatisk nedlasting av nye NordVPN-servere. |
| **29 språk** | Programmet snakker 29 språk. Trykk `TAB` på hovedskjermen for å bytte språk. |

<br>

---

## 📋 Hva du trenger

**Windows 10 eller 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (eller [OpenVPN](https://openvpn.net/community-downloads/)) · **en konto hos en VPN-leverandør** · **administratorrettigheter** (skriptet ber om dem selv)

<br>

---

## 📖 Veiledning

<br>

### 1️⃣ Last ned

Klikk på **Last ned GHOST-NET**. Flytt **GhostNet.exe** til en egen mappe, for eksempel `C:\GHOST-NET`, fordi skriptet lagrer innstillinger og pålogginger ved siden av seg selv.

<br>

### 2️⃣ Start

Dobbeltklikk på **GhostNet.exe** og klikk **Ja** når Windows ber om tillatelse. Hvis Windows viser en advarsel: **Mer informasjon** → **Kjør likevel**. Velg språket ditt ved første oppstart.

<img src="../screenshots/language-select.png" alt="29 språk" width="100%">

📸 **29 språk.** Programmet snakker 29 språk. Trykk `TAB` på hovedskjermen for å bytte språk.

<br>

### 3️⃣ Velg land

Skriv en landskode og trykk **Enter**, for eksempel `pl`, `de` eller `us`. Bytt leverandør med piltastene eller et nummer fra `1` til `19`.

<br>

### 4️⃣ Velg server

Skriv servernavnet fra listen, eller bare begynnelsen, for eksempel `pl1273`, og trykk **Enter**.

<img src="../screenshots/server-ping.png" alt="Serverliste med ping" width="100%">

📸 **Serverliste.** Hver server viser ping i hakeparentes, altså svartiden: jo færre `ms`, desto raskere. `udp` er vanligvis raskere, `tcp` kommer lettere forbi blokkeringer. Nederst skriver du serveren du vil ha.

<br>

### 5️⃣ Skriv inn pålogging (bare første gang)

Skriptet spør etter OpenVPN-brukernavn og passord og forteller hvor du finner dem. NordVPN og Surfshark bruker egne *Service credentials*, ikke e-post og passord til kontoen.

<img src="../screenshots/login.png" alt="Første pålogging" width="100%">

📸 **Første pålogging.** Skriptet viser hvilken leverandør påloggingen gjelder og hvor du finner den. Passordet skjules med stjerner. Påloggingen lagres én gang, så du slipper å skrive den igjen.

<br>

### 6️⃣ Ferdig

<img src="../screenshots/connected.png" alt="Tilkoblingsskjerm" width="100%">

📸 **Tilkoblet.** `NODE_IP` er din nye IP som nettsider ser. `PING` er tunnelens hastighet, `ENCRYPTION` krypteringen, og `KILL_SWITCH` viser om internett utenfor VPN er blokkert. `LOCATION` og `PROVIDER` er serverens by og selskap. Nederst: `1` hastighetstest, `2` koble fra, `3` kill switch.

<br>

---

## ⌨️ Kommandoer

| Skriv | Hva den gjør |
|---|---|
| `pl`, `de`, `us`… | servere i det landet |
| `1` … `19` | bytt VPN-leverandør |
| `TAB` | bytt språk |
| `ks` | kill switch på eller av |
| `fs` | fullskjerm eller vindu |
| `Alt+C` | koble fra VPN (fungerer overalt) |
| `1` / `2` / `3` når du er tilkoblet | hastighetstest / koble fra / kill switch |

<br>

---

## 🌍 Leverandører

`NordVPN` (i listen som **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET selger ikke VPN: du bruker din egen konto. Serverfiler legger du til i GhostVPN.

<br>

---

## 🆘 Virker noe ikke?

| Hva jeg ser | Hva jeg gjør |
|---|---|
| **OpenVPN**: ikke installert | Installer [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) eller [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: ingen serverfiler | Legg til leverandørens servere i GhostVPN, eller velg en annen leverandør. |
| **AUTH_FAILED** | Velg `1` for å prøve neste server. Hvis ingen fungerer, velg `2` og skriv inn påloggingen på nytt. |
| **TUNNEL FAILED** | Les rapporten i Notisblokk. Velg en annen server. |
| Ikke internett etter at vinduet er lukket | Start skriptet og velg **FJERN BLOKKERING**, eller skriv `ks`. |

> 🔒 Påloggingene blir bare på datamaskinen din, i mappen ved siden av skriptet. Ikke gi den mappen til noen.

<br>

---

## 📜 Lisens

### Kun til privat bruk hjemme. GHOST-NET tilhører utelukkende forfatteren, MRGREGOR85.

**Det er ikke tillatt** å selge det, gi eller sende det til andre, laste det opp på andre nettsider, forum eller Discord, bruke det i en bedrift, endre det eller kopiere koden. Alle laster ned sin egen kopi fra denne siden. Full tekst: [LICENSE](../LICENSE).

<br>

---

## 🎬 YouTube

<a href="https://youtu.be/Fb_61rHk95Y"><img src="../docs/images/video.jpg" alt="Komplett videoveiledning på YouTube" width="480"></a>

**▶ [Komplett videoveiledning på YouTube](https://youtu.be/Fb_61rHk95Y)** 🇵🇱

<br>

---

## 👨‍💻 Forfatter

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Hvis GHOST-NET hjelper deg, legg igjen en ⭐

</div>
