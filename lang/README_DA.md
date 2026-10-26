<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN fra CMD: vælg et land, skriv en server, og du er forbundet. 19 VPN-udbydere, kill switch og hastighedstest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Download GHOST-NET" width="380"></a>

**Windows 10 og 11 · virker med GhostVPN**

## [🇵🇱 Polski](../README_PL.md) &nbsp; [🇬🇧 English](../README.md) &nbsp; [🇩🇪 Deutsch](README_DE.md) &nbsp; [🇨🇿 Čeština](README_CS.md) &nbsp; [🇸🇰 Slovenčina](README_SK.md) &nbsp; [🇺🇦 Українська](README_UK.md) &nbsp; [🇷🇺 Русский](README_RU.md) &nbsp; [🇱🇹 Lietuvių](README_LT.md) &nbsp; [🇱🇻 Latviešu](README_LV.md) &nbsp; [🇪🇪 Eesti](README_ET.md) &nbsp; [🇪🇸 Español](README_ES.md) &nbsp; [🇫🇷 Français](README_FR.md) &nbsp; [🇮🇹 Italiano](README_IT.md) &nbsp; [🇵🇹 Português](README_PT.md) &nbsp; [🇳🇱 Nederlands](README_NL.md) &nbsp; [🇸🇪 Svenska](README_SV.md) &nbsp; [🇩🇰 Dansk](README_DA.md) &nbsp; [🇳🇴 Norsk](README_NO.md) &nbsp; [🇫🇮 Suomi](README_FI.md) &nbsp; [🇭🇺 Magyar](README_HU.md) &nbsp; [🇷🇴 Română](README_RO.md) &nbsp; [🇧🇬 Български](README_BG.md) &nbsp; [🇬🇷 Ελληνικά](README_EL.md) &nbsp; [🇭🇷 Hrvatski](README_HR.md) &nbsp; [🇷🇸 Српски](README_SR.md) &nbsp; [🇸🇮 Slovenščina](README_SL.md) &nbsp; [🇹🇷 Türkçe](README_TR.md) &nbsp; [🇻🇳 Tiếng Việt](README_VI.md) &nbsp; [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="GHOST-NET's hovedskærm" width="100%">

📸 **Hovedskærm.** Øverst: de lande, hvor din udbyder har servere. Under dem: landekoderne, du skal skrive, for eksempel `pl` = Polen. Længere nede: kill switchens status og de 19 VPN-udbydere, den markerede er den, der bruges. Nederst skriver du en landekode.

<br>

---

## 💀 Hvad er GHOST-NET?

En VPN-styring i et almindeligt CMD-vindue. Den forbinder dig via OpenVPN til en server hos din egen VPN-udbyder, så hjemmesider ser serverens IP i stedet for din. Den bruger de samme serverfiler som [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Programmet taler 29 sprog. Tryk `TAB` på hovedskærmen for at skifte sprog.

<br>

---

## ✨ Funktioner

| Funktion | Hvad den gør |
|---|---|
| **19 VPN-udbydere** | NordVPN, ProtonVPN, Surfshark, Mullvad og flere. Skift med piletasterne eller et nummer. |
| **Live-ping** | Serverlisten viser, hvilken server der er hurtigst. |
| **Kill switch** | Windows Firewall blokerer internettet uden for VPN. Hvis tunnelen falder ud, lækker din IP ikke. Hjemmenetværket virker stadig. |
| **DNS-beskyttelse** | DNS-forespørgsler forlader ikke tunnelen. |
| **Forbindelsesskærm** | Ny IP, by, udbyder, ping og kryptering. |
| **Hastighedstest** | Hastighedstest med en fil på 1 GB, resultat i Mbit/s. |
| **Smarte fejl** | Rapport i Notesblok, forslag til næste server og automatisk download af nye NordVPN-servere. |
| **29 sprog** | Programmet taler 29 sprog. Tryk `TAB` på hovedskærmen for at skifte sprog. |

<br>

---

## 📋 Hvad du skal bruge

**Windows 10 eller 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (eller [OpenVPN](https://openvpn.net/community-downloads/)) · **en konto hos en VPN-udbyder** · **administratorrettigheder** (scriptet beder selv om dem)

<br>

---

## 📖 Vejledning

<br>

### 1️⃣ Download

Klik på **Download GHOST-NET**. Flyt **GhostNet.exe** til sin egen mappe, for eksempel `C:\GHOST-NET`, fordi scriptet gemmer indstillinger og logins ved siden af sig selv.

<br>

### 2️⃣ Start

Dobbeltklik på **GhostNet.exe**, og klik på **Ja**, når Windows beder om tilladelse. Hvis Windows viser en advarsel: **Flere oplysninger** → **Kør alligevel**. Vælg dit sprog ved første start.

<img src="../screenshots/language-select.png" alt="29 sprog" width="100%">

📸 **29 sprog.** Programmet taler 29 sprog. Tryk `TAB` på hovedskærmen for at skifte sprog.

<br>

### 3️⃣ Vælg land

Skriv en landekode, og tryk på **Enter**, for eksempel `pl`, `de` eller `us`. Skift udbyder med piletasterne eller et nummer fra `1` til `19`.

<br>

### 4️⃣ Vælg server

Skriv servernavnet fra listen, eller bare begyndelsen, for eksempel `pl1273`, og tryk på **Enter**.

<img src="../screenshots/server-ping.png" alt="Serverliste med ping" width="100%">

📸 **Serverliste.** Hver server viser sin ping i parentes, svartiden: jo færre `ms`, jo hurtigere. `udp` er som regel hurtigere, `tcp` kommer lettere forbi blokeringer. Nederst skriver du den valgte server.

<br>

### 5️⃣ Indtast login (kun første gang)

Scriptet spørger efter dit OpenVPN-brugernavn og din adgangskode og fortæller, hvor du finder dem. NordVPN og Surfshark bruger separate *Service credentials*, ikke kontoens e-mail og adgangskode.

<img src="../screenshots/login.png" alt="Første login" width="100%">

📸 **Første login.** Scriptet viser, hvilken udbyder loginnet gælder, og hvor du finder det. Adgangskoden skjules med stjerner. Loginnet gemmes én gang, så du ikke skal skrive det igen.

<br>

### 6️⃣ Færdig

<img src="../screenshots/connected.png" alt="Forbindelsesskærm" width="100%">

📸 **Forbundet.** `NODE_IP` er din nye IP, som hjemmesider ser. `PING` er tunnelens hastighed, `ENCRYPTION` krypteringen, og `KILL_SWITCH` viser, om internettet uden for VPN er blokeret. `LOCATION` og `PROVIDER` er serverens by og firma. Nederst: `1` hastighedstest, `2` afbryd, `3` kill switch.

<br>

---

## ⌨️ Kommandoer

| Skriv | Hvad den gør |
|---|---|
| `pl`, `de`, `us`… | servere i det land |
| `1` … `19` | skift VPN-udbyder |
| `TAB` | skift sprog |
| `ks` | kill switch til eller fra |
| `fs` | fuld skærm eller vindue |
| `Alt+C` | afbryd VPN (virker overalt) |
| `1` / `2` / `3` når du er forbundet | hastighedstest / afbryd / kill switch |

<br>

---

## 🌍 Udbydere

`NordVPN` (på listen som **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET sælger ikke VPN: du bruger din egen konto. Serverfiler tilføjer du i GhostVPN.

<br>

---

## 🆘 Virker noget ikke?

| Hvad jeg ser | Hvad jeg gør |
|---|---|
| **OpenVPN**: ikke installeret | Installer [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) eller [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: ingen serverfiler | Tilføj udbyderens servere i GhostVPN, eller vælg en anden udbyder. |
| **AUTH_FAILED** | Vælg `1` for at prøve den næste server. Hvis ingen virker, så vælg `2` og skriv dit login igen. |
| **TUNNEL FAILED** | Læs rapporten i Notesblok. Vælg en anden server. |
| Intet internet efter vinduet er lukket | Start scriptet og vælg **FJERN BLOKERING**, eller skriv `ks`. |

> 🔒 Logins bliver kun på din computer, i mappen ved siden af scriptet. Giv ikke den mappe til nogen.

<br>

---

## 📜 Licens

### Kun til privat brug i hjemmet. GHOST-NET tilhører udelukkende forfatteren, MRGREGOR85.

**Det er ikke tilladt** at sælge det, give eller sende det til andre, uploade det til andre hjemmesider, fora eller Discord, bruge det i en virksomhed, ændre det eller kopiere koden. Alle downloader deres egen kopi fra denne side. Fuld tekst: [LICENSE](../LICENSE).

<br>

---

## 🎬 YouTube

<a href="https://youtu.be/Fb_61rHk95Y"><img src="../docs/images/video.jpg" alt="Komplet videovejledning på YouTube" width="480"></a>

<br>

---

## 👨‍💻 Forfatter

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Hvis GHOST-NET hjælper dig, så giv en ⭐

</div>
