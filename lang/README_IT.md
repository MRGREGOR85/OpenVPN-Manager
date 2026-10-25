<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN dal CMD: scegli un paese, scrivi un server e sei connesso. 19 provider VPN, kill switch e speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Scarica GHOST-NET" width="380"></a>

**Windows 10 e 11 · funziona con GhostVPN**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Schermata principale di GHOST-NET" width="100%">

📸 **Schermata principale.** In alto: i paesi in cui il tuo provider ha server. Sotto: i codici paese da scrivere, per esempio `pl` = Polonia. Più in basso: lo stato del kill switch e i 19 provider VPN, quello evidenziato è quello in uso. In fondo scrivi un codice paese.

<br>

---

## 💀 Cos'è GHOST-NET?

Un gestore VPN in una normale finestra CMD. Ti collega tramite OpenVPN a un server del tuo provider VPN, così i siti vedono l'IP del server invece del tuo. Usa gli stessi file dei server di [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Il programma parla 29 lingue. Premi `TAB` nella schermata principale per cambiare lingua.

<br>

---

## ✨ Funzioni

| Funzione | Cosa fa |
|---|---|
| **19 provider VPN** | NordVPN, ProtonVPN, Surfshark, Mullvad e altri. Cambia con le frecce o con un numero. |
| **Ping in tempo reale** | La lista dei server mostra quale è il più veloce. |
| **Kill switch** | Il Firewall di Windows blocca internet fuori dalla VPN. Se il tunnel cade, il tuo IP non trapela. La rete di casa continua a funzionare. |
| **Protezione DNS** | Le richieste DNS non escono dal tunnel. |
| **Schermata di connessione** | Nuovo IP, città, provider, ping e cifratura. |
| **Speedtest** | Test di velocità su un file da 1 GB, risultato in Mbit/s. |
| **Errori intelligenti** | Rapporto nel Blocco note, proposta del server successivo e download automatico dei nuovi server NordVPN. |
| **29 lingue** | Il programma parla 29 lingue. Premi `TAB` nella schermata principale per cambiare lingua. |

<br>

---

## 📋 Cosa ti serve

**Windows 10 o 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (o [OpenVPN](https://openvpn.net/community-downloads/)) · **un account presso un provider VPN** · **diritti di amministratore** (li chiede lo script)

<br>

---

## 📖 Guida

<br>

### 1️⃣ Scarica

Clicca su **Scarica GHOST-NET**. Sposta **GhostNet.exe** in una cartella dedicata, per esempio `C:\GHOST-NET`, perché lo script salva impostazioni e login accanto a sé.

<br>

### 2️⃣ Avvia

Fai doppio clic su **GhostNet.exe** e clicca **Sì** quando Windows chiede il permesso. Se Windows mostra un avviso: **Ulteriori informazioni** → **Esegui comunque**. Al primo avvio scegli la tua lingua.

<img src="../screenshots/language-select.png" alt="29 lingue" width="100%">

📸 **29 lingue.** Il programma parla 29 lingue. Premi `TAB` nella schermata principale per cambiare lingua.

<br>

### 3️⃣ Scegli un paese

Scrivi un codice paese e premi **Invio**, per esempio `pl`, `de` o `us`. Cambia provider con le frecce o con un numero da `1` a `19`.

<br>

### 4️⃣ Scegli un server

Scrivi il nome del server dalla lista, o solo l'inizio, per esempio `pl1273`, e premi **Invio**.

<img src="../screenshots/server-ping.png" alt="Lista dei server con ping" width="100%">

📸 **Lista dei server.** Ogni server mostra il ping tra parentesi, il tempo di risposta: meno `ms`, più veloce. `udp` di solito è più veloce, `tcp` supera meglio i blocchi. In fondo scrivi il server scelto.

<br>

### 5️⃣ Inserisci il login (solo la prima volta)

Lo script chiede nome utente e password OpenVPN e ti dice dove trovarli. NordVPN e Surfshark usano *Service credentials* separate, non l'e-mail e la password del tuo account.

<img src="../screenshots/login.png" alt="Primo login" width="100%">

📸 **Primo login.** Lo script mostra per quale provider è il login e dove trovarlo. La password è nascosta da asterischi. Il login viene salvato una volta e non devi riscriverlo.

<br>

### 6️⃣ Fatto

<img src="../screenshots/connected.png" alt="Schermata di connessione" width="100%">

📸 **Connesso.** `NODE_IP` è il tuo nuovo IP visto dai siti. `PING` è la velocità del tunnel, `ENCRYPTION` la cifratura, e `KILL_SWITCH` dice se internet fuori dalla VPN è bloccato. `LOCATION` e `PROVIDER` sono città e azienda del server. In fondo: `1` speedtest, `2` disconnetti, `3` kill switch.

<br>

---

## ⌨️ Comandi

| Scrivi | Cosa fa |
|---|---|
| `pl`, `de`, `us`… | server in quel paese |
| `1` … `19` | cambia provider VPN |
| `TAB` | cambia lingua |
| `ks` | kill switch acceso o spento |
| `fs` | schermo intero o finestra |
| `Alt+C` | disconnetti la VPN (funziona ovunque) |
| `1` / `2` / `3` quando connesso | speedtest / disconnetti / kill switch |

<br>

---

## 🌍 Provider

`NordVPN` (nella lista come **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET non vende VPN: usi il tuo account. Aggiungi i file dei server in GhostVPN.

<br>

---

## 🆘 Qualcosa non funziona?

| Cosa vedo | Cosa fare |
|---|---|
| **OpenVPN**: non installato | Installa [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) o [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: nessun file server | Aggiungi i server di questo provider in GhostVPN o scegli un altro provider. |
| **AUTH_FAILED** | Scegli `1` per provare il server successivo. Se nessuno funziona, scegli `2` e reinserisci il login. |
| **TUNNEL FAILED** | Leggi il rapporto nel Blocco note. Scegli un altro server. |
| Niente internet dopo aver chiuso la finestra | Avvia lo script e scegli **RIMUOVI BLOCCO**, oppure scrivi `ks`. |

> 🔒 I login restano solo sul tuo computer, nella cartella accanto allo script. Non dare quella cartella a nessuno.

<br>

---

## 📜 Licenza

### Solo per uso privato e domestico. GHOST-NET appartiene esclusivamente al suo autore, MRGREGOR85.

**Non è permesso** venderlo, darlo o inviarlo ad altri, caricarlo su altri siti, forum o Discord, usarlo in un'azienda, modificarlo o copiarne il codice. Ognuno scarica la propria copia da questa pagina. Testo completo: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Autore

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Se GHOST-NET ti aiuta, lascia una ⭐

</div>
