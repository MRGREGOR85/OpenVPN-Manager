<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN vanuit CMD: kies een land, typ een server en je bent verbonden. 19 VPN-aanbieders, kill switch en speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="GHOST-NET downloaden" width="380"></a>

**Windows 10 en 11 · werkt met GhostVPN**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · 🇳🇱 Nederlands · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Hoofdscherm van GHOST-NET" width="100%">

📸 **Hoofdscherm.** Bovenaan: de landen waar je aanbieder servers heeft. Daaronder: de landcodes om te typen, bijvoorbeeld `pl` = Polen. Verder naar beneden: de status van de kill switch en de 19 VPN-aanbieders, de gemarkeerde is de actieve. Helemaal onderaan typ je een landcode.

<br>

---

## 💀 Wat is GHOST-NET?

Een VPN-manager in een gewoon CMD-venster. Hij verbindt je via OpenVPN met een server van je eigen VPN-aanbieder, zodat websites het IP van de server zien in plaats van het jouwe. Hij gebruikt dezelfde serverbestanden als [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Het programma spreekt 29 talen. Druk op `TAB` op het hoofdscherm om de taal te wijzigen.

<br>

---

## ✨ Functies

| Functie | Wat het doet |
|---|---|
| **19 VPN-aanbieders** | NordVPN, ProtonVPN, Surfshark, Mullvad en meer. Wissel met de pijltjestoetsen of een nummer. |
| **Live ping** | De serverlijst laat zien welke server het snelst is. |
| **Kill switch** | Windows Firewall blokkeert internet buiten de VPN. Valt de tunnel weg, dan lekt je IP niet. Je thuisnetwerk blijft werken. |
| **DNS-bescherming** | DNS-verzoeken verlaten de tunnel niet. |
| **Verbindingsscherm** | Nieuw IP, stad, aanbieder, ping en versleuteling. |
| **Speedtest** | Snelheidstest met een bestand van 1 GB, resultaat in Mbit/s. |
| **Slimme foutmeldingen** | Rapport in Kladblok, de volgende server voorgesteld en nieuwe NordVPN-servers automatisch gedownload. |
| **29 talen** | Het programma spreekt 29 talen. Druk op `TAB` op het hoofdscherm om de taal te wijzigen. |

<br>

---

## 📋 Wat je nodig hebt

**Windows 10 of 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (of [OpenVPN](https://openvpn.net/community-downloads/)) · **een account bij een VPN-aanbieder** · **beheerdersrechten** (het script vraagt er zelf om)

<br>

---

## 📖 Handleiding

<br>

### 1️⃣ Downloaden

Klik op **GHOST-NET downloaden**. Zet **GhostNet.exe** in een eigen map, bijvoorbeeld `C:\GHOST-NET`, want het script slaat instellingen en logins naast zichzelf op.

<br>

### 2️⃣ Starten

Dubbelklik op **GhostNet.exe** en klik op **Ja** als Windows om toestemming vraagt. Geeft Windows een waarschuwing: **Meer informatie** → **Toch uitvoeren**. Kies bij de eerste start je taal.

<img src="../screenshots/language-select.png" alt="29 talen" width="100%">

📸 **29 talen.** Het programma spreekt 29 talen. Druk op `TAB` op het hoofdscherm om de taal te wijzigen.

<br>

### 3️⃣ Kies een land

Typ een landcode en druk op **Enter**, bijvoorbeeld `pl`, `de` of `us`. Wissel van aanbieder met de pijltjestoetsen of een nummer van `1` tot `19`.

<br>

### 4️⃣ Kies een server

Typ de servernaam uit de lijst, of alleen het begin, bijvoorbeeld `pl1273`, en druk op **Enter**.

<img src="../screenshots/server-ping.png" alt="Serverlijst met ping" width="100%">

📸 **Serverlijst.** Elke server toont tussen haakjes zijn ping, de reactietijd: hoe minder `ms`, hoe sneller. `udp` is meestal sneller, `tcp` komt makkelijker door blokkades. Onderaan typ je de gekozen server.

<br>

### 5️⃣ Voer je login in (alleen de eerste keer)

Het script vraagt om je OpenVPN-gebruikersnaam en wachtwoord en zegt waar je ze vindt. NordVPN en Surfshark gebruiken aparte *Service credentials*, niet het e-mailadres en wachtwoord van je account.

<img src="../screenshots/login.png" alt="Eerste login" width="100%">

📸 **Eerste login.** Het script laat zien voor welke aanbieder de login is en waar je hem vindt. Het wachtwoord wordt verborgen met sterretjes. De login wordt één keer opgeslagen, daarna hoef je hem niet opnieuw te typen.

<br>

### 6️⃣ Klaar

<img src="../screenshots/connected.png" alt="Verbindingsscherm" width="100%">

📸 **Verbonden.** `NODE_IP` is je nieuwe IP dat websites zien. `PING` is de snelheid van de tunnel, `ENCRYPTION` de versleuteling, en `KILL_SWITCH` laat zien of internet buiten de VPN geblokkeerd is. `LOCATION` en `PROVIDER` zijn de stad en het bedrijf van de server. Onderaan: `1` speedtest, `2` verbreken, `3` kill switch.

<br>

---

## ⌨️ Commando's

| Typ | Wat het doet |
|---|---|
| `pl`, `de`, `us`… | servers in dat land |
| `1` … `19` | VPN-aanbieder wisselen |
| `TAB` | taal wijzigen |
| `ks` | kill switch aan of uit |
| `fs` | volledig scherm of venster |
| `Alt+C` | VPN verbreken (werkt overal) |
| `1` / `2` / `3` als je verbonden bent | speedtest / verbreken / kill switch |

<br>

---

## 🌍 Aanbieders

`NordVPN` (in de lijst als **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET verkoopt geen VPN: je gebruikt je eigen account. Serverbestanden voeg je toe in GhostVPN.

<br>

---

## 🆘 Werkt er iets niet?

| Wat ik zie | Wat te doen |
|---|---|
| **OpenVPN**: niet geïnstalleerd | Installeer [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) of [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: geen serverbestanden | Voeg de servers van deze aanbieder toe in GhostVPN, of kies een andere aanbieder. |
| **AUTH_FAILED** | Kies `1` om de volgende server te proberen. Werkt er geen enkele, kies dan `2` en typ je login opnieuw. |
| **TUNNEL FAILED** | Lees het rapport in Kladblok. Kies een andere server. |
| Geen internet na het sluiten van het venster | Start het script en kies **BLOKKADE OPHEFFEN**, of typ `ks`. |

> 🔒 Logins blijven alleen op je computer, in de map naast het script. Geef die map aan niemand.

<br>

---

## 📜 Licentie

### Alleen voor privégebruik thuis. GHOST-NET is uitsluitend eigendom van de auteur, MRGREGOR85.

**Het is niet toegestaan** het te verkopen, aan anderen te geven of te sturen, op andere websites, fora of Discord te zetten, in een bedrijf te gebruiken, aan te passen of de code te kopiëren. Iedereen downloadt zijn eigen kopie van deze pagina. Volledige tekst: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Auteur

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Helpt GHOST-NET je, laat dan een ⭐ achter

</div>
