<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN iz CMD-a: odabereš državu, upišeš poslužitelj i spojen si. 19 VPN pružatelja, kill switch i test brzine.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Preuzmi GHOST-NET" width="380"></a>

**Windows 10 i 11 · radi s GhostVPN-om**

## [🇵🇱 Polski](../README_PL.md) &nbsp; [🇬🇧 English](../README.md) &nbsp; [🇩🇪 Deutsch](README_DE.md) &nbsp; [🇨🇿 Čeština](README_CS.md) &nbsp; [🇸🇰 Slovenčina](README_SK.md) &nbsp; [🇺🇦 Українська](README_UK.md) &nbsp; [🇷🇺 Русский](README_RU.md) &nbsp; [🇱🇹 Lietuvių](README_LT.md) &nbsp; [🇱🇻 Latviešu](README_LV.md) &nbsp; [🇪🇪 Eesti](README_ET.md) &nbsp; [🇪🇸 Español](README_ES.md) &nbsp; [🇫🇷 Français](README_FR.md) &nbsp; [🇮🇹 Italiano](README_IT.md) &nbsp; [🇵🇹 Português](README_PT.md) &nbsp; [🇳🇱 Nederlands](README_NL.md) &nbsp; [🇸🇪 Svenska](README_SV.md) &nbsp; [🇩🇰 Dansk](README_DA.md) &nbsp; [🇳🇴 Norsk](README_NO.md) &nbsp; [🇫🇮 Suomi](README_FI.md) &nbsp; [🇭🇺 Magyar](README_HU.md) &nbsp; [🇷🇴 Română](README_RO.md) &nbsp; [🇧🇬 Български](README_BG.md) &nbsp; [🇬🇷 Ελληνικά](README_EL.md) &nbsp; [🇭🇷 Hrvatski](README_HR.md) &nbsp; [🇷🇸 Српски](README_SR.md) &nbsp; [🇸🇮 Slovenščina](README_SL.md) &nbsp; [🇹🇷 Türkçe](README_TR.md) &nbsp; [🇻🇳 Tiếng Việt](README_VI.md) &nbsp; [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Glavni zaslon GHOST-NET-a" width="100%">

📸 **Glavni zaslon.** Gore: države u kojima tvoj pružatelj ima poslužitelje. Ispod njih: kodovi država za upis, na primjer `pl` = Poljska. Niže: stanje kill switcha i 19 VPN pružatelja, istaknuti je onaj koji koristiš. Na samom dnu upisuješ kod države.

<br>

---

## 💀 Što je GHOST-NET?

VPN upravitelj u običnom CMD prozoru. Preko OpenVPN-a te spaja na poslužitelj tvog vlastitog VPN pružatelja, pa stranice vide IP poslužitelja umjesto tvog. Koristi iste datoteke poslužitelja kao [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Program govori 29 jezika. Jezik mijenjaš tipkom `TAB` na glavnom zaslonu.

<br>

---

## ✨ Značajke

| Značajka | Što radi |
|---|---|
| **19 VPN pružatelja** | NordVPN, ProtonVPN, Surfshark, Mullvad i drugi. Mijenjaš strelicama ili brojem. |
| **Ping uživo** | Popis poslužitelja pokazuje koji je najbrži. |
| **Kill switch** | Vatrozid Windowsa blokira internet izvan VPN-a. Ako tunel padne, tvoj IP ne curi. Kućna mreža i dalje radi. |
| **DNS zaštita** | DNS upiti ne izlaze iz tunela. |
| **Zaslon veze** | Novi IP, grad, pružatelj, ping i šifra. |
| **Test brzine** | Test brzine s datotekom od 1 GB, rezultat u Mbit/s. |
| **Pametne greške** | Izvješće u Blok-notesu, prijedlog sljedećeg poslužitelja i automatsko preuzimanje novih NordVPN poslužitelja. |
| **29 jezika** | Program govori 29 jezika. Jezik mijenjaš tipkom `TAB` na glavnom zaslonu. |

<br>

---

## 📋 Što ti treba

**Windows 10 ili 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (ili [OpenVPN](https://openvpn.net/community-downloads/)) · **račun kod VPN pružatelja** · **administratorska prava** (skripta ih sama traži)

<br>

---

## 📖 Upute

<br>

### 1️⃣ Preuzmi

Klikni **Preuzmi GHOST-NET**. Premjesti **GhostNet.exe** u zasebnu mapu, na primjer `C:\GHOST-NET`, jer skripta pored sebe sprema postavke i prijave.

<br>

### 2️⃣ Pokreni

Dvaput klikni **GhostNet.exe** i klikni **Da** kad Windows zatraži dopuštenje. Ako Windows prikaže upozorenje: **Više informacija** → **Svejedno pokreni**. Pri prvom pokretanju odaberi svoj jezik.

<img src="../screenshots/language-select.png" alt="29 jezika" width="100%">

📸 **29 jezika.** Program govori 29 jezika. Jezik mijenjaš tipkom `TAB` na glavnom zaslonu.

<br>

### 3️⃣ Odaberi državu

Upiši kod države i pritisni **Enter**, na primjer `pl`, `de` ili `us`. Pružatelja mijenjaš strelicama ili brojem od `1` do `19`.

<br>

### 4️⃣ Odaberi poslužitelj

Upiši naziv poslužitelja s popisa ili samo njegov početak, na primjer `pl1273`, i pritisni **Enter**.

<img src="../screenshots/server-ping.png" alt="Popis poslužitelja s pingom" width="100%">

📸 **Popis poslužitelja.** Uz svaki poslužitelj u zagradi je ping, odnosno vrijeme odziva: što manje `ms`, to brže. `udp` je obično brži, `tcp` lakše prolazi kroz blokade. Na dnu upisuješ odabrani poslužitelj.

<br>

### 5️⃣ Upiši prijavu (samo prvi put)

Skripta će tražiti OpenVPN korisničko ime i lozinku i reći ti gdje ih naći. NordVPN i Surfshark koriste zasebne *Service credentials*, a ne e-poštu i lozinku računa.

<img src="../screenshots/login.png" alt="Prva prijava" width="100%">

📸 **Prva prijava.** Skripta pokazuje za kojeg su pružatelja podaci i gdje ih nabaviti. Lozinka je skrivena zvjezdicama. Prijava se sprema jednom i sljedeći put je ne moraš upisivati.

<br>

### 6️⃣ Gotovo

<img src="../screenshots/connected.png" alt="Zaslon veze" width="100%">

📸 **Spojeno.** `NODE_IP` je tvoj novi IP koji vide stranice. `PING` je brzina tunela, `ENCRYPTION` šifra, a `KILL_SWITCH` pokazuje je li internet izvan VPN-a blokiran. `LOCATION` i `PROVIDER` su grad i tvrtka poslužitelja. Dolje: `1` test brzine, `2` prekini vezu, `3` kill switch.

<br>

---

## ⌨️ Naredbe

| Upiši | Što radi |
|---|---|
| `pl`, `de`, `us`… | poslužitelji u toj državi |
| `1` … `19` | promjena VPN pružatelja |
| `TAB` | promjena jezika |
| `ks` | kill switch uključen ili isključen |
| `fs` | cijeli zaslon ili prozor |
| `Alt+C` | prekini VPN (radi svugdje) |
| `1` / `2` / `3` kad si spojen | test brzine / prekini vezu / kill switch |

<br>

---

## 🌍 Pružatelji

`NordVPN` (na popisu kao **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET ne prodaje VPN: koristiš vlastiti račun. Datoteke poslužitelja dodaješ u GhostVPN-u.

<br>

---

## 🆘 Nešto ne radi?

| Što vidim | Što učiniti |
|---|---|
| **OpenVPN**: nije instaliran | Instaliraj [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) ili [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: nema datoteka poslužitelja | Dodaj poslužitelje tog pružatelja u GhostVPN-u ili odaberi drugog pružatelja. |
| **AUTH_FAILED** | Odaberi `1` za sljedeći poslužitelj. Ako nijedan ne radi, odaberi `2` i ponovno upiši prijavu. |
| **TUNNEL FAILED** | Pročitaj izvješće u Blok-notesu. Odaberi drugi poslužitelj. |
| Nema interneta nakon zatvaranja prozora | Pokreni skriptu i odaberi **UKLONI BLOKADU** ili upiši `ks`. |

> 🔒 Prijave ostaju samo na tvom računalu, u mapi pored skripte. Nikome ne daj tu mapu.

<br>

---

## 📜 Licenca

### Samo za privatnu kućnu upotrebu. GHOST-NET pripada isključivo autoru, MRGREGOR85.

**Zabranjeno je** prodavati ga, davati ili slati drugima, postavljati na druge stranice, forume ili Discord, koristiti u tvrtki, mijenjati ga ili kopirati njegov kod. Svatko preuzima vlastitu kopiju s ove stranice. Puni tekst: [LICENSE](../LICENSE).

<br>

---

## 🎬 YouTube

<a href="https://youtu.be/Fb_61rHk95Y"><img src="../docs/images/video.jpg" alt="Potpune video upute na YouTubeu" width="480"></a>

<br>

---

## 👨‍💻 Autor

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Ako ti GHOST-NET pomaže, ostavi ⭐

</div>
