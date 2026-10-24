# 💀 GHOST-NET VPN Manager

**A console OpenVPN manager for Windows, made for people who like living in `cmd`.**

Pick a country, see the ping of every server, connect with one name, run a speedtest, and lock your internet behind the VPN with a firewall kill switch, all in a green hacker-style terminal.

*by MRGREGOR85*

![Main screen](menu%20tcp_ydp.png)

---

## ✨ Features

- **19 VPN providers in one menu**: NordVPN (OpenVPN), ProtonVPN, ExpressVPN, PrivadoVPN, Surfshark, AirVPN, CyberGhost, PIA, IPVanish, OVPN.com, Mullvad, PureVPN, VyprVPN, IVPN, PrivateVPN, Perfect Privacy, HMA, FastVPN and TorGuard.
- **Country list and code database**: every country with servers is listed, and you just type its code (`pl`, `de`, `us`...).
- **Fast parallel ping**: up to 300 servers are pinged at the same time, and you see the latency of each one in ms before connecting.
- **Live connection screen**: status, server IP, ping, location, provider and session time.
- **Speedtest**: downloads a 1 GB test file from Hetzner through the tunnel and shows the average speed.
- **Kill switch on the Windows Firewall**: blocks all traffic outside the VPN. Your firewall settings are backed up and restored when you turn it off. Local network (printer, router, NAS) keeps working.
- **Quick disconnect**: `ALT+C` disconnects from anywhere, including the main screen.
- **29 languages**: press `TAB` on the main screen to change the language.
- **720p window or full screen**: type `fs` to switch.
- **Auto-fix for NordVPN**: if a server no longer exists, the program downloads fresh server files.
- Written in Python using only the standard library, with a ready-made `GhostNet.exe`.

---

## 📸 Screenshots

### Server list with ping
![Server ping](lista%20serwerow%20tcp_udp.png)

### Connected (Ghost Mode)
![Connected](menu%20tcp_udp.jpg)

### Speedtest
![Speedtest](speedtest%20tcp_udp.jpg)

---

## 🧰 Requirements

- Windows 10 or 11
- **OpenVPN** installed in `C:\Program Files\OpenVPN\bin` (or GhostVPN in `C:\Program Files\GhostVPN\bin`)
- Administrator rights (the program asks for them on start, because it needs them for OpenVPN and the firewall)
- An account with at least one of the supported VPN providers
- Python 3.10+ is needed **only** if you run the `.py` version instead of the `.exe`

---

## 🚀 Installation

1. Download **`GhostNet.exe`** from [Releases](../../releases) (or download the source code).
2. Put your provider's `.ovpn` server files into its folder in `C:\Program Files\GhostVPN\`:

   | Provider | Folder |
   |---|---|
   | NordVPN (OpenVPN) | `config` |
   | ProtonVPN | `proton_config` |
   | ExpressVPN | `express_config` |
   | PrivadoVPN | `privado_config` |
   | Surfshark | `surfshark_config` |
   | AirVPN | `airvpn_config` |
   | CyberGhost | `cyberghost_config` |
   | PIA VPN | `pia_config` |
   | IPVanish | `ipvanish_config` |
   | OVPN.com | `ovpncom_config` |
   | Mullvad VPN | `mullvad_config` |
   | PureVPN | `purevpn_config` |
   | VyprVPN | `vyprvpn_config` |
   | IVPN | `ivpn_config` |
   | PrivateVPN | `privatevpn_config` |
   | Perfect Privacy | `perfectprivacy_config` |
   | HMA VPN | `hma_config` |
   | FastVPN | `fastvpn_config` |
   | TorGuard | `torguard_config` |

   Example: `C:\Program Files\GhostVPN\config\pl128.nordvpn.com.udp.ovpn`
3. Run `GhostNet.exe` and accept the administrator prompt.
4. On the first start, choose your language.

**Running from source:** double-click `uruchom.bat` or run `python ghostnet.py`.
**Building the .exe yourself:** run `zbuduj_exe.bat` (it installs PyInstaller and builds `GhostNet.exe`).

---

## 🕹️ How to use

| On the main screen | What it does |
|---|---|
| `↑ ↓ ← →` + `ENTER` | choose a VPN provider |
| type a provider number + `ENTER` | the same, faster |
| type a country code (e.g. `pl`) + `ENTER` | show servers in that country with ping |
| `TAB` | change the language |
| `ks` | kill switch on / off |
| `fs` | full screen / 720p window |
| `lang` | change the language (same as TAB) |
| `ALT+C` | disconnect immediately |

**Connecting step by step:**
1. Choose the provider.
2. Type the country code. The program pings all servers and shows the results.
3. Type the server name. The beginning is enough, e.g. `pl128`.
4. The first time, enter your VPN **service** username and password. The program shows a hint for each provider, e.g. NordVPN uses *Service credentials* from the Nord Account dashboard, not your e-mail.
5. When connected, you can choose `[1]` speedtest, `[2]` disconnect or `[3]` kill switch.

---

## 🛡️ Kill switch: how it works

When the kill switch is **ON** and you connect:

- the Windows Firewall switches to **block all outgoing traffic**,
- allowed are only the VPN tunnel adapter, the VPN server's IP, `openvpn.exe`, DHCP and your local network,
- your previous firewall settings are saved to `killswitch_backup.txt` and **restored** when you disconnect or turn the kill switch off.

If the VPN drops, your real IP does not leak, because nothing goes out outside the tunnel.

---

## 🔒 Your data stays on your PC

Your VPN logins are saved **only locally**, next to the program (`Login.txt` and the `loginy` folder). They are never sent anywhere except to your VPN provider by OpenVPN.

⚠️ **Never upload `Login.txt`, the `loginy` or `bledy` folders, or `killswitch_backup.txt` anywhere.**

---

## 📜 License

Copyright © 2026 **MRGREGOR85**. All rights reserved.

You may use this program for your own private, non-commercial use. You may **not** copy, re-upload, share, modify or sell it without the author's permission. Official sources are only the places where the author has published it, such as this GitHub page. Full text in [LICENSE](LICENSE).

---

## 👨‍💻 About the author

**MRGREGOR85**: a hobby project, made for people who like working in the command line, just like me. 💀
