<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### Le VPN depuis CMD : choisis un pays, tape un serveur et tu es connecté. 19 fournisseurs VPN, kill switch et speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Télécharger GHOST-NET" width="380"></a>

**Windows 10 et 11 · fonctionne avec GhostVPN**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · [🇵🇹 Português](README_PT.md) · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Écran principal de GHOST-NET" width="100%">

📸 **Écran principal.** En haut : les pays où ton fournisseur a des serveurs. En dessous : les codes pays à taper, par exemple `pl` = Pologne. Plus bas : l'état du kill switch et les 19 fournisseurs VPN, celui en surbrillance est celui utilisé. Tout en bas, tu tapes un code pays.

<br>

---

## 💀 Qu'est-ce que GHOST-NET ?

Un gestionnaire VPN dans une simple fenêtre CMD. Il te connecte via OpenVPN à un serveur de ton propre fournisseur VPN : les sites voient l'IP du serveur au lieu de la tienne. Il utilise les mêmes fichiers de serveurs que [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). Le programme parle 29 langues. Appuie sur `TAB` sur l'écran principal pour changer de langue.

<br>

---

## ✨ Fonctions

| Fonction | Ce qu'elle fait |
|---|---|
| **19 fournisseurs VPN** | NordVPN, ProtonVPN, Surfshark, Mullvad et d'autres. Change avec les flèches ou un numéro. |
| **Ping en direct** | La liste des serveurs montre le plus rapide. |
| **Kill switch** | Le pare-feu Windows bloque Internet en dehors du VPN. Si le tunnel tombe, ton IP ne fuit pas. Ton réseau local continue de marcher. |
| **Protection DNS** | Les requêtes DNS ne sortent pas du tunnel. |
| **Écran de connexion** | Nouvelle IP, ville, fournisseur, ping et chiffrement. |
| **Speedtest** | Test de vitesse sur un fichier de 1 Go, résultat en Mbit/s. |
| **Erreurs intelligentes** | Rapport dans le Bloc-notes, serveur suivant proposé et nouveaux serveurs NordVPN téléchargés automatiquement. |
| **29 langues** | Le programme parle 29 langues. Appuie sur `TAB` sur l'écran principal pour changer de langue. |

<br>

---

## 📋 Ce qu'il te faut

**Windows 10 ou 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (ou [OpenVPN](https://openvpn.net/community-downloads/)) · **un compte chez un fournisseur VPN** · **les droits administrateur** (le script les demande lui-même)

<br>

---

## 📖 Guide

<br>

### 1️⃣ Télécharger

Clique sur **Télécharger GHOST-NET**. Déplace **GhostNet.exe** dans son propre dossier, par exemple `C:\GHOST-NET`, car le script enregistre ses réglages et identifiants à côté de lui.

<br>

### 2️⃣ Lancer

Double-clique sur **GhostNet.exe** et clique sur **Oui** quand Windows demande l'autorisation. Si Windows affiche un avertissement : **Informations complémentaires** → **Exécuter quand même**. Au premier démarrage, choisis ta langue.

<img src="../screenshots/language-select.png" alt="29 langues" width="100%">

📸 **29 langues.** Le programme parle 29 langues. Appuie sur `TAB` sur l'écran principal pour changer de langue.

<br>

### 3️⃣ Choisir un pays

Tape un code pays et appuie sur **Entrée**, par exemple `pl`, `de` ou `us`. Change de fournisseur avec les flèches ou un numéro de `1` à `19`.

<br>

### 4️⃣ Choisir un serveur

Tape le nom du serveur de la liste, ou juste son début, par exemple `pl1273`, et appuie sur **Entrée**.

<img src="../screenshots/server-ping.png" alt="Liste des serveurs avec ping" width="100%">

📸 **Liste des serveurs.** Chaque serveur affiche son ping entre crochets, le temps de réponse : moins il y a de `ms`, plus c'est rapide. `udp` est souvent plus rapide, `tcp` passe plus facilement les blocages. En bas, tu tapes le serveur choisi.

<br>

### 5️⃣ Entrer ton identifiant (la première fois)

Le script demande ton nom d'utilisateur et ton mot de passe OpenVPN et t'indique où les trouver. NordVPN et Surfshark utilisent des *Service credentials* séparés, pas l'e-mail et le mot de passe de ton compte.

<img src="../screenshots/login.png" alt="Première connexion" width="100%">

📸 **Première connexion.** Le script montre pour quel fournisseur sont les identifiants et où les trouver. Le mot de passe est masqué par des astérisques. L'identifiant est enregistré une fois, tu n'as pas à le retaper ensuite.

<br>

### 6️⃣ Terminé

<img src="../screenshots/connected.png" alt="Écran de connexion" width="100%">

📸 **Connecté.** `NODE_IP` est ta nouvelle IP vue par les sites. `PING` est la vitesse du tunnel, `ENCRYPTION` le chiffrement, et `KILL_SWITCH` indique si Internet est bloqué hors du VPN. `LOCATION` et `PROVIDER` sont la ville et la société du serveur. En bas : `1` speedtest, `2` déconnecter, `3` kill switch.

<br>

---

## ⌨️ Commandes

| Tape | Ce qu'elle fait |
|---|---|
| `pl`, `de`, `us`… | serveurs de ce pays |
| `1` … `19` | changer de fournisseur VPN |
| `TAB` | changer de langue |
| `ks` | kill switch activé ou désactivé |
| `fs` | plein écran ou fenêtre |
| `Alt+C` | déconnecter le VPN (marche partout) |
| `1` / `2` / `3` une fois connecté | speedtest / déconnecter / kill switch |

<br>

---

## 🌍 Fournisseurs

`NordVPN` (affiché comme **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

GHOST-NET ne vend pas de VPN : tu utilises ton propre compte. Ajoute les fichiers de serveurs dans GhostVPN.

<br>

---

## 🆘 Quelque chose ne marche pas ?

| Ce que je vois | Que faire |
|---|---|
| **OpenVPN**: non installé | Installe [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) ou [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: pas de fichiers serveur | Ajoute les serveurs de ce fournisseur dans GhostVPN, ou choisis un autre fournisseur. |
| **AUTH_FAILED** | Choisis `1` pour essayer le serveur suivant. Si aucun ne marche, choisis `2` et retape ton identifiant. |
| **TUNNEL FAILED** | Lis le rapport dans le Bloc-notes. Choisis un autre serveur. |
| Plus d'Internet après avoir fermé la fenêtre | Lance le script et choisis **RETIRER LE BLOCAGE**, ou tape `ks`. |

> 🔒 Les identifiants restent uniquement sur ton ordinateur, dans le dossier à côté du script. Ne donne ce dossier à personne.

<br>

---

## 📜 Licence

### Usage privé à la maison uniquement. GHOST-NET appartient exclusivement à son auteur, MRGREGOR85.

**Interdit** de le vendre, de le donner ou l'envoyer à d'autres, de le publier sur d'autres sites, forums ou Discord, de l'utiliser en entreprise, de le modifier ou de copier son code. Chacun télécharge sa propre copie depuis cette page. Texte complet : [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Auteur

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Si GHOST-NET t'aide, laisse une ⭐

</div>
