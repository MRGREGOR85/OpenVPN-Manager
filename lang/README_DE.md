<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN aus der CMD: Land wählen, Server eintippen, verbunden. 19 VPN-Anbieter, Kill Switch und Speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="GHOST-NET herunterladen" width="380"></a>

**Windows 10 und 11 · funktioniert mit GhostVPN**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="GHOST-NET Hauptbildschirm" width="100%">

📸 **Hauptbildschirm.** Oben: die Länder, in denen dein Anbieter Server hat. Darunter: die Ländercodes zum Eintippen, zum Beispiel `pl` = Polen. Weiter unten: der Status des Kill Switch und die 19 VPN-Anbieter, der markierte ist der aktive. Ganz unten tippst du einen Ländercode ein.

<br>

---

## 💀 Was ist GHOST-NET?

Ein VPN-Manager in einem normalen CMD-Fenster. Er verbindet dich über OpenVPN mit einem Server deines eigenen VPN-Anbieters, sodass Websites die IP des Servers statt deiner sehen. Er nutzt dieselben Serverdateien wie [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Das Programm spricht 29 Sprachen. Mit `TAB` auf dem Hauptbildschirm wechselst du die Sprache.

<br>

---

## ✨ Funktionen

| Funktion | Was sie macht |
|---|---|
| **19 VPN-Anbieter** | NordVPN, ProtonVPN, Surfshark, Mullvad und mehr. Wechsel mit den Pfeiltasten oder einer Nummer. |
| **Live-Ping** | Die Serverliste zeigt, welcher Server am schnellsten ist. |
| **Kill Switch** | Die Windows-Firewall blockiert das Internet außerhalb des VPN. Fällt der Tunnel aus, bleibt deine IP geschützt. Das Heimnetz funktioniert weiter. |
| **DNS-Schutz** | DNS-Anfragen verlassen den Tunnel nicht. |
| **Verbindungsbildschirm** | Neue IP, Stadt, Anbieter, Ping und Verschlüsselung. |
| **Speedtest** | Geschwindigkeitstest mit einer 1-GB-Datei, Ergebnis in Mbit/s. |
| **Schlaue Fehlermeldungen** | Bericht im Editor, Vorschlag für den nächsten Server und automatischer Download neuer NordVPN-Server. |
| **29 Sprachen** | Das Programm spricht 29 Sprachen. Mit `TAB` auf dem Hauptbildschirm wechselst du die Sprache. |

<br>

---

## 📋 Was du brauchst

**Windows 10 oder 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (oder [OpenVPN](https://openvpn.net/community-downloads/)) · **ein Konto bei einem VPN-Anbieter** · **Administratorrechte** (das Skript fragt selbst danach)

<br>

---

## 📖 Anleitung

<br>

### 1️⃣ Herunterladen

Klicke auf **GHOST-NET herunterladen**. Verschiebe **GhostNet.exe** in einen eigenen Ordner, zum Beispiel `C:\GHOST-NET`, denn das Skript speichert Einstellungen und Logins neben sich.

<br>

### 2️⃣ Starten

Doppelklicke auf **GhostNet.exe** und klicke auf **Ja**, wenn Windows nach der Berechtigung fragt. Zeigt Windows eine Warnung: **Weitere Informationen** → **Trotzdem ausführen**. Beim ersten Start wählst du deine Sprache.

<img src="../screenshots/language-select.png" alt="29 Sprachen" width="100%">

📸 **29 Sprachen.** Das Programm spricht 29 Sprachen. Mit `TAB` auf dem Hauptbildschirm wechselst du die Sprache.

<br>

### 3️⃣ Land wählen

Tippe einen Ländercode ein und drücke **Enter**, zum Beispiel `pl`, `de` oder `us`. Den Anbieter wechselst du mit den Pfeiltasten oder einer Nummer von `1` bis `19`.

<br>

### 4️⃣ Server wählen

Tippe den Servernamen aus der Liste oder nur seinen Anfang ein, zum Beispiel `pl1273`, und drücke **Enter**.

<img src="../screenshots/server-ping.png" alt="Serverliste mit Ping" width="100%">

📸 **Serverliste.** Jeder Server zeigt in Klammern seinen Ping, also die Antwortzeit: je weniger `ms`, desto schneller. `udp` ist meist schneller, `tcp` kommt leichter durch Sperren. Unten tippst du den gewünschten Server ein.

<br>

### 5️⃣ Login eingeben (nur beim ersten Mal)

Das Skript fragt nach deinem OpenVPN-Benutzernamen und Passwort und sagt dir, wo du sie findest. NordVPN und Surfshark nutzen eigene *Service credentials*, nicht die E-Mail und das Passwort deines Kontos.

<img src="../screenshots/login.png" alt="Erster Login" width="100%">

📸 **Erster Login.** Das Skript zeigt, für welchen Anbieter der Login ist und wo du ihn findest. Das Passwort wird mit Sternchen verborgen. Der Login wird einmal gespeichert, beim nächsten Mal musst du ihn nicht erneut eingeben.

<br>

### 6️⃣ Fertig

<img src="../screenshots/connected.png" alt="Verbindungsbildschirm" width="100%">

📸 **Verbunden.** `NODE_IP` ist deine neue IP, die Websites sehen. `PING` ist die Geschwindigkeit des Tunnels, `ENCRYPTION` die Verschlüsselung, und `KILL_SWITCH` zeigt, ob das Internet außerhalb des VPN blockiert ist. `LOCATION` und `PROVIDER` sind Stadt und Firma des Servers. Unten: `1` Speedtest, `2` trennen, `3` Kill Switch.

<br>

---

## ⌨️ Befehle

| Eingabe | Was sie macht |
|---|---|
| `pl`, `de`, `us`… | Server in diesem Land |
| `1` … `19` | VPN-Anbieter wechseln |
| `TAB` | Sprache wechseln |
| `ks` | Kill Switch ein oder aus |
| `fs` | Vollbild oder Fenster |
| `Alt+C` | VPN trennen (funktioniert überall) |
| `1` / `2` / `3` wenn verbunden | Speedtest / trennen / Kill Switch |

<br>

---

## 🌍 Anbieter

`NordVPN` (in der Liste als **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET verkauft kein VPN: du nutzt dein eigenes Konto. Serverdateien fügst du in GhostVPN hinzu.

<br>

---

## 🆘 Etwas funktioniert nicht?

| Was ich sehe | Was zu tun ist |
|---|---|
| **OpenVPN**: nicht installiert | Installiere [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) oder [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: keine Serverdateien | Füge die Server dieses Anbieters in GhostVPN hinzu oder wähle einen anderen Anbieter. |
| **AUTH_FAILED** | Wähle `1`, um den nächsten Server zu versuchen. Wenn keiner funktioniert, wähle `2` und gib deinen Login erneut ein. |
| **TUNNEL FAILED** | Lies den Bericht im Editor. Wähle einen anderen Server. |
| Kein Internet nach dem Schließen des Fensters | Starte das Skript und wähle **SPERRE AUFHEBEN** oder tippe `ks`. |

> 🔒 Logins bleiben nur auf deinem Computer, im Ordner neben dem Skript. Gib diesen Ordner niemandem.

<br>

---

## 📜 Lizenz

### Nur für den privaten Gebrauch zu Hause. GHOST-NET gehört ausschließlich seinem Autor, MRGREGOR85.

**Du darfst es nicht** verkaufen, an andere weitergeben oder senden, auf andere Websites, Foren oder Discord hochladen, in einer Firma nutzen, verändern oder seinen Code kopieren. Jeder lädt seine eigene Kopie von dieser Seite herunter. Volltext: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Autor

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Wenn dir GHOST-NET hilft, lass einen ⭐ da

</div>
