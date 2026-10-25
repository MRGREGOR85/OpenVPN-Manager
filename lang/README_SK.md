<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN z CMD: vyberieš krajinu, napíšeš server a si pripojený. 19 poskytovateľov VPN, kill switch a speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Stiahnuť GHOST-NET" width="380"></a>

**Windows 10 a 11 · funguje s GhostVPN**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · 🇸🇰 Slovenčina · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Hlavná obrazovka GHOST-NET" width="100%">

📸 **Hlavná obrazovka.** Hore: krajiny, kde má tvoj poskytovateľ servery. Pod nimi: kódy krajín na napísanie, napríklad `pl` = Poľsko. Nižšie: stav kill switchu a 19 poskytovateľov VPN, zvýraznený je ten, ktorý používaš. Úplne dole napíšeš kód krajiny.

<br>

---

## 💀 Čo je GHOST-NET?

Správca VPN v obyčajnom okne CMD. Pripojí ťa cez OpenVPN k serveru tvojho vlastného poskytovateľa VPN, takže weby vidia IP servera namiesto tvojej. Používa rovnaké súbory serverov ako [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Program hovorí 29 jazykmi. Jazyk zmeníš klávesom `TAB` na hlavnej obrazovke.

<br>

---

## ✨ Funkcie

| Funkcia | Čo robí |
|---|---|
| **19 poskytovateľov VPN** | NordVPN, ProtonVPN, Surfshark, Mullvad a ďalší. Prepínaš šípkami alebo číslom. |
| **Živý ping** | Zoznam serverov ukazuje, ktorý je najrýchlejší. |
| **Kill switch** | Brána firewall Windows blokuje internet mimo VPN. Keď tunel spadne, tvoja IP neunikne. Domáca sieť ďalej funguje. |
| **Ochrana DNS** | Dotazy DNS neopustia tunel. |
| **Obrazovka pripojenia** | Nová IP, mesto, poskytovateľ, ping a šifra. |
| **Speedtest** | Test rýchlosti na súbore 1 GB, výsledok v Mbit/s. |
| **Múdre chyby** | Správa v Poznámkovom bloku, návrh ďalšieho servera a automatické stiahnutie nových serverov NordVPN. |
| **29 jazykov** | Program hovorí 29 jazykmi. Jazyk zmeníš klávesom `TAB` na hlavnej obrazovke. |

<br>

---

## 📋 Čo potrebuješ

**Windows 10 alebo 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (alebo [OpenVPN](https://openvpn.net/community-downloads/)) · **účet u poskytovateľa VPN** · **práva správcu** (skript si o ne povie sám)

<br>

---

## 📖 Návod

<br>

### 1️⃣ Stiahni

Klikni na **Stiahnuť GHOST-NET**. Presuň **GhostNet.exe** do vlastného priečinka, napríklad `C:\GHOST-NET`, pretože skript si vedľa seba ukladá nastavenia a prihlásenia.

<br>

### 2️⃣ Spusti

Dvakrát klikni na **GhostNet.exe** a klikni na **Áno**, keď sa Windows opýta na povolenie. Ak Windows ukáže varovanie: **Ďalšie informácie** → **Spustiť aj tak**. Pri prvom spustení si vyber jazyk.

<img src="../screenshots/language-select.png" alt="29 jazykov" width="100%">

📸 **29 jazykov.** Program hovorí 29 jazykmi. Jazyk zmeníš klávesom `TAB` na hlavnej obrazovke.

<br>

### 3️⃣ Vyber krajinu

Napíš kód krajiny a stlač **Enter**, napríklad `pl`, `de` alebo `us`. Poskytovateľa zmeníš šípkami alebo číslom od `1` do `19`.

<br>

### 4️⃣ Vyber server

Napíš názov servera zo zoznamu alebo len jeho začiatok, napríklad `pl1273`, a stlač **Enter**.

<img src="../screenshots/server-ping.png" alt="Zoznam serverov s pingom" width="100%">

📸 **Zoznam serverov.** Každý server má v zátvorke ping, teda čas odozvy: čím menej `ms`, tým rýchlejší. `udp` býva rýchlejšie, `tcp` lepšie prejde blokovaním. Dole napíšeš vybraný server.

<br>

### 5️⃣ Zadaj prihlásenie (iba prvýkrát)

Skript sa opýta na používateľské meno a heslo k OpenVPN a poradí, kde ich nájdeš. NordVPN a Surfshark majú samostatné *Service credentials*, nie e-mail a heslo k účtu.

<br>

### 6️⃣ Hotovo

<img src="../screenshots/connected.png" alt="Obrazovka pripojenia" width="100%">

📸 **Pripojené.** `NODE_IP` je tvoja nová IP, ktorú vidia weby. `PING` je rýchlosť tunela, `ENCRYPTION` šifra a `KILL_SWITCH` hovorí, či je internet mimo VPN blokovaný. `LOCATION` a `PROVIDER` sú mesto a firma servera. Dole: `1` speedtest, `2` odpojiť, `3` kill switch.

<br>

---

## ⌨️ Príkazy

| Napíš | Čo robí |
|---|---|
| `pl`, `de`, `us`… | servery v tej krajine |
| `1` … `19` | zmena poskytovateľa VPN |
| `TAB` | zmena jazyka |
| `ks` | kill switch zapnúť alebo vypnúť |
| `fs` | celá obrazovka alebo okno |
| `Alt+C` | odpojiť VPN (funguje všade) |
| `1` / `2` / `3` po pripojení | speedtest / odpojiť / kill switch |

<br>

---

## 🌍 Poskytovatelia

`NordVPN` (v zozname ako **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET nepredáva VPN: používaš vlastný účet. Súbory serverov pridáš v GhostVPN.

<br>

---

## 🆘 Niečo nefunguje?

| Čo vidím | Čo robiť |
|---|---|
| **OpenVPN**: nie je nainštalovaný | Nainštaluj [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) alebo [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: žiadne súbory serverov | Pridaj servery tohto poskytovateľa v GhostVPN alebo vyber iného poskytovateľa. |
| **AUTH_FAILED** | Zvoľ `1` a skús ďalší server. Ak nefunguje žiadny, zvoľ `2` a zadaj prihlásenie znova. |
| **TUNNEL FAILED** | Prečítaj si správu v Poznámkovom bloku. Vyber iný server. |
| Žiadny internet po zatvorení okna | Spusti skript a zvoľ **ZRUŠIŤ BLOKOVANIE** alebo napíš `ks`. |

> 🔒 Prihlásenia zostávajú iba v tvojom počítači, v priečinku vedľa skriptu. Tento priečinok nikomu nedávaj.

<br>

---

## 📜 Licencia

### Iba na súkromné domáce použitie. GHOST-NET patrí výhradne autorovi, MRGREGOR85.

**Nie je dovolené** ho predávať, dávať alebo posielať iným, nahrávať na iné weby, fóra či Discord, používať vo firme, upravovať ho ani kopírovať jeho kód. Každý si stiahne vlastnú kópiu z tejto stránky. Plné znenie: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Autor

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Ak ti GHOST-NET pomáha, nechaj ⭐

</div>
