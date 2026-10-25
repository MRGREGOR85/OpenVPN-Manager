<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN CMD-st: vali riik, sisesta server ja oledki ühendatud. 19 VPN-teenusepakkujat, kill switch ja kiirustest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Laadi GHOST-NET alla" width="380"></a>

**Windows 10 ja 11 · töötab koos GhostVPN-iga**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · 🇪🇪 Eesti · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="GHOST-NET-i põhiekraan" width="100%">

📸 **Põhiekraan.** Üleval: riigid, kus sinu teenusepakkujal on servereid. Nende all: sisestatavad riigikoodid, näiteks `pl` = Poola. Allpool: kill switchi olek ja 19 VPN-teenusepakkujat, esiletõstetud on kasutusel olev. Päris all sisestad riigikoodi.

<br>

---

## 💀 Mis on GHOST-NET?

VPN-haldur tavalises CMD-aknas. See ühendab sind OpenVPN-i kaudu sinu enda VPN-teenusepakkuja serveriga, nii et veebilehed näevad serveri IP-d, mitte sinu oma. Kasutab samu serverifaile mis [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Programm räägib 29 keelt. Keelt vahetad põhiekraanil klahviga `TAB`.

<br>

---

## ✨ Funktsioonid

| Funktsioon | Mida teeb |
|---|---|
| **19 VPN-teenusepakkujat** | NordVPN, ProtonVPN, Surfshark, Mullvad ja teised. Vaheta nooleklahvide või numbriga. |
| **Reaalajas ping** | Serverite nimekiri näitab, milline on kiireim. |
| **Kill switch** | Windowsi tulemüür blokeerib interneti väljaspool VPN-i. Kui tunnel katkeb, sinu IP ei leki. Koduvõrk töötab edasi. |
| **DNS-kaitse** | DNS-päringud ei lahku tunnelist. |
| **Ühenduse ekraan** | Uus IP, linn, teenusepakkuja, ping ja šiffer. |
| **Kiirustest** | Kiiruse test 1 GB failiga, tulemus Mbit/s. |
| **Nutikad vead** | Raport Notepadis, järgmise serveri soovitus ja uute NordVPN-i serverite automaatne allalaadimine. |
| **29 keelt** | Programm räägib 29 keelt. Keelt vahetad põhiekraanil klahviga `TAB`. |

<br>

---

## 📋 Mida sul vaja on

**Windows 10 või 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (või [OpenVPN](https://openvpn.net/community-downloads/)) · **VPN-teenusepakkuja konto** · **administraatori õigused** (skript küsib neid ise)

<br>

---

## 📖 Juhend

<br>

### 1️⃣ Laadi alla

Klõpsa **Laadi GHOST-NET alla**. Tõsta **GhostNet.exe** eraldi kausta, näiteks `C:\GHOST-NET`, sest skript salvestab seaded ja sisselogimised enda kõrvale.

<br>

### 2️⃣ Käivita

Topeltklõpsa **GhostNet.exe** ja klõpsa **Jah**, kui Windows küsib luba. Kui Windows näitab hoiatust: **Lisateave** → **Käivita ikkagi**. Esimesel käivitamisel vali oma keel.

<img src="../screenshots/language-select.png" alt="29 keelt" width="100%">

📸 **29 keelt.** Programm räägib 29 keelt. Keelt vahetad põhiekraanil klahviga `TAB`.

<br>

### 3️⃣ Vali riik

Sisesta riigikood ja vajuta **Enter**, näiteks `pl`, `de` või `us`. Teenusepakkujat vahetad nooleklahvide või numbriga `1`–`19`.

<br>

### 4️⃣ Vali server

Sisesta serveri nimi nimekirjast või ainult selle algus, näiteks `pl1273`, ja vajuta **Enter**.

<img src="../screenshots/server-ping.png" alt="Serverite nimekiri koos pingiga" width="100%">

📸 **Serverite nimekiri.** Iga serveri juures on sulgudes ping ehk vastamisaeg: mida vähem `ms`, seda kiirem. `udp` on tavaliselt kiirem, `tcp` pääseb blokeeringutest kergemini läbi. All sisestad valitud serveri.

<br>

### 5️⃣ Sisesta sisselogimine (ainult esimesel korral)

Skript küsib OpenVPN-i kasutajanime ja parooli ning ütleb, kust need leida. NordVPN ja Surfshark kasutavad eraldi *Service credentials*, mitte konto e-posti ja parooli.

<br>

### 6️⃣ Valmis

<img src="../screenshots/connected.png" alt="Ühenduse ekraan" width="100%">

📸 **Ühendatud.** `NODE_IP` on sinu uus IP, mida veebilehed näevad. `PING` on tunneli kiirus, `ENCRYPTION` šiffer ja `KILL_SWITCH` näitab, kas internet väljaspool VPN-i on blokeeritud. `LOCATION` ja `PROVIDER` on serveri linn ja ettevõte. All: `1` kiirustest, `2` katkesta, `3` kill switch.

<br>

---

## ⌨️ Käsud

| Sisesta | Mida teeb |
|---|---|
| `pl`, `de`, `us`… | selle riigi serverid |
| `1` … `19` | VPN-teenusepakkuja vahetamine |
| `TAB` | keele vahetamine |
| `ks` | kill switch sisse või välja |
| `fs` | täisekraan või aken |
| `Alt+C` | VPN-i katkestamine (töötab kõikjal) |
| `1` / `2` / `3` ühenduse ajal | kiirustest / katkesta / kill switch |

<br>

---

## 🌍 Teenusepakkujad

`NordVPN` (nimekirjas nimega **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET ei müü VPN-i: kasutad oma kontot. Serverifailid lisad GhostVPN-is.

<br>

---

## 🆘 Midagi ei tööta?

| Mida näen | Mida teha |
|---|---|
| **OpenVPN**: pole paigaldatud | Paigalda [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) või [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: serverifaile pole | Lisa selle teenusepakkuja serverid GhostVPN-is või vali teine teenusepakkuja. |
| **AUTH_FAILED** | Vali `1`, et proovida järgmist serverit. Kui ükski ei tööta, vali `2` ja sisesta andmed uuesti. |
| **TUNNEL FAILED** | Loe raportit Notepadis. Vali teine server. |
| Pärast akna sulgemist pole internetti | Käivita skript ja vali **EEMALDA BLOKEERING** või sisesta `ks`. |

> 🔒 Sisselogimised jäävad ainult sinu arvutisse, skripti kõrval olevasse kausta. Ära anna seda kausta kellelegi.

<br>

---

## 📜 Litsents

### Ainult isiklikuks kasutamiseks kodus. GHOST-NET kuulub ainult autorile MRGREGOR85.

**Keelatud** on seda müüa, teistele anda või saata, teistele veebilehtedele, foorumitesse või Discordi üles laadida, ettevõttes kasutada, muuta või selle koodi kopeerida. Igaüks laadib oma koopia sellelt lehelt. Täistekst: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Autor

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Kui GHOST-NET sind aitab, jäta ⭐

</div>
