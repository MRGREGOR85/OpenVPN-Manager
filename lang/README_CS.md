<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN z CMD: vybereš zemi, napíšeš server a jsi připojen. 19 poskytovatelů VPN, kill switch a speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Stáhnout GHOST-NET" width="380"></a>

**Windows 10 a 11 · funguje s GhostVPN**

## [🇵🇱 Polski](../README_PL.md) &nbsp; [🇬🇧 English](../README.md) &nbsp; [🇩🇪 Deutsch](README_DE.md) &nbsp; [🇨🇿 Čeština](README_CS.md) &nbsp; [🇸🇰 Slovenčina](README_SK.md) &nbsp; [🇺🇦 Українська](README_UK.md) &nbsp; [🇷🇺 Русский](README_RU.md) &nbsp; [🇱🇹 Lietuvių](README_LT.md) &nbsp; [🇱🇻 Latviešu](README_LV.md) &nbsp; [🇪🇪 Eesti](README_ET.md) &nbsp; [🇪🇸 Español](README_ES.md) &nbsp; [🇫🇷 Français](README_FR.md) &nbsp; [🇮🇹 Italiano](README_IT.md) &nbsp; [🇵🇹 Português](README_PT.md) &nbsp; [🇳🇱 Nederlands](README_NL.md) &nbsp; [🇸🇪 Svenska](README_SV.md) &nbsp; [🇩🇰 Dansk](README_DA.md) &nbsp; [🇳🇴 Norsk](README_NO.md) &nbsp; [🇫🇮 Suomi](README_FI.md) &nbsp; [🇭🇺 Magyar](README_HU.md) &nbsp; [🇷🇴 Română](README_RO.md) &nbsp; [🇧🇬 Български](README_BG.md) &nbsp; [🇬🇷 Ελληνικά](README_EL.md) &nbsp; [🇭🇷 Hrvatski](README_HR.md) &nbsp; [🇷🇸 Српски](README_SR.md) &nbsp; [🇸🇮 Slovenščina](README_SL.md) &nbsp; [🇹🇷 Türkçe](README_TR.md) &nbsp; [🇻🇳 Tiếng Việt](README_VI.md) &nbsp; [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Hlavní obrazovka GHOST-NET" width="100%">

📸 **Hlavní obrazovka.** Nahoře: země, kde má tvůj poskytovatel servery. Pod nimi: kódy zemí k napsání, například `pl` = Polsko. Níže: stav kill switche a 19 poskytovatelů VPN, zvýrazněný je ten, který používáš. Úplně dole napíšeš kód země.

<br>

---

## 💀 Co je GHOST-NET?

Správce VPN v obyčejném okně CMD. Připojí tě přes OpenVPN k serveru tvého vlastního poskytovatele VPN, takže weby vidí IP serveru místo tvé. Používá stejné soubory serverů jako [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Program umí 29 jazyků. Jazyk změníš klávesou `TAB` na hlavní obrazovce.

<br>

---

## ✨ Funkce

| Funkce | Co dělá |
|---|---|
| **19 poskytovatelů VPN** | NordVPN, ProtonVPN, Surfshark, Mullvad a další. Přepínáš šipkami nebo číslem. |
| **Živý ping** | Seznam serverů ukazuje, který je nejrychlejší. |
| **Kill switch** | Brána firewall Windows blokuje internet mimo VPN. Když tunel spadne, tvoje IP neunikne. Domácí síť dál funguje. |
| **Ochrana DNS** | Dotazy DNS neopustí tunel. |
| **Obrazovka připojení** | Nová IP, město, poskytovatel, ping a šifra. |
| **Speedtest** | Test rychlosti na souboru 1 GB, výsledek v Mbit/s. |
| **Chytré chyby** | Zpráva v Poznámkovém bloku, návrh dalšího serveru a automatické stažení nových serverů NordVPN. |
| **29 jazyků** | Program umí 29 jazyků. Jazyk změníš klávesou `TAB` na hlavní obrazovce. |

<br>

---

## 📋 Co potřebuješ

**Windows 10 nebo 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (nebo [OpenVPN](https://openvpn.net/community-downloads/)) · **účet u poskytovatele VPN** · **práva správce** (skript si o ně řekne sám)

<br>

---

## 📖 Návod

<br>

### 1️⃣ Stáhnout

Klikni na **Stáhnout GHOST-NET**. Přesuň **GhostNet.exe** do vlastní složky, například `C:\GHOST-NET`, protože skript si vedle sebe ukládá nastavení a přihlášení.

<br>

### 2️⃣ Spustit

Dvakrát klikni na **GhostNet.exe** a klikni na **Ano**, když se Windows zeptá na oprávnění. Pokud Windows ukáže varování: **Další informace** → **Přesto spustit**. Při prvním spuštění si vyber jazyk.

<img src="../screenshots/language-select.png" alt="29 jazyků" width="100%">

📸 **29 jazyků.** Program umí 29 jazyků. Jazyk změníš klávesou `TAB` na hlavní obrazovce.

<br>

### 3️⃣ Vyber zemi

Napiš kód země a stiskni **Enter**, například `pl`, `de` nebo `us`. Poskytovatele změníš šipkami nebo číslem od `1` do `19`.

<br>

### 4️⃣ Vyber server

Napiš název serveru ze seznamu, nebo jen jeho začátek, například `pl1273`, a stiskni **Enter**.

<img src="../screenshots/server-ping.png" alt="Seznam serverů s pingem" width="100%">

📸 **Seznam serverů.** Každý server má v závorce ping, tedy dobu odezvy: čím méně `ms`, tím rychlejší. `udp` bývá rychlejší, `tcp` lépe projde blokacemi. Dole napíšeš vybraný server.

<br>

### 5️⃣ Zadej přihlášení (jen poprvé)

Skript se zeptá na uživatelské jméno a heslo k OpenVPN a poradí, kde je najdeš. NordVPN a Surfshark mají zvláštní *Service credentials*, ne e-mail a heslo k účtu.

<img src="../screenshots/login.png" alt="První přihlášení" width="100%">

📸 **První přihlášení.** Skript ukazuje, pro kterého poskytovatele zadáváš údaje a kde je najdeš. Heslo je skryté hvězdičkami. Přihlášení se uloží jednou a příště ho nemusíš psát znovu.

<br>

### 6️⃣ Hotovo

<img src="../screenshots/connected.png" alt="Obrazovka připojení" width="100%">

📸 **Připojeno.** `NODE_IP` je tvoje nová IP, kterou vidí weby. `PING` je rychlost tunelu, `ENCRYPTION` šifra a `KILL_SWITCH` říká, zda je internet mimo VPN blokovaný. `LOCATION` a `PROVIDER` jsou město a firma serveru. Dole: `1` speedtest, `2` odpojit, `3` kill switch.

<br>

---

## ⌨️ Příkazy

| Napiš | Co dělá |
|---|---|
| `pl`, `de`, `us`… | servery v té zemi |
| `1` … `19` | změna poskytovatele VPN |
| `TAB` | změna jazyka |
| `ks` | kill switch zapnout nebo vypnout |
| `fs` | celá obrazovka nebo okno |
| `Alt+C` | odpojit VPN (funguje všude) |
| `1` / `2` / `3` po připojení | speedtest / odpojit / kill switch |

<br>

---

## 🌍 Poskytovatelé

`NordVPN` (v seznamu jako **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET VPN neprodává: používáš svůj vlastní účet. Soubory serverů přidáš v GhostVPN.

<br>

---

## 🆘 Něco nefunguje?

| Co vidím | Co dělat |
|---|---|
| **OpenVPN**: není nainstalován | Nainstaluj [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) nebo [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: žádné soubory serverů | Přidej servery tohoto poskytovatele v GhostVPN, nebo vyber jiného poskytovatele. |
| **AUTH_FAILED** | Zvol `1` a zkus další server. Pokud nefunguje žádný, zvol `2` a zadej přihlášení znovu. |
| **TUNNEL FAILED** | Přečti si zprávu v Poznámkovém bloku. Vyber jiný server. |
| Žádný internet po zavření okna | Spusť skript a zvol **ZRUŠIT BLOKACI**, nebo napiš `ks`. |

> 🔒 Přihlášení zůstávají jen v tvém počítači, ve složce vedle skriptu. Tuto složku nikomu nedávej.

<br>

---

## 📜 Licence

### Pouze pro soukromé domácí použití. GHOST-NET patří výhradně autorovi, MRGREGOR85.

**Není dovoleno** ho prodávat, dávat nebo posílat jiným, nahrávat na jiné weby, fóra či Discord, používat ve firmě, upravovat ho ani kopírovat jeho kód. Každý si stáhne vlastní kopii z této stránky. Plné znění: [LICENSE](../LICENSE).

<br>

---

## 🎬 YouTube

<a href="https://youtu.be/Fb_61rHk95Y"><img src="../docs/images/video.jpg" alt="Kompletní videonávod na YouTube" width="100%"></a>

<br>

---

## 👨‍💻 Autor

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Pokud ti GHOST-NET pomáhá, nech ⭐

</div>
