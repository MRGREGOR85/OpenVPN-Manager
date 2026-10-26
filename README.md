<div align="center">

<img src="docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN from CMD: pick a country, type a server and you're connected. 19 VPN providers, kill switch and speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="docs/images/download_en.png" alt="Download GHOST-NET" width="380"></a>

**Windows 10 and 11 · works with GhostVPN**

## [🇵🇱 Polski](README_PL.md) &nbsp; [🇬🇧 English](README.md) &nbsp; [🇩🇪 Deutsch](lang/README_DE.md) &nbsp; [🇨🇿 Čeština](lang/README_CS.md) &nbsp; [🇸🇰 Slovenčina](lang/README_SK.md) &nbsp; [🇺🇦 Українська](lang/README_UK.md) &nbsp; [🇷🇺 Русский](lang/README_RU.md) &nbsp; [🇱🇹 Lietuvių](lang/README_LT.md) &nbsp; [🇱🇻 Latviešu](lang/README_LV.md) &nbsp; [🇪🇪 Eesti](lang/README_ET.md) &nbsp; [🇪🇸 Español](lang/README_ES.md) &nbsp; [🇫🇷 Français](lang/README_FR.md) &nbsp; [🇮🇹 Italiano](lang/README_IT.md) &nbsp; [🇵🇹 Português](lang/README_PT.md) &nbsp; [🇳🇱 Nederlands](lang/README_NL.md) &nbsp; [🇸🇪 Svenska](lang/README_SV.md) &nbsp; [🇩🇰 Dansk](lang/README_DA.md) &nbsp; [🇳🇴 Norsk](lang/README_NO.md) &nbsp; [🇫🇮 Suomi](lang/README_FI.md) &nbsp; [🇭🇺 Magyar](lang/README_HU.md) &nbsp; [🇷🇴 Română](lang/README_RO.md) &nbsp; [🇧🇬 Български](lang/README_BG.md) &nbsp; [🇬🇷 Ελληνικά](lang/README_EL.md) &nbsp; [🇭🇷 Hrvatski](lang/README_HR.md) &nbsp; [🇷🇸 Српски](lang/README_SR.md) &nbsp; [🇸🇮 Slovenščina](lang/README_SL.md) &nbsp; [🇹🇷 Türkçe](lang/README_TR.md) &nbsp; [🇻🇳 Tiếng Việt](lang/README_VI.md) &nbsp; [🇮🇩 Indonesia](lang/README_ID.md)

<br>

<img src="screenshots/main-screen.png" alt="GHOST-NET main screen" width="100%">

📸 **Main screen.** At the top: the countries where your provider has servers. Below them: the country codes to type, for example `pl` = Poland. Further down: the kill switch status and the 19 VPN providers, the highlighted one is the one in use. At the very bottom you type a country code.

<br>

---

## 💀 What is GHOST-NET?

A VPN manager in a plain CMD window. It connects you through OpenVPN to a server of your own VPN provider, so websites see the server's IP instead of yours. It uses the same server files as [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). The program speaks 29 languages. Press `TAB` on the main screen to change the language.

<br>

---

## ✨ Features

| Feature | What it does |
|---|---|
| **19 VPN providers** | NordVPN, ProtonVPN, Surfshark, Mullvad and more. Switch with the arrow keys or a number. |
| **Live ping** | The server list shows which server is fastest. |
| **Kill switch** | Windows Firewall blocks internet outside the VPN. If the tunnel drops, your IP doesn't leak. Your home network keeps working. |
| **DNS protection** | DNS queries can't leave the tunnel. |
| **Connection screen** | New IP, city, provider, ping and cipher. |
| **Speedtest** | Speed test on a 1 GB file, result in Mbit/s. |
| **Smart errors** | Report in Notepad, the next server suggested, and fresh NordVPN servers downloaded automatically. |
| **29 languages** | The program speaks 29 languages. Press `TAB` on the main screen to change the language. |

<br>

---

## 📋 What you need

**Windows 10 or 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (or [OpenVPN](https://openvpn.net/community-downloads/)) · **a VPN provider account** · **administrator rights** (the program asks for them)

<br>

---

## 📖 Guide

<br>

### 1️⃣ Download

Click **Download GHOST-NET**. Move **GhostNet.exe** to its own folder, for example `C:\GHOST-NET`, because the program saves settings and logins next to itself.

<br>

### 2️⃣ Run it

Double-click **GhostNet.exe** and click **Yes** when Windows asks for permission. If Windows shows a warning: **More info** → **Run anyway**. On the first start, choose your language.

<img src="screenshots/language-select.png" alt="29 languages" width="100%">

📸 **29 languages.** The program speaks 29 languages. Press `TAB` on the main screen to change the language.

<br>

### 3️⃣ Pick a country

Type a country code and press **Enter**, for example `pl`, `de` or `us`. Change the provider with the arrow keys or a number from `1` to `19`.

<br>

### 4️⃣ Pick a server

Type the server name from the list, or just its beginning, for example `pl1273`, and press **Enter**.

<img src="screenshots/server-ping.png" alt="Server list with ping" width="100%">

📸 **Server list.** Each server shows its ping in brackets, the response time: the lower the `ms`, the faster. `udp` is usually faster, `tcp` gets through blocks more easily. At the bottom you type the server you want.

<br>

### 5️⃣ Enter your login (first time only)

The program asks for your OpenVPN username and password and tells you where to find them. NordVPN and Surfshark use separate *Service credentials*, not your account e-mail and password.

<img src="screenshots/login.png" alt="First login" width="100%">

📸 **First login.** The program shows which provider the login is for and where to find it. The password is hidden with asterisks. The login is saved once, so you don't type it again next time.

<br>

### 6️⃣ Done

<img src="screenshots/connected.png" alt="Connection screen" width="100%">

📸 **Connected.** `NODE_IP` is your new IP that websites see. `PING` is the tunnel speed, `ENCRYPTION` the cipher, and `KILL_SWITCH` tells you whether internet outside the VPN is blocked. `LOCATION` and `PROVIDER` are the server's city and company. At the bottom: `1` speedtest, `2` disconnect, `3` kill switch.

<br>

---

## ⌨️ Commands

| Type | What it does |
|---|---|
| `pl`, `de`, `us`… | servers in that country |
| `1` … `19` | switch VPN provider |
| `TAB` | change the language |
| `ks` | kill switch on or off |
| `fs` | full screen or window |
| `Alt+C` | disconnect the VPN (works everywhere) |
| `1` / `2` / `3` when connected | speedtest / disconnect / kill switch |

<br>

---

## 🌍 Providers

`NordVPN` (listed as **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET doesn't sell VPN: you use your own account. Add server files in GhostVPN.

<br>

---

## 🆘 Something is not working?

| What I see | What to do |
|---|---|
| **OpenVPN**: not installed | Install [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) or [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: no server files | Add this provider's servers in GhostVPN, or pick another provider. |
| **AUTH_FAILED** | Choose `1` to try the next server. If none work, choose `2` and enter your login again. |
| **TUNNEL FAILED** | Read the report in Notepad. Pick another server. |
| No internet after closing the window | Start the program and choose **REMOVE BLOCK**, or type `ks`. |

> 🔒 Logins stay only on your computer, in the folder next to the program. Don't give that folder to anyone.

<br>

---

## 📜 License

### Private home use only. GHOST-NET belongs exclusively to its author, MRGREGOR85.

**You may not** sell it, give or send it to others, upload it to other websites, forums or Discord, use it in a company, modify it or copy its code. Everyone downloads their own copy from this page. Full text: [LICENSE](LICENSE).

<br>

---

## 🎬 YouTube

<a href="https://youtu.be/Fb_61rHk95Y"><img src="docs/images/video.jpg" alt="Full video guide on YouTube" width="480"></a>

<br>

---

## 👨‍💻 Author

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### If GHOST-NET helps you, please leave a ⭐

</div>
