<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN CMD:stä: valitse maa, kirjoita palvelin ja olet yhdistetty. 19 VPN-palveluntarjoajaa, kill switch ja nopeustesti.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Lataa GHOST-NET" width="380"></a>

**Windows 10 ja 11 · toimii GhostVPN:n kanssa**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="GHOST-NETin päänäkymä" width="100%">

📸 **Päänäkymä.** Ylhäällä: maat, joissa palveluntarjoajallasi on palvelimia. Niiden alla: kirjoitettavat maakoodit, esimerkiksi `pl` = Puola. Alempana: kill switchin tila ja 19 VPN-palveluntarjoajaa, korostettu on käytössä oleva. Aivan alhaalla kirjoitat maakoodin.

<br>

---

## 💀 Mikä GHOST-NET on?

VPN-hallinta tavallisessa CMD-ikkunassa. Se yhdistää sinut OpenVPN:n kautta oman VPN-palveluntarjoajasi palvelimeen, joten sivustot näkevät palvelimen IP:n eivätkä sinun. Se käyttää samoja palvelintiedostoja kuin [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Ohjelma puhuu 29 kieltä. Vaihda kieli painamalla `TAB` päänäkymässä.

<br>

---

## ✨ Ominaisuudet

| Ominaisuus | Mitä se tekee |
|---|---|
| **19 VPN-palveluntarjoajaa** | NordVPN, ProtonVPN, Surfshark, Mullvad ja muut. Vaihda nuolinäppäimillä tai numerolla. |
| **Reaaliaikainen ping** | Palvelinluettelo näyttää, mikä palvelin on nopein. |
| **Kill switch** | Windowsin palomuuri estää internetin VPN:n ulkopuolella. Jos tunneli katkeaa, IP-osoitteesi ei vuoda. Kotiverkko toimii edelleen. |
| **DNS-suojaus** | DNS-kyselyt eivät poistu tunnelista. |
| **Yhteysnäkymä** | Uusi IP, kaupunki, palveluntarjoaja, ping ja salaus. |
| **Nopeustesti** | Nopeustesti 1 Gt:n tiedostolla, tulos Mbit/s. |
| **Fiksut virheet** | Raportti Muistiossa, seuraavan palvelimen ehdotus ja uusien NordVPN-palvelimien automaattinen lataus. |
| **29 kieltä** | Ohjelma puhuu 29 kieltä. Vaihda kieli painamalla `TAB` päänäkymässä. |

<br>

---

## 📋 Mitä tarvitset

**Windows 10 tai 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (tai [OpenVPN](https://openvpn.net/community-downloads/)) · **tili VPN-palveluntarjoajalla** · **järjestelmänvalvojan oikeudet** (skripti pyytää ne itse)

<br>

---

## 📖 Ohje

<br>

### 1️⃣ Lataa

Napsauta **Lataa GHOST-NET**. Siirrä **GhostNet.exe** omaan kansioon, esimerkiksi `C:\GHOST-NET`, koska skripti tallentaa asetukset ja kirjautumistiedot viereensä.

<br>

### 2️⃣ Käynnistä

Kaksoisnapsauta **GhostNet.exe** ja valitse **Kyllä**, kun Windows kysyy lupaa. Jos Windows näyttää varoituksen: **Lisätietoja** → **Suorita silti**. Valitse kielesi ensimmäisellä käynnistyskerralla.

<img src="../screenshots/language-select.png" alt="29 kieltä" width="100%">

📸 **29 kieltä.** Ohjelma puhuu 29 kieltä. Vaihda kieli painamalla `TAB` päänäkymässä.

<br>

### 3️⃣ Valitse maa

Kirjoita maakoodi ja paina **Enter**, esimerkiksi `pl`, `de` tai `us`. Vaihda palveluntarjoajaa nuolinäppäimillä tai numerolla `1`–`19`.

<br>

### 4️⃣ Valitse palvelin

Kirjoita palvelimen nimi luettelosta tai vain sen alku, esimerkiksi `pl1273`, ja paina **Enter**.

<img src="../screenshots/server-ping.png" alt="Palvelinluettelo pingillä" width="100%">

📸 **Palvelinluettelo.** Jokaisen palvelimen ping eli vasteaika näkyy suluissa: mitä vähemmän `ms`, sitä nopeampi. `udp` on yleensä nopeampi, `tcp` pääsee helpommin estojen läpi. Alhaalla kirjoitat valitsemasi palvelimen.

<br>

### 5️⃣ Anna kirjautumistiedot (vain ensimmäisellä kerralla)

Skripti kysyy OpenVPN-käyttäjätunnusta ja salasanaa ja kertoo, mistä ne löytyvät. NordVPN ja Surfshark käyttävät erillisiä *Service credentials* -tunnuksia, eivät tilin sähköpostia ja salasanaa.

<img src="../screenshots/login.png" alt="Ensimmäinen kirjautuminen" width="100%">

📸 **Ensimmäinen kirjautuminen.** Skripti näyttää, minkä palveluntarjoajan tunnuksista on kyse ja mistä ne saa. Salasana piilotetaan tähdillä. Tunnukset tallennetaan kerran, eikä niitä tarvitse kirjoittaa uudelleen.

<br>

### 6️⃣ Valmis

<img src="../screenshots/connected.png" alt="Yhteysnäkymä" width="100%">

📸 **Yhdistetty.** `NODE_IP` on uusi IP-osoitteesi, jonka sivustot näkevät. `PING` on tunnelin nopeus, `ENCRYPTION` salaus ja `KILL_SWITCH` kertoo, onko internet VPN:n ulkopuolella estetty. `LOCATION` ja `PROVIDER` ovat palvelimen kaupunki ja yritys. Alhaalla: `1` nopeustesti, `2` katkaise, `3` kill switch.

<br>

---

## ⌨️ Komennot

| Kirjoita | Mitä se tekee |
|---|---|
| `pl`, `de`, `us`… | kyseisen maan palvelimet |
| `1` … `19` | vaihda VPN-palveluntarjoajaa |
| `TAB` | vaihda kieli |
| `ks` | kill switch päälle tai pois |
| `fs` | koko näyttö tai ikkuna |
| `Alt+C` | katkaise VPN (toimii kaikkialla) |
| `1` / `2` / `3` yhteyden aikana | nopeustesti / katkaise / kill switch |

<br>

---

## 🌍 Palveluntarjoajat

`NordVPN` (luettelossa nimellä **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET ei myy VPN:ää: käytät omaa tiliäsi. Palvelintiedostot lisäät GhostVPN:ssä.

<br>

---

## 🆘 Jokin ei toimi?

| Mitä näen | Mitä teen |
|---|---|
| **OpenVPN**: ei asennettu | Asenna [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) tai [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: ei palvelintiedostoja | Lisää palveluntarjoajan palvelimet GhostVPN:ssä tai valitse toinen palveluntarjoaja. |
| **AUTH_FAILED** | Valitse `1` kokeillaksesi seuraavaa palvelinta. Jos mikään ei toimi, valitse `2` ja anna tunnukset uudelleen. |
| **TUNNEL FAILED** | Lue raportti Muistiosta. Valitse toinen palvelin. |
| Ei internetiä ikkunan sulkemisen jälkeen | Käynnistä skripti ja valitse **POISTA ESTO** tai kirjoita `ks`. |

> 🔒 Kirjautumistiedot pysyvät vain tietokoneellasi, skriptin vieressä olevassa kansiossa. Älä anna tätä kansiota kenellekään.

<br>

---

## 📜 Lisenssi

### Vain yksityiseen kotikäyttöön. GHOST-NET kuuluu yksinomaan tekijälleen, MRGREGOR85.

**Kiellettyä** on myydä sitä, antaa tai lähettää sitä muille, ladata sitä muille sivustoille, foorumeille tai Discordiin, käyttää sitä yrityksessä, muuttaa sitä tai kopioida sen koodia. Jokainen lataa oman kopionsa tältä sivulta. Koko teksti: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Tekijä

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Jos GHOST-NET auttaa sinua, jätä ⭐

</div>
