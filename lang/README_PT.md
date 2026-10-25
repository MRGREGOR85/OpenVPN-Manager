<div align="center">

<img src="../docs/images/banner.png" alt="GHOST-NET VPN MANAGER PRO" width="100%">

# GHOST-NET VPN MANAGER PRO · Windows 10/11

### VPN pelo CMD: escolha um país, digite um servidor e pronto, conectado. 19 provedores VPN, kill switch e speedtest.

<picture><img src="https://img.shields.io/badge/version-2.0-0e6830?style=for-the-badge" alt="version"></picture> <picture><img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 10 | 11"></picture> <a href="../LICENSE"><img src="https://img.shields.io/badge/license-home%20use%20only-red?style=for-the-badge" alt="License"></a>

<a href="https://github.com/MRGREGOR85/OpenVPN-Manager/releases/latest/download/GhostNet.exe"><img src="../docs/images/download_en.png" alt="Baixar GHOST-NET" width="380"></a>

**Windows 10 e 11 · funciona com o GhostVPN**

## [🇵🇱 Polski](../README_PL.md) · [🇬🇧 English](../README.md) · [🇩🇪 Deutsch](README_DE.md) · [🇨🇿 Čeština](README_CS.md) · [🇸🇰 Slovenčina](README_SK.md) · [🇺🇦 Українська](README_UK.md) · [🇷🇺 Русский](README_RU.md) · [🇱🇹 Lietuvių](README_LT.md) · [🇱🇻 Latviešu](README_LV.md) · [🇪🇪 Eesti](README_ET.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇮🇹 Italiano](README_IT.md) · 🇵🇹 Português · [🇳🇱 Nederlands](README_NL.md) · [🇸🇪 Svenska](README_SV.md) · [🇩🇰 Dansk](README_DA.md) · [🇳🇴 Norsk](README_NO.md) · [🇫🇮 Suomi](README_FI.md) · [🇭🇺 Magyar](README_HU.md) · [🇷🇴 Română](README_RO.md) · [🇧🇬 Български](README_BG.md) · [🇬🇷 Ελληνικά](README_EL.md) · [🇭🇷 Hrvatski](README_HR.md) · [🇷🇸 Српски](README_SR.md) · [🇸🇮 Slovenščina](README_SL.md) · [🇹🇷 Türkçe](README_TR.md) · [🇻🇳 Tiếng Việt](README_VI.md) · [🇮🇩 Indonesia](README_ID.md)

<br>

<img src="../screenshots/main-screen.png" alt="Tela principal do GHOST-NET" width="100%">

📸 **Tela principal.** No topo: os países onde seu provedor tem servidores. Abaixo: os códigos de país para digitar, por exemplo `pl` = Polônia. Mais abaixo: o estado do kill switch e os 19 provedores VPN; o destacado é o que está em uso. Bem embaixo você digita um código de país.

<br>

---

## 💀 O que é o GHOST-NET?

Um gerenciador de VPN numa janela comum do CMD. Ele conecta você via OpenVPN a um servidor do seu próprio provedor VPN, e os sites veem o IP do servidor em vez do seu. Usa os mesmos arquivos de servidores do [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA). O programa fala 29 idiomas. Prima `TAB` no ecrã principal para mudar de idioma.

<br>

---

## ✨ Recursos

| Recurso | O que faz |
|---|---|
| **19 provedores VPN** | NordVPN, ProtonVPN, Surfshark, Mullvad e outros. Troque com as setas ou com um número. |
| **Ping ao vivo** | A lista de servidores mostra qual é o mais rápido. |
| **Kill switch** | O Firewall do Windows bloqueia a internet fora da VPN. Se o túnel cair, seu IP não vaza. Sua rede de casa continua funcionando. |
| **Proteção de DNS** | As consultas DNS não saem do túnel. |
| **Tela de conexão** | Novo IP, cidade, provedor, ping e criptografia. |
| **Speedtest** | Teste de velocidade com um arquivo de 1 GB, resultado em Mbit/s. |
| **Erros inteligentes** | Relatório no Bloco de Notas, sugestão do próximo servidor e download automático de novos servidores NordVPN. |
| **29 idiomas** | O programa fala 29 idiomas. Prima `TAB` no ecrã principal para mudar de idioma. |

<br>

---

## 📋 Do que você precisa

**Windows 10 ou 11** · **[GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA)** (ou [OpenVPN](https://openvpn.net/community-downloads/)) · **uma conta em um provedor VPN** · **permissões de administrador** (o script pede sozinho)

<br>

---

## 📖 Guia

<br>

### 1️⃣ Baixar

Clique em **Baixar GHOST-NET**. Mova o **GhostNet.exe** para uma pasta própria, por exemplo `C:\GHOST-NET`, porque o script salva configurações e logins ao lado dele.

<br>

### 2️⃣ Executar

Clique duas vezes em **GhostNet.exe** e clique em **Sim** quando o Windows pedir permissão. Se o Windows mostrar um aviso: **Mais informações** → **Executar assim mesmo**. No primeiro arranque, escolha o seu idioma.

<img src="../screenshots/language-select.png" alt="29 idiomas" width="100%">

📸 **29 idiomas.** O programa fala 29 idiomas. Prima `TAB` no ecrã principal para mudar de idioma.

<br>

### 3️⃣ Escolher o país

Digite um código de país e pressione **Enter**, por exemplo `pl`, `de` ou `us`. Troque de provedor com as setas ou com um número de `1` a `19`.

<br>

### 4️⃣ Escolher o servidor

Digite o nome do servidor da lista, ou só o começo, por exemplo `pl1273`, e pressione **Enter**.

<img src="../screenshots/server-ping.png" alt="Lista de servidores com ping" width="100%">

📸 **Lista de servidores.** Cada servidor mostra o ping entre colchetes, o tempo de resposta: quanto menos `ms`, mais rápido. `udp` costuma ser mais rápido, `tcp` passa melhor por bloqueios. Embaixo você digita o servidor escolhido.

<br>

### 5️⃣ Digite seu login (só na primeira vez)

O script pede seu usuário e senha do OpenVPN e diz onde encontrá-los. NordVPN e Surfshark usam *Service credentials* separadas, não o e-mail e a senha da sua conta.

<img src="../screenshots/login.png" alt="Primeiro login" width="100%">

📸 **Primeiro login.** O script mostra para qual provedor é o login e onde encontrá-lo. A senha fica oculta com asteriscos. O login é salvo uma vez e você não precisa digitá-lo de novo.

<br>

### 6️⃣ Pronto

<img src="../screenshots/connected.png" alt="Tela de conexão" width="100%">

📸 **Conectado.** `NODE_IP` é o seu novo IP que os sites veem. `PING` é a velocidade do túnel, `ENCRYPTION` a criptografia, e `KILL_SWITCH` mostra se a internet fora da VPN está bloqueada. `LOCATION` e `PROVIDER` são a cidade e a empresa do servidor. Embaixo: `1` speedtest, `2` desconectar, `3` kill switch.

<br>

---

## ⌨️ Comandos

| Digite | O que faz |
|---|---|
| `pl`, `de`, `us`… | servidores nesse país |
| `1` … `19` | trocar de provedor VPN |
| `TAB` | mudar de idioma |
| `ks` | ligar ou desligar o kill switch |
| `fs` | tela cheia ou janela |
| `Alt+C` | desconectar a VPN (funciona em todo lugar) |
| `1` / `2` / `3` quando conectado | speedtest / desconectar / kill switch |

<br>

---

## 🌍 Provedores

`NordVPN` (na lista como **OpenVPN**) · `ProtonVPN` · `ExpressVPN` · `PrivadoVPN` · `Surfshark` · `AirVPN` · `CyberGhost` · `PIA VPN` · `IPVanish` · `OVPN.com` · `Mullvad VPN` · `PureVPN` · `VyprVPN` · `IVPN` · `PrivateVPN` · `Perfect Privacy` · `HMA VPN` · `FastVPN` · `TorGuard`

O GHOST-NET não vende VPN: você usa sua própria conta. Adicione os arquivos de servidores no GhostVPN.

<br>

---

## 🆘 Algo não funciona?

| O que vejo | O que fazer |
|---|---|
| **OpenVPN**: não instalado | Instale o [GhostVPN](https://github.com/MRGREGOR85/GhostVPN-BETA) ou o [OpenVPN](https://openvpn.net/community-downloads/). |
| **.ovpn**: sem arquivos de servidor | Adicione os servidores desse provedor no GhostVPN ou escolha outro provedor. |
| **AUTH_FAILED** | Escolha `1` para tentar o próximo servidor. Se nenhum funcionar, escolha `2` e digite seu login de novo. |
| **TUNNEL FAILED** | Leia o relatório no Bloco de Notas. Escolha outro servidor. |
| Sem internet depois de fechar a janela | Abra o script e escolha **REMOVER BLOQUEIO**, ou digite `ks`. |

> 🔒 Os logins ficam só no seu computador, na pasta ao lado do script. Não entregue essa pasta a ninguém.

<br>

---

## 📜 Licença

### Somente para uso privado e doméstico. O GHOST-NET pertence exclusivamente ao seu autor, MRGREGOR85.

**Não é permitido** vendê-lo, dá-lo ou enviá-lo a outras pessoas, publicá-lo em outros sites, fóruns ou Discord, usá-lo em empresas, modificá-lo ou copiar seu código. Cada pessoa baixa sua própria cópia nesta página. Texto completo: [LICENSE](../LICENSE).

<br>

---

## 👨‍💻 Autor

### [MRGREGOR85](https://github.com/MRGREGOR85)

[**GhostVPN**](https://github.com/MRGREGOR85/GhostVPN-BETA) · [**WG Installing**](https://github.com/MRGREGOR85/WG-INSTALLING-BETA) · [**CMD HELP**](https://github.com/MRGREGOR85/Windows-10-11-CMD-HELP-GUI-BETA)

### Se o GHOST-NET te ajuda, deixe uma ⭐

</div>
