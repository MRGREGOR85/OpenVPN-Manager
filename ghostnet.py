# [ GHOST-NET ] VPN MANAGER PRO // FULL GITHUB EDITION - wersja Python
# Autor: MRGREGOR85
# Copyright (c) 2026 MRGREGOR85. Wszelkie prawa zastrzezone - tylko do prywatnego uzytku,
# bez kopiowania, zmieniania i udostepniania dalej. Pelny tekst w pliku LICENSE.
#
# Serwery czytane z folderow GhostVPN: C:\Program Files\GhostVPN\<dostawca>_config
# Na ekranie krajow wpisz kod kraju albo numer dostawcy z listy na dole.
# Uzywa tych samych plikow co wersja .bat (Login.txt, loginy, bledy, killswitch*.txt, pelny_ekran.txt).
# Jezyki: PL i EN w slowniku TXT ponizej, pozostale w jezyki.py (komenda "lang", wybor w jezyk.txt).
# Tylko biblioteka standardowa Pythona - mozna spakowac do .exe (zbuduj_exe.bat).

import concurrent.futures
import ctypes
import datetime
import fnmatch
import json
import os
import random
import re
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.request
import zipfile
from ctypes import wintypes

from jezyki import HINTS, JEZYKI, TR

# ===================================== SCIEZKI I USTAWIENIA =====================================

if getattr(sys, 'frozen', False):
    WORK_DIR = os.path.dirname(sys.executable)
else:
    WORK_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP = tempfile.gettempdir()
GHOST_DIR = r'C:\Program Files\GhostVPN'
LOGIN_DIR = os.path.join(WORK_DIR, 'loginy')
ERR_DIR = os.path.join(WORK_DIR, 'bledy')
OVPN_LOG = os.path.join(TEMP, 'ghost_ovpn.log')
RUN_CFG = os.path.join(TEMP, 'ghost_run.ovpn')
TEST_URL = 'https://nbg1-speed.hetzner.com/1GB.bin'
# Pingi sa rownolegle, wiec mozna sprawdzic duzo wiecej serwerow niz w wersji .bat
PING_LIMIT = 300
WIN_W, WIN_H = 1280, 720
WIN_FILE = os.path.join(WORK_DIR, 'pelny_ekran.txt')
# Jezyk: jezyk.txt = kod jezyka, np. pl / en / de (komenda "lang"); gdy pliku brak, program pyta przy pierwszym starcie
LANG_FILE = os.path.join(WORK_DIR, 'jezyk.txt')
# Kill switch: killswitch.txt = 1/0 (wpisz "ks" na ekranie glownym),
# killswitch_backup.txt istnieje = blokada w zaporze jest teraz aktywna (trzyma stare ustawienia zapory)
KS_FILE = os.path.join(WORK_DIR, 'killswitch.txt')
KS_BACKUP = os.path.join(WORK_DIR, 'killswitch_backup.txt')
# 1 = przy aktywnej blokadzie siec lokalna (drukarka, router, NAS) dalej dziala
KS_LAN = '1'

# OpenVPN z GhostVPN, a gdy go brak - zwykla instalacja OpenVPN
BIN_DIR = os.path.join(GHOST_DIR, 'bin')
if not os.path.exists(os.path.join(BIN_DIR, 'openvpn.exe')):
    BIN_DIR = r'C:\Program Files\OpenVPN\bin'
OPENVPN_EXE = os.path.join(BIN_DIR, 'openvpn.exe')

# ===================================== JEZYKI =====================================

LANG = 'pl'

# klucz: (polski, angielski); {nazwy} wypelnia t(klucz, nazwa=...).
# Inne jezyki: TR[kod][klucz] w jezyki.py - brakujacy napis = angielski.
TXT = {
    # ekran glowny
    'locations': ('[ TERMINAL: DOSTEPNE LOKALIZACJE ]', '[ TERMINAL: AVAILABLE LOCATIONS ]'),
    'codes': ('[BAZA KODOW KRAJOW]', '[COUNTRY CODE DATABASE]'),
    'ks_line': ('  KILL SWITCH: {s}', '  KILL SWITCH: {s}'),
    'cmds': ('  KOMENDY:  [ks = kill switch wl/wyl]   [fs = pelny ekran / okno]   [lang = jezyk]   [ALT+C = rozlacz]',
             '  COMMANDS:  [ks = kill switch on/off]   [fs = full screen / window]   [lang = language]   [ALT+C = disconnect]'),
    'ks_active': ('AKTYWNY - internet tylko przez VPN', 'ACTIVE - internet only through VPN'),
    'ks_armed': ('WLACZONY - zablokuje internet poza VPN po polaczeniu', 'ON - will block internet outside VPN after connecting'),
    'ks_off': ('WYLACZONY', 'OFF'),
    'prompt': ('  WPISZ NAZWE: ', '  ENTER NAME: '),
    'lang_line': ('  JEZYK / LANGUAGE: {n}   [TAB = zmiana]', '  LANGUAGE: {n}   [TAB = change]'),
    'no_files': ('  [!] BLAD: Nie znaleziono plikow .ovpn w folderze {d}', '  [!] ERROR: No .ovpn files found in folder {d}'),
    'no_openvpn': ('  [!] BLAD: OpenVPN nie zainstalowany w {d}', '  [!] ERROR: OpenVPN is not installed in {d}'),
    'pause': ('  Nacisnij dowolny klawisz, aby kontynuowac . . .', '  Press any key to continue . . .'),
    'lang_pick': ('  WYBIERZ JEZYK / CHOOSE LANGUAGE', '  WYBIERZ JEZYK / CHOOSE LANGUAGE'),
    # lista serwerow
    'nodes': ('    DOSTEPNE NODES DLA: {k} [ ANALYZING LATENCY... ]', '    AVAILABLE NODES FOR: {k} [ ANALYZING LATENCY... ]'),
    'no_servers': ('  [!] Nie znaleziono serwerow dla: {k}', '  [!] No servers found for: {k}'),
    'no_servers2': ('      Sprawdz, czy kod jest dokladnie taki jak na liscie krajow, np. akl - litera L, a nie cyfra 1.',
                    '      Check that the code matches the country list exactly, e.g. akl - letter L, not digit 1.'),
    'no_servers3': ('      Powrot do listy krajow za 5 sekund...', '      Back to the country list in 5 seconds...'),
    'no_server': ('  [!] Nie ma serwera: {p} - wpisz nazwe z listy powyzej, wystarczy poczatek, np. af1 albo pl128',
                  '  [!] No such server: {p} - type a name from the list above, the beginning is enough, e.g. af1 or pl128'),
    # login
    'no_login': ('  Brak pliku z loginem: {f}', '  Login file not found: {f}'),
    'login_for': ('  Podaj dane do swojego dostawcy VPN: {p}', '  Enter the credentials for your VPN provider: {p}'),
    'login': ('  LOGIN: ', '  USERNAME: '),
    'password': ('  HASLO: ', '  PASSWORD: '),
    'login_saved': ('  [+] Plik z loginem utworzony lokalnie.', '  [+] Login file created locally.'),
    # kill switch
    'ks_disabling': ('  [#] WYLACZAM KILL SWITCH...', '  [#] DISABLING KILL SWITCH...'),
    'ks_enabled': ('  [#] KILL SWITCH WLACZONY - zablokuje internet poza VPN po kazdym polaczeniu.',
                   '  [#] KILL SWITCH ON - it will block internet outside VPN after every connection.'),
    'ks_later': ('  [#] VPN nie jest polaczony - blokada wlaczy sie po nastepnym polaczeniu.',
                 '  [#] VPN is not connected - the block will turn on after the next connection.'),
    'ks_enabling': ('  [#] WLACZAM KILL SWITCH...', '  [#] ENABLING KILL SWITCH...'),
    # komunikaty kill switcha wypisywane przez PowerShell ({0} {1} wypelnia PowerShell)
    'ksps_prep': ('  [#] KILL SWITCH: przepuszczam serwer VPN ({0}).', '  [#] KILL SWITCH: allowing the VPN server ({0}).'),
    'ksps_look': ('  [#] KILL SWITCH: szukam karty tunelu...', '  [#] KILL SWITCH: looking for the tunnel adapter...'),
    'ksps_notun': ('  [!] KILL SWITCH: nie znaleziono karty tunelu OpenVPN - blokada NIE wlaczona.',
                   '  [!] KILL SWITCH: OpenVPN tunnel adapter not found - block NOT enabled.'),
    'ksps_active': ('  [+] KILL SWITCH AKTYWNY - internet tylko przez: {0} / serwer: {1}',
                    '  [+] KILL SWITCH ACTIVE - internet only through: {0} / server: {1}'),
    'ksps_dnsoff': ('  [#] KILL SWITCH: DNS z laczenia zamkniety.', '  [#] KILL SWITCH: connection DNS closed.'),
    'ksps_off': ('  [+] KILL SWITCH WYLACZONY - zapora przywrocona.', '  [+] KILL SWITCH OFF - firewall restored.'),
    'ksps_err': ('  [!] KILL SWITCH: BLAD ZAPORY - {0}', '  [!] KILL SWITCH: FIREWALL ERROR - {0}'),
    'ks_no_tun': ('  [!] KILL SWITCH NIE WLACZONY - nie znaleziono karty tunelu OpenVPN.',
                  '  [!] KILL SWITCH NOT ENABLED - OpenVPN tunnel adapter not found.'),
    'ks_fw_err': ('  [!] KILL SWITCH NIE WLACZONY - zapora Windows zglosila blad (komunikat powyzej).',
                  '  [!] KILL SWITCH NOT ENABLED - Windows Firewall reported an error (message above).'),
    # start
    'still_on': ('    [!] VPN JEST NADAL POLACZONY // OPENVPN DZIALA W TLE', '    [!] VPN IS STILL CONNECTED // OPENVPN IS RUNNING IN THE BACKGROUND'),
    'still_on2': ('  To moze byc polaczenie z poprzedniego uruchomienia programu albo z GhostVPN GUI.',
                  '  This may be a connection from a previous run of the program or from the GhostVPN GUI.'),
    'disconnect': ('  [1] ROZLACZ', '  [1] DISCONNECT'),
    'keep': ('  [2] ZOSTAW POLACZONY', '  [2] STAY CONNECTED'),
    'ks_stuck': ('    [!] KILL SWITCH BLOKUJE INTERNET // VPN NIE JEST POLACZONY', '    [!] KILL SWITCH IS BLOCKING THE INTERNET // VPN IS NOT CONNECTED'),
    'ks_stuck2': ('  Zapora przepuszcza tylko ruch przez tunel VPN, a tunel nie dziala.',
                  '  The firewall only lets traffic through the VPN tunnel, and the tunnel is down.'),
    'ks_unblock': ('  [1] WYLACZ BLOKADE (INTERNET BEZ VPN)', '  [1] REMOVE THE BLOCK (INTERNET WITHOUT VPN)'),
    'ks_keep': ('  [2] ZOSTAW - polacze sie z serwerem', '  [2] KEEP IT - I will connect to a server'),
    # polaczenie
    'speed_done': ('  [+] TEST COMPLETED. SREDNIA PREDKOSC: {s:.1f} Mbit/s ({mb:.0f} MB w {t:.0f} s)',
                   '  [+] TEST COMPLETED. AVERAGE SPEED: {s:.1f} Mbit/s ({mb:.0f} MB in {t:.0f} s)'),
    'speed_fail': ('  [!] TEST NIEUDANY - brak odpowiedzi serwera testowego ({e}).', '  [!] TEST FAILED - no response from the test server ({e}).'),
    'altc': ('  [ALT+C] SZYBKIE ROZLACZENIE (DZIALA TEZ NA EKRANIE GLOWNYM)', '  [ALT+C] QUICK DISCONNECT (ALSO WORKS ON THE MAIN SCREEN)'),
    'unknown': ('NIEZNANY', 'UNKNOWN'),
    # bledy polaczenia
    'tunnel_lost': ('    [!] TUNEL ZERWANY // OPENVPN SIE ZAMKNAL // {s}', '    [!] TUNNEL DROPPED // OPENVPN HAS CLOSED // {s}'),
    'last_log': ('  Ostatnie linie logu OpenVPN:', '  Last lines of the OpenVPN log:'),
    'ks_holds': ('  [#] KILL SWITCH blokuje internet, dopoki VPN sie nie polaczy - ruch poza tunelem jest zablokowany.',
                 '  [#] KILL SWITCH is blocking the internet until the VPN reconnects - traffic outside the tunnel is blocked.'),
    'reconnect': ('  [1] POLACZ PONOWNIE Z {s}', '  [1] RECONNECT TO {s}'),
    'ks_unblock2': ('  [2] WYLACZ BLOKADE (INTERNET BEZ VPN)', '  [2] REMOVE THE BLOCK (INTERNET WITHOUT VPN)'),
    'back_enter': ('  [ENTER] POWROT DO LISTY KRAJOW', '  [ENTER] BACK TO THE COUNTRY LIST'),
    'why_auth': ('SERWER ODRZUCIL LOGOWANIE - AUTH_FAILED', 'SERVER REJECTED THE LOGIN - AUTH_FAILED'),
    'why_dead': ('OPENVPN SIE ZAMKNAL - SPRAWDZ LOG PONIZEJ', 'OPENVPN HAS CLOSED - CHECK THE LOG BELOW'),
    'why_timeout': ('SERWER NIE ODPOWIADA PRZEZ 30 SEKUND', 'SERVER DID NOT RESPOND FOR 30 SECONDS'),
    'auth_fail': ('    [!] AUTH_FAILED // SERWER {s} ODRZUCIL LOGOWANIE', '    [!] AUTH_FAILED // SERVER {s} REJECTED THE LOGIN'),
    'auth_fail2': ('  Jesli na innych serwerach sie laczysz, haslo jest dobre - ten serwer jest dla Ciebie zablokowany.',
                   '  If other servers connect, your password is fine - this server is blocked for you.'),
    'auth_fail3': ('  Jesli zaden serwer nie dziala, sprawdz haslo. {h}', '  If no server works, check your password. {h}'),
    'next_srv': ('  [1] POLACZ Z NASTEPNYM SERWEREM: {s}', '  [1] CONNECT TO THE NEXT SERVER: {s}'),
    'no_next': ('  [1] BRAK INNEGO SERWERA W TYM KRAJU', '  [1] NO OTHER SERVER IN THIS COUNTRY'),
    'relogin': ('  [2] WPISZ LOGIN I HASLO PONOWNIE', '  [2] ENTER USERNAME AND PASSWORD AGAIN'),
    'back_list': ('  [3] POWROT DO LISTY SERWEROW', '  [3] BACK TO THE SERVER LIST'),
    'report': ('  [#] Raport bledu zapisany: {f}', '  [#] Error report saved: {f}'),
    'stale': ('  [!] Pliki serwerow {p} sa przestarzale - instrukcja w pliku: WYMIEN_SERWERY_{i}.txt',
              '  [!] {p} server files are outdated - instructions in file: WYMIEN_SERWERY_{i}.txt'),
    'ks_blocks': ('  [#] KILL SWITCH blokuje internet bez VPN - wpisz ks na ekranie glownym, zeby go wylaczyc.',
                  '  [#] KILL SWITCH is blocking internet without VPN - type ks on the main screen to turn it off.'),
    # NordVPN
    'nord_check': ('  [#] SPRAWDZAM, CZY SERWER {s} JESZCZE ISTNIEJE U NORDVPN...', '  [#] CHECKING WHETHER SERVER {s} STILL EXISTS AT NORDVPN...'),
    'nord_ok': ('  [+] Serwer istnieje - pliki NordVPN sa aktualne.', '  [+] The server exists - NordVPN files are up to date.'),
    'nord_gone': ('  [!] Serwer {h} nie istnieje - NordVPN go wylaczyl.', '  [!] Server {h} does not exist - NordVPN has shut it down.'),
    'nord_dl': ('  [#] POBIERAM AKTUALNE SERWERY NORDVPN (ok. 75 MB)...', '  [#] DOWNLOADING CURRENT NORDVPN SERVERS (approx. 75 MB)...'),
    'nord_unzip': ('  [#] ROZPAKOWUJE...', '  [#] UNPACKING...'),
    'nord_few': ('Za malo plikow w paczce: {n}', 'Too few files in the package: {n}'),
    'nord_swap': ('  [#] PODMIENIAM PLIKI W {d} ...', '  [#] REPLACING FILES IN {d} ...'),
    'nord_count': ('  [+] Gotowe: {n} plikow serwerow NordVPN.', '  [+] Done: {n} NordVPN server files.'),
    'nord_fail': ('  [!] Nie udalo sie pobrac serwerow NordVPN ({e}) - instrukcja recznej wymiany w pliku WYMIEN_SERWERY_OPENVPN.txt',
                  '  [!] Could not download NordVPN servers ({e}) - manual replacement instructions in WYMIEN_SERWERY_OPENVPN.txt'),
    'nord_ks': ('      Kill switch blokuje pobieranie - wylacz go (ks) i polacz jeszcze raz.',
                '      The kill switch is blocking the download - turn it off (ks) and connect again.'),
    'nord_done': ('  [+] Serwery NordVPN zaktualizowane. Wybierz kraj i serwer jeszcze raz.',
                  '  [+] NordVPN servers updated. Choose the country and server again.'),
    # raport bledu (plik)
    'rep_title': ('===================== GHOST-NET // RAPORT BLEDU POLACZENIA =====================',
                  '===================== GHOST-NET // CONNECTION ERROR REPORT ====================='),
    'rep_head': ('DATA:      {d}\nPOWOD:     {w}\nDOSTAWCA:  {p}\nSERWER:    {s}\nFOLDER:    {f}\nOPENVPN:   {o}\n',
                 'DATE:      {d}\nREASON:    {w}\nPROVIDER:  {p}\nSERVER:    {s}\nFOLDER:    {f}\nOPENVPN:   {o}\n'),
    'rep_log': ('===================== PELNY LOG OPENVPN =====================', '===================== FULL OPENVPN LOG ====================='),
    'rep_nolog': ('Brak logu - OpenVPN sie nie uruchomil.\n', 'No log - OpenVPN did not start.\n'),
    # plik WYMIEN_SERWERY
    'st_title': ('===================== GHOST-NET // TRZEBA WYMIENIC PLIKI SERWEROW =====================',
                 '===================== GHOST-NET // SERVER FILES NEED TO BE REPLACED ====================='),
    'st_body': ('DOSTAWCA:  {p}\nSERWER:    {s} - adres {h} juz nie istnieje\nDATA:      {d}\n\n'
                'Pliki serwerow tego dostawcy sa przestarzale - dostawca wylaczyl stare serwery.\n\n'
                'CO ZROBIC:\n'
                '1. Pobierz aktualne pliki OpenVPN: {u}\n'
                '2. Usun stare pliki .ovpn z folderu: {f}\n'
                '3. Wrzuc tam nowe pliki .ovpn bez podfolderow, razem z plikami .crt i .key, jesli sa w paczce.\n'
                '4. Uruchom program ponownie - lista krajow sama sie odswiezy.\n',
                'PROVIDER:  {p}\nSERVER:    {s} - address {h} no longer exists\nDATE:      {d}\n\n'
                'The server files of this provider are outdated - the provider has shut down the old servers.\n\n'
                'WHAT TO DO:\n'
                '1. Download the current OpenVPN files: {u}\n'
                '2. Delete the old .ovpn files from the folder: {f}\n'
                '3. Put the new .ovpn files there without subfolders, together with .crt and .key files if included.\n'
                '4. Start the program again - the country list will refresh itself.\n'),
}


def t(key, **kw):
    if LANG == 'pl':
        s = TXT[key][0]
    else:
        s = TR.get(LANG, {}).get(key) or TXT[key][1]
    return s.format(**kw) if kw else s


# LISTA DOSTAWCOW (te same co w GhostVPN GUI): ID, NAZWA, FOLDER, TRYB, LOGIN, PODPOWIEDZ (PL, EN), SKAD POBRAC SERWERY
# TRYB: CC2 = kod kraju na poczatku nazwy pliku, TOK2 = kod kraju po pierwszym "-", FIRST = pierwszy czlon nazwy
# LOGIN: True = pyta o login i haslo, False = klucze sa w pliku .ovpn
PROVIDERS = [
    ('OPENVPN', 'OpenVPN', 'config', 'CC2', True,
     ('NordVPN: dane Service credentials z panelu Nord Account, nie e-mail i haslo do konta.',
      'NordVPN: Service credentials from the Nord Account dashboard, not your account e-mail and password.'),
     'https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip'),
    ('PROTONVPN', 'ProtonVPN', 'proton_config', 'CC2', True,
     ('ProtonVPN: OpenVPN / IKEv2 username i haslo z panelu account.proton.me - Downloads.',
      'ProtonVPN: OpenVPN / IKEv2 username and password from account.proton.me - Downloads.'),
     'account.proton.me - Downloads - OpenVPN configuration files - Windows, UDP'),
    ('EXPRESSVPN', 'ExpressVPN', 'express_config', 'FIRST', True,
     ('ExpressVPN: username i password z sekcji Manual configuration na stronie ExpressVPN.',
      'ExpressVPN: username and password from the Manual configuration section on the ExpressVPN website.'),
     'www.expressvpn.com/setup - Manual configuration - OpenVPN'),
    ('PRIVADOVPN', 'PrivadoVPN', 'privado_config', 'FIRST', True,
     ('PrivadoVPN: login i haslo do konta PrivadoVPN.', 'PrivadoVPN: your PrivadoVPN account username and password.'),
     'https://utils.privadovpn.com/share/udp_tcp.zip'),
    ('SURFSHARK', 'Surfshark', 'surfshark_config', 'CC2', True,
     ('Surfshark: Service credentials z panelu Surfshark - Manual setup.',
      'Surfshark: Service credentials from the Surfshark dashboard - Manual setup.'),
     'my.surfshark.com - VPN - Manual setup - OpenVPN - Locations - Download'),
    ('AIRVPN', 'AirVPN', 'airvpn_config', 'FIRST', False,
     ('AirVPN: klucze sa w pliku .ovpn, login nie jest potrzebny.', 'AirVPN: the keys are in the .ovpn file, no login needed.'),
     'airvpn.org - Client Area - Config Generator - OpenVPN'),
    ('CYBERGHOST', 'CyberGhost', 'cyberghost_config', 'FIRST', True,
     ('CyberGhost: username i password z panelu CyberGhost - Configure device - OpenVPN.',
      'CyberGhost: username and password from the CyberGhost dashboard - Configure device - OpenVPN.'),
     'my.cyberghostvpn.com - VPN - Configure device - OpenVPN - Download'),
    ('PIA', 'PIA VPN', 'pia_config', 'FIRST', True,
     ('PIA: login konta w formie p1234567 i haslo do konta.', 'PIA: account username in the form p1234567 and account password.'),
     'https://www.privateinternetaccess.com/openvpn/openvpn.zip'),
    ('IPVANISH', 'IPVanish', 'ipvanish_config', 'TOK2', True,
     ('IPVanish: e-mail i haslo do konta IPVanish.', 'IPVanish: your IPVanish account e-mail and password.'),
     'https://configs.ipvanish.com/configs/configs.zip'),
    ('OVPNCOM', 'OVPN.com', 'ovpncom_config', 'CC2', True,
     ('OVPN.com: login i haslo do konta OVPN.', 'OVPN.com: your OVPN account username and password.'),
     'www.ovpn.com - Guides - OpenVPN + ovpn-ca.crt, ovpn-tls.key'),
    ('MULLVAD', 'Mullvad VPN', 'mullvad_config', 'FIRST', True,
     ('Mullvad: LOGIN = numer konta, HASLO = m', 'Mullvad: USERNAME = account number, PASSWORD = m'),
     'mullvad.net/account - OpenVPN configuration file generator'),
    ('PUREVPN', 'PureVPN', 'purevpn_config', 'FIRST', True,
     ('PureVPN: VPN username typu purevpn0s... i haslo z panelu PureVPN Member Area.',
      'PureVPN: VPN username like purevpn0s... and password from the PureVPN Member Area.'),
     'https://d11a57lttb2ffq.cloudfront.net/heartbleed/router/Recommended-CA2.zip'),
    ('VYPRVPN', 'VyprVPN', 'vyprvpn_config', 'FIRST', True,
     ('VyprVPN: e-mail i haslo do konta VyprVPN.', 'VyprVPN: your VyprVPN account e-mail and password.'),
     'https://support.vyprvpn.com/hc/article_attachments/46761120489229'),
    ('IVPN', 'IVPN', 'ivpn_config', 'FIRST', True,
     ('IVPN: LOGIN = ID konta i-XXXX-XXXX-XXXX, HASLO = dowolne, np. ivpn',
      'IVPN: USERNAME = account ID i-XXXX-XXXX-XXXX, PASSWORD = anything, e.g. ivpn'),
     'https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip'),
    ('PRIVATEVPN', 'PrivateVPN', 'privatevpn_config', 'FIRST', True,
     ('PrivateVPN: login i haslo do konta PrivateVPN.', 'PrivateVPN: your PrivateVPN account username and password.'),
     'privatevpn.com - Client area - OpenVPN configuration files'),
    ('PERFECTPRIVACY', 'Perfect Privacy', 'perfectprivacy_config', 'FIRST', True,
     ('Perfect Privacy: login i haslo do konta Perfect Privacy.', 'Perfect Privacy: your Perfect Privacy account username and password.'),
     'www.perfect-privacy.com - Download - OpenVPN config files'),
    ('HMA', 'HMA VPN', 'hma_config', 'FIRST', True,
     ('HMA: username i password OpenVPN z panelu konta HMA.', 'HMA: OpenVPN username and password from the HMA account dashboard.'),
     'www.hidemyass.com - Account - OpenVPN config files'),
    ('FASTVPN', 'FastVPN', 'fastvpn_config', 'FIRST', True,
     ('FastVPN: login i haslo do FastVPN z panelu Namecheap.', 'FastVPN: FastVPN username and password from the Namecheap dashboard.'),
     'https://vpn.ncapi.io/groupedServerList.zip'),
    ('TORGUARD', 'TorGuard', 'torguard_config', 'FIRST', True,
     ('TorGuard: VPN username i password z panelu TorGuard - Services, nie dane do strony.',
      'TorGuard: VPN username and password from the TorGuard dashboard - Services, not your website login.'),
     'https://torguard.net/tgconf.php?action=vpn-openvpnconfig'),
]

# PELNA BAZA KRAJOW
COUNTRIES = {
    'af': 'Afghanistan', 'al': 'Albania', 'dz': 'Algeria', 'ad': 'Andorra', 'ao': 'Angola',
    'ar': 'Argentina', 'am': 'Armenia', 'au': 'Australia', 'at': 'Austria', 'az': 'Azerbaijan',
    'bs': 'Bahamas', 'bh': 'Bahrain', 'bd': 'Bangladesh', 'be': 'Belgium', 'bz': 'Belize',
    'bm': 'Bermuda', 'bt': 'Bhutan', 'bo': 'Bolivia', 'ba': 'Bosnia and Herzegovina', 'br': 'Brazil',
    'bn': 'Brunei', 'bg': 'Bulgaria', 'kh': 'Cambodia', 'ca': 'Canada', 'ky': 'Cayman Islands',
    'cl': 'Chile', 'co': 'Colombia', 'km': 'Comoros', 'cr': 'Costa Rica', 'hr': 'Croatia',
    'cy': 'Cyprus', 'cz': 'Czech Republic', 'dk': 'Denmark', 'do': 'Dominican Republic', 'ec': 'Ecuador',
    'eg': 'Egypt', 'sv': 'El Salvador', 'ee': 'Estonia', 'et': 'Ethiopia', 'fi': 'Finland',
    'fr': 'France', 'ge': 'Georgia', 'de': 'Germany', 'gh': 'Ghana', 'gr': 'Greece',
    'gl': 'Greenland', 'gu': 'Guam', 'gt': 'Guatemala', 'hn': 'Honduras', 'hk': 'Hong Kong',
    'hu': 'Hungary', 'is': 'Iceland', 'in': 'India', 'id': 'Indonesia', 'iq': 'Iraq',
    'ie': 'Ireland', 'im': 'Isle of Man', 'il': 'Israel', 'it': 'Italy', 'jm': 'Jamaica',
    'jp': 'Japan', 'je': 'Jersey', 'jo': 'Jordan', 'kz': 'Kazakhstan', 'ke': 'Kenya',
    'kw': 'Kuwait', 'la': 'Laos', 'lv': 'Latvia', 'lb': 'Lebanon', 'ly': 'Libya',
    'li': 'Liechtenstein', 'lt': 'Lithuania', 'lu': 'Luxembourg', 'my': 'Malaysia', 'mt': 'Malta',
    'mr': 'Mauritania', 'mu': 'Mauritius', 'mx': 'Mexico', 'md': 'Moldova', 'mc': 'Monaco',
    'mn': 'Mongolia', 'me': 'Montenegro', 'ma': 'Morocco', 'mz': 'Mozambique', 'mm': 'Myanmar',
    'np': 'Nepal', 'nl': 'Netherlands', 'nz': 'New Zealand', 'ng': 'Nigeria', 'mk': 'North Macedonia',
    'no': 'Norway', 'pk': 'Pakistan', 'pa': 'Panama', 'pg': 'Papua New Guinea', 'py': 'Paraguay',
    'pe': 'Peru', 'ph': 'Philippines', 'pl': 'Poland', 'pt': 'Portugal', 'pr': 'Puerto Rico',
    'qa': 'Qatar', 'ro': 'Romania', 'rw': 'Rwanda', 'sn': 'Senegal', 'rs': 'Serbia',
    'sg': 'Singapore', 'sk': 'Slovakia', 'si': 'Slovenia', 'so': 'Somalia', 'za': 'South Africa',
    'kr': 'South Korea', 'es': 'Spain', 'lk': 'Sri Lanka', 'se': 'Sweden', 'ch': 'Switzerland',
    'tw': 'Taiwan', 'tj': 'Tajikistan', 'th': 'Thailand', 'tt': 'Trinidad', 'tn': 'Tunisia',
    'tr': 'Turkey', 'ua': 'Ukraine', 'ae': 'U.A.E.', 'uk': 'United Kingdom', 'gb': 'United Kingdom',
    'us': 'United States', 'uy': 'Uruguay', 'uz': 'Uzbekistan', 've': 'Venezuela', 'vn': 'Vietnam',
    'ht': 'Haiti', 'mo': 'Macau', 'ni': 'Nicaragua', 'sa': 'Saudi Arabia',
}

# Miasta PrivadoVPN (kody lotnisk) - na liscie widac "Warsaw [waw]", wpisuje sie kod
CITIES = {
    'akl': 'Auckland', 'ams': 'Amsterdam', 'arn': 'Stockholm', 'ath': 'Athens', 'atl': 'Atlanta',
    'beg': 'Belgrade', 'ber': 'Berlin', 'bkk': 'Bangkok', 'bom': 'Mumbai', 'bru': 'Brussels',
    'bts': 'Bratislava', 'bud': 'Budapest', 'cdg': 'Paris', 'cgk': 'Jakarta', 'cph': 'Copenhagen',
    'dca': 'Washington', 'den': 'Denver', 'dfw': 'Dallas', 'dtw': 'Detroit', 'dub': 'Dublin',
    'eze': 'Buenos Aires', 'fra': 'Frankfurt', 'gru': 'Sao Paulo', 'hel': 'Helsinki', 'hkg': 'Hong Kong',
    'icn': 'Seoul', 'iev': 'Kyiv', 'ist': 'Istanbul', 'jfk': 'New York', 'jnb': 'Johannesburg',
    'jrs': 'Jerusalem', 'kul': 'Kuala Lumpur', 'lax': 'Los Angeles', 'lhr': 'London', 'lis': 'Lisbon',
    'lju': 'Ljubljana', 'mad': 'Madrid', 'man': 'Manchester', 'mex': 'Mexico City', 'mia': 'Miami',
    'mnl': 'Manila', 'mxp': 'Milan', 'nrt': 'Tokyo', 'ord': 'Chicago', 'osl': 'Oslo',
    'otp': 'Bucharest', 'pdx': 'Portland', 'prg': 'Prague', 'rix': 'Riga', 'rkv': 'Reykjavik',
    'sea': 'Seattle', 'sfo': 'San Francisco', 'sin': 'Singapore', 'sjc': 'San Jose', 'sof': 'Sofia',
    'stl': 'St. Louis', 'svo': 'Moscow', 'syd': 'Sydney', 'tia': 'Tirana', 'tll': 'Tallinn',
    'tsa': 'Taipei', 'vie': 'Vienna', 'waw': 'Warsaw', 'yul': 'Montreal', 'yvr': 'Vancouver',
    'yyz': 'Toronto', 'zrh': 'Zurich',
}

CODES_BLOCK = [
    'af, al, dz, ad, ao, ar, am, au, at, az, bs, bh, bd, be, bz, bm, bt, bo, ba, br,',
    'bn, bg, kh, ca, ky, cl, co, km, cr, hr, cy, cz, dk, do, ec, eg, sv, ee, et, fi,',
    'fr, ge, de, gh, gr, gl, gu, gt, hn, hk, hu, is, in, id, iq, ie, im, il, it, jm,',
    'jp, je, jo, kz, ke, kw, la, lv, lb, ly, li, lt, lu, my, mt, mr, mu, mx, md, mc,',
    'mn, me, ma, mz, mm, np, nl, nz, ng, mk, no, pk, pa, pg, py, pe, ph, pl, pt, pr,',
    'qa, ro, rw, sn, rs, sg, sk, si, so, za, kr, es, lk, se, ch, tw, tj, th, tt, tn,',
    'tr, ua, ae, uk, gb, us, uy, uz, ve, vn, ht, mo, ni, sa.',
]

# Czaszka na ekran po prawej: lewa polowa do srodkowej kolumny wlacznie ("ile spacji|tekst");
# prawa = lustrzane odbicie, wiec czaszka jest zawsze rowna. Znaki u $ " i spacja wygladaja tak samo w lustrze.
SKULL_HALF = [
    '20|uuuu', '16|uu$$$$$$', '13|uu$$$$$$$$$', '12|u$$$$$$$$$$$', '11|u$$$$$$$$$$$$',
    '10|u$$$$$$$$$$$$$', '10|u$$$$$$$$$$$$$', '10|u$$$$$$"   "$$', '10|"$$$$"      u$', '11|$$$u       u$',
    '11|$$$u      u$$', '12|"$$$$uu$$$', '13|"$$$$$$$"', '15|u$$$$$$$u', '16|u$"$"$"$',
    '6|uuu       $$u$ $ $', '4|u$$$$        $$$$$u$', '5|$$$$$uu      "$$$$$', '3|u$$$$$$$$$$$uu    """',
    '3|$$$$"""$$$$$$$$$$uuu', '4|"""      ""$$$$$$$$$', '14|uuuu ""$$$', '5|u$$$uuu$$$$$$$$$uu',
    '5|$$$$$$$$$$""""', '6|"$$$$$"', '8|$$$"',
]


def build_skull():
    rows = []
    for h in SKULL_HALF:
        n, s = h.split('|', 1)
        left = (' ' * int(n) + s).ljust(24)
        rows.append(left + left[:23][::-1])
    return rows


SKULL = build_skull()

# Kill switch na zaporze Windows (ten sam kod PowerShell co w wersji .bat; komunikaty przychodza przetlumaczone
# w zmiennych KS_T_*). KS_ACT:
#   prep   = przed laczeniem przy aktywnej blokadzie: przepusc serwer VPN i na chwile DNS
#   on     = po polaczeniu: zablokuj caly ruch wychodzacy poza tunelem (zapisuje stara zapore do KS_BACKUP)
#   dnsoff = po nieudanym laczeniu: zamknij DNS otwarty przez prep
#   off    = przywroc zapore sprzed wlaczenia i usun reguly
# Kod wyjscia: 0 = OK, 1 = blad zapory, 2 = brak karty tunelu (blokada NIE zostala wlaczona)
KS_PS = r"""
$ErrorActionPreference = 'Stop'
$grp = 'GHOST-NET KillSwitch'
$bak = $env:KS_BACKUP
$p = @{ Group = $grp; Direction = 'Outbound'; Action = 'Allow' }
$log = Join-Path $env:WORK_DIR 'killswitch_log.txt'
function Say([string]$m) {
    Write-Host $m
    try { Add-Content -LiteralPath $log -Encoding UTF8 -Value ('{0} [{1}] {2}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $env:KS_ACT, $m.Trim()) } catch { }
}
function Get-ServerIPs {
    $ips = New-Object System.Collections.Generic.List[string]
    if ($env:SRC_CFG -and (Test-Path -LiteralPath $env:SRC_CFG)) {
        foreach ($m in (Select-String -LiteralPath $env:SRC_CFG -Pattern '^\s*remote\s+(\S+)')) {
            $h = $m.Matches[0].Groups[1].Value; $ip = $null
            if ([Net.IPAddress]::TryParse($h, [ref]$ip)) { $ips.Add($h); continue }
            try { foreach ($a in [Net.Dns]::GetHostAddresses($h)) { $ips.Add($a.IPAddressToString) } } catch { }
        }
    }
    if ($env:OVPN_LOG -and (Test-Path -LiteralPath $env:OVPN_LOG)) {
        foreach ($m in (Select-String -LiteralPath $env:OVPN_LOG -Pattern '\[AF_INET6?\]([0-9A-Fa-f\.:]+):\d+' -AllMatches)) {
            foreach ($x in $m.Matches) { $ip = $null; if ([Net.IPAddress]::TryParse($x.Groups[1].Value, [ref]$ip)) { $ips.Add($x.Groups[1].Value) } }
        }
    }
    @($ips | Select-Object -Unique)
}
function Get-TunnelAliases {
    $a = @(Get-NetAdapter -ErrorAction SilentlyContinue | Where-Object { $_.InterfaceDescription -match 'TAP-Win|Wintun|OpenVPN|Data Channel Offload|ovpn-dco' } | ForEach-Object Name)
    $a += @(Get-NetRoute -DestinationPrefix '0.0.0.0/1', '128.0.0.0/1' -ErrorAction SilentlyContinue | ForEach-Object InterfaceAlias)
    @($a | Where-Object { $_ } | Select-Object -Unique)
}
function Reset-Rules([bool]$withDns) {
    Remove-NetFirewallRule -Group $grp -ErrorAction SilentlyContinue
    New-NetFirewallRule @p -DisplayName 'GHOST-NET KS: OpenVPN' -Program (Join-Path $env:BIN_DIR 'openvpn.exe') | Out-Null
    New-NetFirewallRule @p -DisplayName 'GHOST-NET KS: DHCP' -Protocol UDP -LocalPort 68 -RemotePort 67 | Out-Null
    if ($env:KS_LAN -eq '1') { New-NetFirewallRule @p -DisplayName 'GHOST-NET KS: siec lokalna' -RemoteAddress LocalSubnet | Out-Null }
    if ($withDns) {
        New-NetFirewallRule @p -DisplayName 'GHOST-NET KS: DNS (laczenie)' -Protocol UDP -RemotePort 53 | Out-Null
        New-NetFirewallRule @p -DisplayName 'GHOST-NET KS: DNS (laczenie)' -Protocol TCP -RemotePort 53 | Out-Null
    }
    $ips = Get-ServerIPs
    if ($ips.Count) { New-NetFirewallRule @p -DisplayName 'GHOST-NET KS: serwer VPN' -RemoteAddress $ips | Out-Null }
}
try {
switch ($env:KS_ACT) {
    'prep' {
        if (-not (Test-Path -LiteralPath $bak)) { exit 0 }
        Reset-Rules $true
        Say ($env:KS_T_PREP -f ((Get-ServerIPs) -join ', '))
    }
    'on' {
        Say $env:KS_T_LOOK
        $tun = Get-TunnelAliases
        if (-not $tun.Count) { Say $env:KS_T_NOTUN; exit 2 }
        Reset-Rules $false
        New-NetFirewallRule @p -DisplayName 'GHOST-NET KS: tunel VPN' -InterfaceAlias $tun | Out-Null
        if (-not (Test-Path -LiteralPath $bak)) {
            $lines = foreach ($pr in Get-NetFirewallProfile -All) { '{0}|{1}|{2}' -f $pr.Name, $pr.Enabled, $pr.DefaultOutboundAction }
            [IO.File]::WriteAllLines($bak, [string[]]$lines)
        }
        Set-NetFirewallProfile -All -Enabled True -DefaultOutboundAction Block
        Say ($env:KS_T_ACTIVE -f ($tun -join ', '), ((Get-ServerIPs) -join ', '))
    }
    'dnsoff' {
        Remove-NetFirewallRule -DisplayName 'GHOST-NET KS: DNS*' -ErrorAction SilentlyContinue
        Say $env:KS_T_DNSOFF
    }
    'off' {
        Remove-NetFirewallRule -Group $grp -ErrorAction SilentlyContinue
        if (Test-Path -LiteralPath $bak) {
            foreach ($l in [IO.File]::ReadAllLines($bak)) {
                $x = $l.Split('|')
                if ($x.Count -eq 3) { Set-NetFirewallProfile -Name $x[0] -Enabled $x[1] -DefaultOutboundAction $x[2] }
            }
            [IO.File]::Delete($bak)
        }
        Say $env:KS_T_OFF
    }
}
} catch { Say ($env:KS_T_ERR -f $_.Exception.Message); exit 1 }
exit 0
"""

# ===================================== KONSOLA (WinAPI) =====================================

k32 = ctypes.WinDLL('kernel32', use_last_error=True)
u32 = ctypes.WinDLL('user32', use_last_error=True)
STD_OUT = k32.GetStdHandle(-11)
CREATE_NO_WINDOW = 0x08000000
CREATE_NEW_PROCESS_GROUP = 0x00000200


class COORD(ctypes.Structure):
    _fields_ = [('X', ctypes.c_short), ('Y', ctypes.c_short)]


class SMALL_RECT(ctypes.Structure):
    _fields_ = [('Left', ctypes.c_short), ('Top', ctypes.c_short), ('Right', ctypes.c_short), ('Bottom', ctypes.c_short)]


class CSBI(ctypes.Structure):
    _fields_ = [('dwSize', COORD), ('dwCursorPosition', COORD), ('wAttributes', wintypes.WORD),
                ('srWindow', SMALL_RECT), ('dwMaximumWindowSize', COORD)]


class FONTEX(ctypes.Structure):
    _fields_ = [('cbSize', wintypes.ULONG), ('nFont', wintypes.DWORD), ('dwFontSize', COORD),
                ('FontFamily', wintypes.UINT), ('FontWeight', wintypes.UINT), ('FaceName', wintypes.WCHAR * 32)]


class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_long), ('top', ctypes.c_long), ('right', ctypes.c_long), ('bottom', ctypes.c_long)]


class KEY_EVENT_RECORD(ctypes.Structure):
    _fields_ = [('bKeyDown', wintypes.BOOL), ('wRepeatCount', wintypes.WORD), ('wVirtualKeyCode', wintypes.WORD),
                ('wVirtualScanCode', wintypes.WORD), ('uChar', wintypes.WCHAR), ('dwControlKeyState', wintypes.DWORD)]


class _EVENT(ctypes.Union):
    _fields_ = [('KeyEvent', KEY_EVENT_RECORD), ('_pad', ctypes.c_byte * 16)]


class INPUT_RECORD(ctypes.Structure):
    _fields_ = [('EventType', wintypes.WORD), ('Event', _EVENT)]


STD_IN = k32.GetStdHandle(-10)
k32.GetConsoleWindow.restype = wintypes.HWND
k32.SetConsoleCursorPosition.argtypes = [wintypes.HANDLE, COORD]
k32.SetConsoleScreenBufferSize.argtypes = [wintypes.HANDLE, COORD]
k32.SetConsoleWindowInfo.argtypes = [wintypes.HANDLE, wintypes.BOOL, ctypes.POINTER(SMALL_RECT)]
k32.GetLargestConsoleWindowSize.argtypes = [wintypes.HANDLE]
k32.GetLargestConsoleWindowSize.restype = wintypes.DWORD
u32.GetWindowRect.argtypes = [wintypes.HWND, ctypes.POINTER(RECT)]
u32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, wintypes.UINT]
u32.ShowWindow.argtypes = [wintypes.HWND, ctypes.c_int]

# Kolory ANSI: jasnozielony jak "color 0A", ciemnozielony, ciemnoszary, czerwony, ciemna zielen podpisu
ESC = '\x1b'
C_FG = ESC + '[92m'
C_DARK = ESC + '[32m'
C_GRAY = ESC + '[90m'
C_RED = ESC + '[91m'
C_AUTHOR = ESC + '[38;2;0;110;0m'
C_INV, C_NOINV = ESC + '[7m', ESC + '[27m'
LINE = '=' * 124
LINE_S = '=' * 101


def out(s=''):
    sys.stdout.write(s)
    sys.stdout.flush()


def say(s=''):
    out(s + '\n')


def enable_vt():
    mode = wintypes.DWORD()
    if k32.GetConsoleMode(STD_OUT, ctypes.byref(mode)):
        k32.SetConsoleMode(STD_OUT, mode.value | 0x0004)


def csbi():
    info = CSBI()
    k32.GetConsoleScreenBufferInfo(STD_OUT, ctypes.byref(info))
    return info


def goto(x, y):
    # Pozycja w buforze konsoli (nie tylko w widocznym oknie)
    sys.stdout.flush()
    k32.SetConsoleCursorPosition(STD_OUT, COORD(x, y))


def cursor():
    c = csbi().dwCursorPosition
    return c.X, c.Y


def cls():
    os.system('cls')
    out(C_FG)


def alert(on):
    # Jak "color 0C" / "color 0A" w wersji .bat - caly ekran na czerwono albo zielono
    os.system('color 0C' if on else 'color 0A')
    out(C_RED if on else C_FG)


KEYS = {0x26: 'UP', 0x28: 'DOWN', 0x25: 'LEFT', 0x27: 'RIGHT', 0x0D: 'ENTER', 0x08: 'BACK', 0x1B: 'ESC', 0x09: 'TAB'}


def read_key():
    # Jeden klawisz prosto z konsoli (msvcrt gubi Alta: Alt+C daje samo "c").
    # Zwraca znak albo nazwe: UP/DOWN/LEFT/RIGHT/ENTER/BACK/ESC/ALT_C.
    # Prawy Alt na polskiej klawiaturze to Ctrl+Alt (AltGr+C = "c" z ogonkiem) - to zwykla litera, nie Alt+C.
    rec, n = INPUT_RECORD(), wintypes.DWORD()
    while True:
        k32.ReadConsoleInputW(STD_IN, ctypes.byref(rec), 1, ctypes.byref(n))
        if rec.EventType != 1 or not rec.Event.KeyEvent.bKeyDown:
            continue
        k = rec.Event.KeyEvent
        alt, ctrl = k.dwControlKeyState & 0x3, k.dwControlKeyState & 0xC
        if alt and not ctrl and k.wVirtualKeyCode == 0x43:
            return 'ALT_C'
        if k.wVirtualKeyCode in KEYS:
            return KEYS[k.wVirtualKeyCode]
        if k.uChar == '\x03':
            raise KeyboardInterrupt
        if k.uChar and k.uChar >= ' ':
            return k.uChar


def pause():
    out(t('pause'))
    k32.FlushConsoleInputBuffer(STD_IN)
    rec, n = INPUT_RECORD(), wintypes.DWORD()
    while True:
        k32.ReadConsoleInputW(STD_IN, ctypes.byref(rec), 1, ctypes.byref(n))
        k = rec.Event.KeyEvent
        # sam Shift/Ctrl/Alt nie liczy sie jako klawisz
        if rec.EventType == 1 and k.bKeyDown and k.wVirtualKeyCode not in (0x10, 0x11, 0x12):
            break
    say()


def ask(prompt):
    out(prompt)
    try:
        return input().strip()
    except EOFError:
        return ''


def read_secret(prompt):
    # Haslo z gwiazdkami
    out(prompt)
    s = ''
    while True:
        k = read_key()
        if k == 'ENTER':
            break
        if k == 'BACK':
            if s:
                s = s[:-1]
                out('\b \b')
        elif len(k) == 1:
            s += k
            out('*')
    say()
    return s


def read_line_altc(prompt):
    # Prosty prompt (ekran z czaszka): wpisywanie + ENTER, Alt+C = rozlacz
    out(prompt)
    s = ''
    while True:
        k = read_key()
        if k == 'ALT_C':
            say()
            return 'ALT_C'
        if k == 'ENTER':
            break
        if k == 'BACK':
            if s:
                s = s[:-1]
                out('\b \b')
        elif len(k) == 1:
            s += k
            out(k)
    say()
    return s.strip()


def apply_window(full):
    # Okno WIN_W x WIN_H pikseli na srodku ekranu albo caly ekran; bufor 3000 linii do przewijania
    hwnd = k32.GetConsoleWindow()
    if not hwnd:
        return
    u32.ShowWindow(hwnd, 9)
    gsm = u32.GetSystemMetrics
    w, h = (gsm(61), gsm(62)) if full else (WIN_W, WIN_H)
    f = FONTEX()
    f.cbSize = ctypes.sizeof(FONTEX)
    fw, fh = 8, 16
    if k32.GetCurrentConsoleFontEx(STD_OUT, False, ctypes.byref(f)) and f.dwFontSize.X > 0:
        fw, fh = f.dwFontSize.X, f.dwFontSize.Y
    frame = gsm(32) + gsm(92)
    cols = (w - 2 * frame - gsm(2)) // fw
    rows = (h - gsm(4) - 2 * frame) // fh
    big = k32.GetLargestConsoleWindowSize(STD_OUT)
    maxw, maxh = big & 0xFFFF, (big >> 16) & 0xFFFF
    # Menu ma 125 znakow szerokosci - wezsze okno by je polamalo
    cols = min(max(cols, 125), max(maxw, 125))
    rows = min(max(rows, 30), maxh) if maxh else max(rows, 30)
    win = csbi().srWindow
    curw, curh = win.Right - win.Left + 1, win.Bottom - win.Top + 1
    # Najpierw zmniejszamy okno, bo bufor nie moze byc wezszy niz okno
    k32.SetConsoleWindowInfo(STD_OUT, True, ctypes.byref(SMALL_RECT(0, 0, min(curw, cols) - 1, min(curh, rows) - 1)))
    k32.SetConsoleScreenBufferSize(STD_OUT, COORD(cols, 3000))
    k32.SetConsoleWindowInfo(STD_OUT, True, ctypes.byref(SMALL_RECT(0, 0, cols - 1, rows - 1)))
    if full:
        u32.ShowWindow(hwnd, 3)
    else:
        r = RECT()
        if u32.GetWindowRect(hwnd, ctypes.byref(r)):
            x = max(0, (gsm(0) - (r.right - r.left)) // 2)
            y = max(0, (gsm(1) - (r.bottom - r.top)) // 2)
            u32.SetWindowPos(hwnd, None, x, y, 0, 0, 0x0005)


def draw_art():
    # Ozdoba w wolnym miejscu po prawej (gdy okno jest szersze niz menu): tlo z ciemnoszarych zer i jedynek
    # od pierwszej linii ekranu do dolu okna, na nim ciemnozielona czaszka przy prawej krawedzi.
    # Pelny ekran = czaszka z piszczelami, okno 720p = sama glowa czaszki.
    info = csbi()
    wt, wh = info.srWindow.Top, info.srWindow.Bottom - info.srWindow.Top + 1
    ww = info.srWindow.Right - info.srWindow.Left + 1
    x0 = 125
    aw = ww - 1 - x0
    if aw < 29:
        return
    ox, oy = info.dwCursorPosition.X, info.dwCursorPosition.Y
    skull = SKULL if (aw >= 49 and wh >= 30) else [r[10:37] for r in SKULL[:15]]
    rnd = random.Random()
    out(C_GRAY)
    for y in range(wt + wh):
        goto(x0, y)
        out(''.join(rnd.choice('000111    ') for _ in range(aw)))
    sw = max(len(r.rstrip()) for r in skull)
    sx = x0 + aw - sw - 1
    y0 = wt + max(1, (wh - len(skull)) // 2)
    out(C_DARK)
    for i, row in enumerate(skull):
        s = row.strip()
        if s:
            goto(sx + (len(row) - len(row.lstrip())) - 1, y0 + i)
            out(' ' + s + ' ')
    out(C_FG)
    goto(ox, oy)


# ===================================== SIEC =====================================

class IP_OPTION_INFORMATION(ctypes.Structure):
    _fields_ = [('Ttl', ctypes.c_ubyte), ('Tos', ctypes.c_ubyte), ('Flags', ctypes.c_ubyte),
                ('OptionsSize', ctypes.c_ubyte), ('OptionsData', ctypes.c_void_p)]


class ICMP_ECHO_REPLY(ctypes.Structure):
    _fields_ = [('Address', ctypes.c_ulong), ('Status', ctypes.c_ulong), ('RoundTripTime', ctypes.c_ulong),
                ('DataSize', ctypes.c_ushort), ('Reserved', ctypes.c_ushort), ('Data', ctypes.c_void_p),
                ('Options', IP_OPTION_INFORMATION)]


iphlp = ctypes.WinDLL('iphlpapi')
iphlp.IcmpCreateFile.restype = wintypes.HANDLE
iphlp.IcmpCloseHandle.argtypes = [wintypes.HANDLE]
iphlp.IcmpSendEcho.argtypes = [wintypes.HANDLE, ctypes.c_ulong, ctypes.c_void_p, wintypes.WORD,
                               ctypes.c_void_p, ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD]
iphlp.IcmpSendEcho.restype = wintypes.DWORD


def ping(host, timeout=800):
    # Ping przez Windows ICMP API (bez okienek ping.exe); None = brak odpowiedzi
    try:
        ip = socket.gethostbyname(host)
    except OSError:
        return None
    addr = struct.unpack('<I', socket.inet_aton(ip))[0]
    data = b'GHOST-NET'
    buf = ctypes.create_string_buffer(ctypes.sizeof(ICMP_ECHO_REPLY) + len(data) + 8)
    h = iphlp.IcmpCreateFile()
    try:
        if iphlp.IcmpSendEcho(h, addr, data, len(data), None, buf, len(buf), timeout):
            rep = ICMP_ECHO_REPLY.from_buffer(buf)
            if rep.Status == 0:
                return max(1, rep.RoundTripTime)
    finally:
        iphlp.IcmpCloseHandle(h)
    return None


def http_get(url, timeout=5):
    req = urllib.request.Request(url, headers={'User-Agent': 'GHOST-NET'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def resolves(host):
    try:
        socket.getaddrinfo(host, None)
        return True
    except OSError:
        return False


def is_ip(host):
    try:
        socket.inet_pton(socket.AF_INET6 if ':' in host else socket.AF_INET, host)
        return True
    except OSError:
        return False


def first_remote(path):
    try:
        with open(path, encoding='latin-1') as f:
            for line in f:
                m = re.match(r'\s*remote\s+(\S+)', line, re.I)
                if m:
                    return m.group(1)
    except OSError:
        pass
    return None


def ovpn_running():
    r = subprocess.run(['tasklist', '/fi', 'imagename eq openvpn.exe', '/nh'], capture_output=True,
                       text=True, creationflags=CREATE_NO_WINDOW)
    return 'openvpn.exe' in r.stdout.lower()


def ovpn_kill():
    subprocess.run(['taskkill', '/f', '/im', 'openvpn.exe'], capture_output=True, creationflags=CREATE_NO_WINDOW)


def read_text(path):
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            return f.read()
    except OSError:
        return ''


def log_tail(n=10):
    return read_text(OVPN_LOG).splitlines()[-n:]


def stamp():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


def save_flag(path, on):
    with open(path, 'w') as f:
        f.write('1\n' if on else '0\n')


# ===================================== PROGRAM =====================================

class App:
    def __init__(self):
        self.ks_want = read_text(KS_FILE).strip() == '1'
        self.win_full = read_text(WIN_FILE).strip() == '1'
        self.list_cache = {}
        self.sel = ''
        self.kraj = ''
        self.mask = ''
        self.v = {}
        self.set_provider(1)

    # ---------- dostawca ----------

    def set_provider(self, i):
        pid, name, folder, mode, auth, hint, url = PROVIDERS[i - 1]
        self.cur = i
        self.pid, self.pname, self.pmode, self.pauth, self.hint, self.purl = pid, name, mode, auth, hint, url
        self.pdir = os.path.join(GHOST_DIR, folder)
        # OpenVPN zostaje na starym Login.txt obok programu, reszta w folderze "loginy"
        self.login_file = os.path.join(WORK_DIR, 'Login.txt') if i == 1 else os.path.join(LOGIN_DIR, pid + '.txt')
        self.files = self.ovpn_files()

    @property
    def phint(self):
        if LANG == 'pl':
            return self.hint[0]
        hints = HINTS.get(LANG)
        return hints[self.cur - 1] if hints else self.hint[1]

    def ovpn_files(self):
        try:
            return sorted((e.name for e in os.scandir(self.pdir) if e.is_file() and e.name.lower().endswith('.ovpn')),
                          key=str.lower)
        except OSError:
            return []

    def country_list(self):
        # Lista krajow/miast aktywnego dostawcy (posortowana, bez nieznanych kodow); liczona od nowa,
        # gdy zmieni sie liczba plikow dostawcy
        key = (self.pid, len(self.files))
        if key in self.list_cache:
            return self.list_cache[key]
        seen, names = set(), []
        for fn in self.files:
            full = fn[:-5]
            if self.pmode == 'CC2':
                k = full[:2] if len(full) >= 2 else None
            elif self.pmode == 'TOK2':
                parts = full.split('-')
                k = parts[1] if len(parts) >= 2 else None
            else:
                x = full.replace(' ', '').replace('_-_', '_')
                x = re.sub('_udp', '', x, flags=re.I)
                x = re.sub('_tcp', '', x, flags=re.I)
                k = re.split(r'[.\-]', x)[0]
            if not k or k.lower() in seen:
                continue
            seen.add(k.lower())
            if self.pmode == 'FIRST':
                city = CITIES.get(k.lower())
                n = f'{city} [{k.lower()}]' if city else k
            else:
                n = COUNTRIES.get(k.lower())
            if n:
                names.append(n)
        names.sort(key=str.lower)
        self.list_cache[key] = names
        return names

    def match(self, pattern):
        return [f for f in self.files if fnmatch.fnmatch(f.lower(), pattern.lower())]

    # ---------- kill switch ----------

    def ks_active(self):
        return os.path.exists(KS_BACKUP)

    def ks(self, act):
        env = dict(os.environ, KS_ACT=act, KS_BACKUP=KS_BACKUP, WORK_DIR=WORK_DIR, BIN_DIR=BIN_DIR,
                   KS_LAN=KS_LAN, OVPN_LOG=OVPN_LOG, SRC_CFG=os.path.join(self.pdir, self.sel) if self.sel else '')
        for name in ('prep', 'look', 'notun', 'active', 'dnsoff', 'off', 'err'):
            env['KS_T_' + name.upper()] = t('ksps_' + name)
        r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command', KS_PS], env=env)
        return r.returncode

    def ks_on(self):
        rc = self.ks('on')
        if rc == 0:
            return
        say(t('ks_no_tun') if rc == 2 else t('ks_fw_err'))
        pause()

    def ks_toggle(self, back):
        # Przelaczenie kill switcha z ekranu glownego (ks) albo z ekranu polaczenia [3]
        self.ks_want = not self.ks_want
        save_flag(KS_FILE, self.ks_want)
        cls()
        if not self.ks_want:
            say(t('ks_disabling'))
            if self.ks_active():
                self.ks('off')
        else:
            say(t('ks_enabled'))
            running = ovpn_running()
            with open(os.path.join(WORK_DIR, 'killswitch_log.txt'), 'a', encoding='utf-8') as f:
                f.write(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S} [toggle] on, openvpn={int(running)}\n')
            if running:
                self.ks_on()
            else:
                say(t('ks_later'))
        say()
        pause()
        return back

    # ---------- start programu ----------

    def run(self):
        if ovpn_running():
            self.still_on()
        # Blokada zostala z poprzedniego uruchomienia, a VPN juz nie dziala - internet jest odciety
        if self.ks_active() and not ovpn_running():
            self.ks_stuck()
        state = 'START'
        while state:
            state = getattr(self, 's_' + state)()

    def still_on(self):
        cls()
        alert(True)
        say(LINE_S)
        say(t('still_on'))
        say(LINE_S)
        say()
        say(t('still_on2'))
        say()
        say(t('disconnect'))
        say(t('keep'))
        say()
        choice = ask('  ACTION_REQUIRED: ')
        alert(False)
        if choice == '1':
            ovpn_kill()
            if self.ks_active():
                self.ks('off')

    def ks_stuck(self):
        cls()
        alert(True)
        say(LINE_S)
        say(t('ks_stuck'))
        say(LINE_S)
        say()
        say(t('ks_stuck2'))
        say()
        say(t('ks_unblock'))
        say(t('ks_keep'))
        say()
        choice = ask('  ACTION_REQUIRED: ')
        alert(False)
        if choice == '1':
            self.ks('off')

    # ---------- ekran glowny ----------

    def s_START(self):
        cls()
        names = self.country_list()
        if not names and self.cur != 1:
            say(t('no_files', d=self.pdir))
            pause()
            self.set_provider(1)
            return 'START'
        title = t('locations')
        say(LINE)
        say(' ' * ((124 - len(title)) // 2) + title + ' ' * 30 + C_AUTHOR + 'by MRGREGOR85' + C_FG)
        say(LINE)
        say()
        if not names:
            say(t('no_files', d=self.pdir))
        for i in range(0, len(names), 5):
            say('  ' + ''.join(n[:24].ljust(24) for n in names[i:i + 5]))
        say(LINE)
        say(t('codes').center(124).rstrip())
        say(LINE)
        for line in CODES_BLOCK:
            say(' ' * 19 + line)
        say(LINE)
        if self.ks_active():
            ks_txt = t('ks_active')
        elif self.ks_want:
            ks_txt = t('ks_armed')
        else:
            ks_txt = t('ks_off')
        say(t('ks_line', s=ks_txt))
        say(t('cmds'))
        say(LINE)
        kraj = self.main_prompt()
        if kraj.upper() == 'ALT_C':
            return 'DISCONNECT'
        if not kraj:
            return 'START'
        if kraj.lower() == 'ks':
            return self.ks_toggle('START')
        if kraj.lower() == 'fs':
            self.win_full = not self.win_full
            save_flag(WIN_FILE, self.win_full)
            apply_window(self.win_full)
            return 'START'
        if kraj.lower() == 'lang':
            choose_language(force=True)
            return 'START'
        if kraj.isdigit():
            return self.switch(int(kraj))
        self.kraj = kraj
        self.mask = f'*-{kraj}-*.ovpn' if self.pmode == 'TOK2' else f'{kraj}*.ovpn'
        return 'LISTA'

    def main_prompt(self):
        # Siatka dostawcow (4 wiersze, numeracja w kolumnach od gory, aktywny WIELKIMI literami) + prompt.
        # Strzalki = wybor dostawcy, ENTER bez tekstu = wlacz zaznaczonego, tekst + ENTER = kod kraju lub numer,
        # ESC = wyczysc, Alt+C = rozlacz
        rows, n = 4, len(PROVIDERS)
        cells = {i: f'[{i:2}] ' + (PROVIDERS[i - 1][0] if i == self.cur else PROVIDERS[i - 1][1]) for i in range(1, n + 1)}
        _, top = cursor()
        for _ in range(rows):
            say()
        say(LINE)
        say()
        prompt = t('prompt')
        _, prow = cursor()
        # pod promptem: aktualny jezyk (TAB = lista jezykow)
        say()
        say()
        say(t('lang_line', n=dict(JEZYKI)[LANG]))
        draw_art()
        sel, txt = self.cur, ''
        while True:
            for i in range(1, n + 1):
                c, r = (i - 1) // rows, (i - 1) % rows
                goto(2 + c * 24, top + r)
                cell = cells[i].ljust(23)
                out(C_INV + cell + C_NOINV if i == sel else cell)
            goto(0, prow)
            out((prompt + txt).ljust(120))
            goto(len(prompt) + len(txt), prow)
            k = read_key()
            if k == 'ALT_C':
                txt = 'ALT_C'
                break
            if k == 'TAB':
                txt = 'lang'
                break
            if k == 'UP' and (sel - 1) % rows > 0:
                sel -= 1
            elif k == 'DOWN' and (sel - 1) % rows < rows - 1 and sel < n:
                sel += 1
            elif k == 'LEFT' and sel - rows >= 1:
                sel -= rows
            elif k == 'RIGHT' and sel + rows <= n:
                sel += rows
            elif k == 'ENTER':
                break
            elif k == 'BACK':
                txt = txt[:-1]
            elif k == 'ESC':
                txt = ''
            elif len(k) == 1:
                txt += k
        goto(0, prow + 1)
        return txt.strip() if txt.strip() else str(sel)

    def switch(self, i):
        if not 1 <= i <= len(PROVIDERS):
            return 'START'
        old = self.cur
        self.set_provider(i)
        if not self.files:
            say(t('no_files', d=self.pdir))
            pause()
            self.set_provider(old)
        return 'START'

    # ---------- lista serwerow ----------

    def s_LISTA(self):
        cls()
        say(LINE)
        say(t('nodes', k=self.kraj))
        say(LINE)
        say()
        files = self.match(self.mask)
        if not files:
            say(t('no_servers', k=self.kraj))
            say(t('no_servers2'))
            say(t('no_servers3'))
            time.sleep(5)
            return 'START'
        # Adres serwera z linii "remote" w pliku .ovpn; pingi rownolegle dla pierwszych PING_LIMIT
        hosts = [first_remote(os.path.join(self.pdir, f)) for f in files[:PING_LIMIT]]
        with concurrent.futures.ThreadPoolExecutor(64) as ex:
            pings = list(ex.map(lambda h: ping(h) if h else None, hosts))
        pings += [None] * (len(files) - len(pings))
        for i in range(0, len(files), 3):
            cols = [f'{f} [{p if p is not None else "???"}ms]'[:38].ljust(39) for f, p in zip(files[i:i + 3], pings[i:i + 3])]
            say('  ' + ''.join(cols))
        say()
        say(LINE)
        while True:
            say()
            plik = ask('  SELECT_TARGET_FILE: ')
            if not plik:
                return 'START'
            sel = None
            low = {f.lower(): f for f in self.files}
            if plik.lower() in low:
                sel = low[plik.lower()]
            elif plik.lower() + '.ovpn' in low:
                sel = low[plik.lower() + '.ovpn']
            # Krotka nazwa (np. af1, pl128, waw-065) - najpierw udp, potem tcp, potem cokolwiek o tym poczatku
            for pat in (f'{plik}.*udp*.ovpn', f'{plik}_udp*.ovpn', f'{plik}.*tcp*.ovpn', f'{plik}_tcp*.ovpn', f'{plik}.*.ovpn'):
                if sel:
                    break
                m = self.match(pat)
                sel = m[0] if m else None
            if sel:
                break
            say(t('no_server', p=plik))
        self.sel = sel
        if self.pauth and not os.path.exists(self.login_file):
            self.login_setup()
        return 'CONNECT'

    def login_setup(self):
        while True:
            cls()
            say(LINE_S)
            say('                      [ FIRST RUN: VPN AUTH CONFIGURATION ]')
            say(LINE_S)
            say(t('no_login', f=self.login_file))
            say(t('login_for', p=self.pname))
            say(f'  {self.phint}')
            say()
            name = ask(t('login'))
            if name:
                break
        pwd = read_secret(t('password'))
        os.makedirs(LOGIN_DIR, exist_ok=True)
        with open(self.login_file, 'w', encoding='utf-8', newline='\r\n') as f:
            f.write(name + '\n' + pwd + '\n')
        say()
        say(t('login_saved'))
        time.sleep(2)

    # ---------- laczenie ----------

    def s_CONNECT(self):
        cls()
        alert(True)
        say('  [!] ALERT: INITIALIZING CYBER-GHOST PROTOCOL...')
        say('  [#] GEOLOCATING TARGET NODE...')
        say('  [#] ENCRYPTING PACKETS WITH AES-256-GCM...')
        time.sleep(2)
        alert(False)
        if os.path.exists(OVPN_LOG):
            os.remove(OVPN_LOG)
        src = os.path.join(self.pdir, self.sel)
        # Kopia profilu: bez persist-key/fast-io (ostrzezenia DEPRECATED), bez linuksowych up/down/script-security,
        # sciezki /etc/openvpn/ zamienione na pliki obok profilu (OVPN.com), blokada DNS poza tunelem.
        # OpenVPN startuje w ukrytym oknie; --cd zostaje na folderze dostawcy, wiec certyfikaty sie znajduja.
        with open(src, encoding='latin-1') as f:
            lines = f.read().splitlines()
        cfg = [l.replace('/etc/openvpn/', '') for l in lines
               if not re.match(r'(persist-key|fast-io|up|down|script-security)(\s|$)', l.strip(), re.I)]
        if not any(re.match(r'\s*block-outside-dns', l) for l in cfg):
            cfg.append('block-outside-dns')
        with open(RUN_CFG, 'w', encoding='latin-1', newline='\r\n') as f:
            f.write('\n'.join(cfg) + '\n')
        # Przy aktywnej blokadzie trzeba przepuscic nowy serwer, inaczej OpenVPN sie nie polaczy
        if self.ks_active():
            self.ks('prep')
        args = [OPENVPN_EXE, '--cd', self.pdir, '--config', RUN_CFG, '--log', OVPN_LOG]
        if self.pauth:
            args += ['--auth-user-pass', self.login_file]
        subprocess.Popen(args, cwd=BIN_DIR, creationflags=CREATE_NO_WINDOW | CREATE_NEW_PROCESS_GROUP,
                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        say('  [#] ESTABLISHING TUNNEL...')
        state = 'WAIT'
        for _ in range(30):
            time.sleep(1)
            log = read_text(OVPN_LOG)
            if 'Initialization Sequence Completed' in log:
                state = 'OK'
            elif 'AUTH_FAILED' in log:
                state = 'AUTH'
            elif not ovpn_running():
                state = 'DEAD'
            if state != 'WAIT':
                break
        self.v_state = state
        if state == 'AUTH':
            return 'AUTH_FAIL'
        if state != 'OK':
            return 'CONNECT_FAIL'
        if self.ks_want:
            say(t('ks_enabling'))
            self.ks_on()
        # Dane o nowym IP (timeout 5 s - gdy tunel nie przepuszcza ruchu, nie wisimy w nieskonczonosc)
        v = {'ip': '--', 'city': '--', 'org': '--'}
        try:
            d = json.loads(http_get('https://ipinfo.io/json'))
            v.update({k: d.get(k, '--') for k in v})
        except Exception:
            pass
        # Prawdziwy szyfr tunelu z logu OpenVPN (np. AES-256-GCM)
        m = re.search(r"cipher '([^']+)'", read_text(OVPN_LOG), re.I)
        v['cipher'] = m.group(1) if m else None
        p = ping('8.8.8.8', 1000)
        v['ping'] = str(p) if p is not None else '--'
        v['since'] = datetime.datetime.now().strftime('%H:%M:%S')
        self.v = v
        return 'CONNECTED'

    def s_CONNECTED(self):
        # Tunel padl w tle (np. serwer zerwal polaczenie) - nie udajemy, ze dalej dziala
        if not ovpn_running():
            return 'TUNNEL_LOST'
        v = self.v
        ks_txt = 'ACTIVE (NO VPN = NO INTERNET)' if self.ks_active() else 'OFF'
        cls()
        say(LINE_S)
        say(f'    ACCESS GRANTED // ENCRYPTED UPLINK ESTABLISHED // SESSION: {random.randint(0, 32767)}')
        say(LINE_S)
        say()
        say('       uuuuuuu')
        say('       uu$$$$$$$$$$$uu            STATUS: GHOST_MODE_ACTIVE')
        say(f'    uu$$$$$$$$$$$$$$$$$uu         NODE_IP: {v["ip"]}')
        say(f'   u$$$$$$$$$$$$$$$$$$$$$u        PING: {v["ping"]} ms (ACTIVE TUNNEL)')
        say(f'   u$$$$$$$$$$$$$$$$$$$$$u        ENCRYPTION: {v["cipher"] or t("unknown")}')
        say('   u$$$$$$$$$$$$$$$$$$$$$u        INTERFACE: TUN0 (OPEN_VPN)')
        say('   u$$$$$$$$$$$$$$$$$$$$$u        DNS_SHIELD: 1.1.1.1 ACTIVE')
        say('   u$$$$$$"   "$$$"   "$$$$u       TRACE_STATUS: UNTRACEABLE')
        say(f'   "$$$$"      u$u       "$$$$"      KILL_SWITCH: {ks_txt}')
        say('    $$$u       u$u       u$$$')
        say(f'    $$$u      u$$$u      u$$$         [ LOCATION: {v["city"]} ]')
        say(f'    "$$$$uu$$$   $$$uu$$$$"          [ PROVIDER: {v["org"]} ]')
        say('      "$$$$$$$"   "$$$$$$$"')
        say(f'        u$$$$$$$u$$$$$$$u             CONNECTED_SINCE: {v["since"]}')
        say('        u$"$"$"$"$"$"$u')
        say(LINE_S)
        say()
        say('  [1] PERFORM SPEEDTEST (1GB HETZNER)')
        say('  [2] DISCONNECT AND WIPE SESSION')
        say('  [3] KILL SWITCH ON/OFF')
        say(t('altc'))
        say()
        choice = read_line_altc('  ACTION_REQUIRED: ')
        if choice == '1':
            self.speedtest()
            return 'CONNECTED'
        if choice in ('2', 'ALT_C'):
            return 'DISCONNECT'
        if choice == '3':
            return self.ks_toggle('CONNECTED')
        return 'CONNECTED'

    def speedtest(self):
        cls()
        say(LINE_S)
        say('    SPEEDTEST MODULE: DOWNLOADING 1GB TEST FILE...')
        say(LINE_S)
        say()
        got, t0, last = 0, time.time(), 0.0
        try:
            req = urllib.request.Request(TEST_URL, headers={'User-Agent': 'GHOST-NET'})
            with urllib.request.urlopen(req, timeout=10) as r:
                total = int(r.headers.get('Content-Length') or 0)
                while time.time() - t0 < 120:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    got += len(chunk)
                    now = time.time()
                    if now - last >= 0.5:
                        last = now
                        pct = f'{got * 100 // total:3}%' if total else ''
                        out(f'\r  {pct}  {got / 1048576:7.1f} MB   {got * 8 / 1e6 / (now - t0):7.1f} Mbit/s   ')
            say()
            secs = max(time.time() - t0, 0.001)
            say()
            say(t('speed_done', s=got * 8 / 1e6 / secs, mb=got / 1048576, t=secs))
        except Exception as e:
            say()
            say(t('speed_fail', e=e))
        pause()

    def s_DISCONNECT(self):
        cls()
        alert(True)
        say('  [#] TERMINATING SESSION...')
        ovpn_kill()
        # Rozlaczenie na zyczenie = zwykly internet wraca (kill switch zostaje wlaczony na nastepne polaczenie)
        if self.ks_active():
            self.ks('off')
        for _ in range(20):
            say(''.join(random.choice('0123456789') for _ in range(random.randint(16, 20))))
            time.sleep(0.03)
        alert(False)
        return 'START'

    # ---------- bledy polaczenia ----------

    def s_TUNNEL_LOST(self):
        cls()
        alert(True)
        say(LINE_S)
        say(t('tunnel_lost', s=self.sel))
        say(LINE_S)
        say()
        say(t('last_log'))
        say()
        for l in log_tail():
            say(l)
        say()
        if self.ks_active():
            say(t('ks_holds'))
        say()
        say(t('reconnect', s=self.sel))
        if self.ks_active():
            say(t('ks_unblock2'))
        say(t('back_enter'))
        say()
        alert(False)
        choice = ask('  ACTION_REQUIRED: ')
        if choice == '1':
            return 'CONNECT'
        if choice == '2' and self.ks_active():
            self.ks('off')
        return 'START'

    def save_error(self, why):
        # Raport bledu: bledy\blad_DATA_GODZINA.txt obok programu (pelny log OpenVPN), otwierany w Notatniku
        os.makedirs(ERR_DIR, exist_ok=True)
        st = stamp()
        path = os.path.join(ERR_DIR, f'blad_{st}.txt')
        log = read_text(OVPN_LOG) if os.path.exists(OVPN_LOG) else t('rep_nolog')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(t('rep_title') + '\n')
            f.write(t('rep_head', d=st, w=why, p=self.pname, s=self.sel, f=self.pdir, o=OPENVPN_EXE) + '\n')
            f.write(t('rep_log') + '\n')
            f.write(log)
        subprocess.Popen(['notepad', path])
        self.err_show = os.path.join('bledy', f'blad_{st}.txt')

    def next_server(self):
        # Nastepny serwer z tej samej listy, ten sam protokol (udp/tcp) i wariant (_2.6 lub nie)
        low = self.sel.lower()
        proto = 'udp' if 'udp' in low else ('tcp' if 'tcp' in low else None)
        is26 = '_2.6' in self.sel
        files = self.match(self.mask)

        def ok(f):
            return (not proto or proto in f.lower()) and (('_2.6' in f) == is26)
        try:
            idx = [f.lower() for f in files].index(low)
        except ValueError:
            idx = -1
        for f in files[idx + 1:] + files[:max(idx, 0)]:
            if f.lower() != low and ok(f):
                return f
        return None

    def s_AUTH_FAIL(self):
        ovpn_kill()
        if self.ks_active():
            self.ks('dnsoff')
        self.save_error(t('why_auth'))
        nxt = self.next_server()
        cls()
        alert(True)
        say(LINE_S)
        say(t('auth_fail', s=self.sel))
        say(LINE_S)
        say()
        say(t('auth_fail2'))
        say(t('auth_fail3', h=self.phint))
        say()
        say(t('next_srv', s=nxt) if nxt else t('no_next'))
        say(t('relogin'))
        say(t('back_list'))
        say()
        say(t('report', f=self.err_show))
        choice = ask('  ACTION_REQUIRED: ')
        alert(False)
        if choice == '1' and nxt:
            self.sel = nxt
            return 'CONNECT'
        if choice == '2':
            if os.path.exists(self.login_file):
                os.remove(self.login_file)
            self.login_setup()
            return 'CONNECT'
        return 'LISTA'

    def s_CONNECT_FAIL(self):
        ovpn_kill()
        self.save_error(t('why_dead') if self.v_state == 'DEAD' else t('why_timeout'))
        stale = False
        # NordVPN: gdy serwer juz nie istnieje, pliki sa przestarzale - pobieramy aktualne i wracamy do listy
        if self.pid == 'OPENVPN':
            res = self.nord_check()
            if res == 'UPDATED':
                return 'START'
            stale = res == 'FAILED'
        else:
            stale = self.stale_check()
        # DNS byl otwarty tylko na czas laczenia i sprawdzania serwera
        if self.ks_active():
            self.ks('dnsoff')
        cls()
        alert(True)
        say(LINE_S)
        say(f'    [!] TUNNEL FAILED // {self.pid} // {self.sel}')
        say(LINE_S)
        say()
        say(t('last_log'))
        say()
        for l in log_tail():
            say(l)
        say()
        say(t('report', f=self.err_show))
        if stale:
            say(t('stale', p=self.pname, i=self.pid))
        if self.ks_active():
            say(t('ks_blocks'))
        alert(False)
        pause()
        return 'LISTA'

    def nord_check(self):
        # Sprawdzenie serwera NordVPN i ewentualne pobranie aktualnych plikow.
        # Wynik: EXISTS = serwer istnieje (pliki aktualne), UPDATED = pobrano nowe pliki, FAILED = blad
        cls()
        say(t('nord_check', s=self.sel))
        host = re.sub(r'\.(udp|tcp).*$', '', self.sel, flags=re.I)
        if resolves(host):
            say(t('nord_ok'))
            return 'EXISTS'
        say(t('nord_gone', h=host))
        say(t('nord_dl'))
        zpath = os.path.join(TEMP, 'ghost_nord_ovpn.zip')
        stage = os.path.join(TEMP, 'ghost_nord_new')
        try:
            req = urllib.request.Request(PROVIDERS[0][6], headers={'User-Agent': 'GHOST-NET'})
            with urllib.request.urlopen(req, timeout=30) as r, open(zpath, 'wb') as f:
                got = 0
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    f.write(chunk)
                    got += len(chunk)
                    out(f'\r  [#] {got / 1048576:.0f} MB   ')
            say()
            say(t('nord_unzip'))
            shutil.rmtree(stage, ignore_errors=True)
            os.makedirs(stage)
            with zipfile.ZipFile(zpath) as z:
                for e in z.infolist():
                    # tylko pliki .ovpn, sama nazwa bez sciezki z archiwum
                    name = os.path.basename(e.filename)
                    if name.lower().endswith('.ovpn'):
                        with z.open(e) as src, open(os.path.join(stage, name), 'wb') as dst:
                            shutil.copyfileobj(src, dst)
            new = [f for f in os.listdir(stage) if f.lower().endswith('.ovpn')]
            if len(new) < 1000:
                raise RuntimeError(t('nord_few', n=len(new)))
            say(t('nord_swap', d=self.pdir))
            for f in self.ovpn_files():
                os.remove(os.path.join(self.pdir, f))
            for f in new:
                shutil.move(os.path.join(stage, f), os.path.join(self.pdir, f))
            shutil.rmtree(stage, ignore_errors=True)
            os.remove(zpath)
            self.list_cache.clear()
            say(t('nord_count', n=len(new)))
        except Exception as e:
            say()
            say(t('nord_fail', e=e))
            if self.ks_active():
                say(t('nord_ks'))
            self.stale_info(self.sel)
            pause()
            return 'FAILED'
        say(t('nord_done'))
        pause()
        self.set_provider(1)
        return 'UPDATED'

    def stale_check(self):
        # Czy adres serwera z pliku .ovpn jeszcze istnieje; adresow IP nie da sie tak sprawdzic
        host = first_remote(os.path.join(self.pdir, self.sel))
        if not host or is_ip(host) or resolves(host):
            return False
        self.stale_info(host)
        return True

    def stale_info(self, host):
        # Plik WYMIEN_SERWERY_<DOSTAWCA>.txt obok programu, otwierany w Notatniku
        path = os.path.join(WORK_DIR, f'WYMIEN_SERWERY_{self.pid}.txt')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(t('st_title') + '\n')
            f.write(t('st_body', p=self.pname, s=self.sel, h=host, d=f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S}',
                      u=self.purl, f=self.pdir))
        subprocess.Popen(['notepad', path])


def system_language():
    # Jezyk Windows (np. de_DE -> de) - podswietlony przy pierwszym wyborze; nieznany = angielski
    import locale
    codes = [c for c, _ in JEZYKI]
    try:
        name = locale.windows_locale.get(ctypes.windll.kernel32.GetUserDefaultUILanguage(), '')
    except Exception:
        name = ''
    code = name.split('_')[0].lower()
    code = {'no': 'nb', 'nn': 'nb'}.get(code, code)
    return code if code in codes else 'en'


def choose_language(force=False):
    # Wybor jezyka: strzalki + ENTER albo numer + ENTER; zapamietany w jezyk.txt.
    # Bez force tylko przy pierwszym uruchomieniu (gdy jezyk.txt jeszcze nie ma), ESC = zostaw obecny.
    global LANG
    codes = [c for c, _ in JEZYKI]
    saved = read_text(LANG_FILE).strip().lower()
    if saved in codes and not force:
        LANG = saved
        return
    sel = codes.index(LANG if force else system_language())
    rows = (len(JEZYKI) + 3) // 4
    cls()
    say(LINE_S)
    say('    [ JEZYK / LANGUAGE / SPRACHE / LANGUE / IDIOMA / ЯЗЫК ]')
    say(LINE_S)
    say()
    _, top = cursor()
    for _ in range(rows):
        say()
    say()
    say('  ↑ ↓ ← → + ENTER   /   NR + ENTER' + ('   /   ESC' if force else ''))
    say()
    prompt = '  > '
    _, prow = cursor()
    txt = ''
    while True:
        for i, (_c, name) in enumerate(JEZYKI):
            goto(2 + (i // rows) * 30, top + i % rows)
            cell = f'[{i + 1:2}] {name}'.ljust(28)
            out(C_INV + cell + C_NOINV if i == sel else cell)
        goto(0, prow)
        out((prompt + txt).ljust(40))
        goto(len(prompt) + len(txt), prow)
        k = read_key()
        if k == 'UP' and sel % rows > 0:
            sel -= 1
        elif k == 'DOWN' and sel % rows < rows - 1 and sel + 1 < len(JEZYKI):
            sel += 1
        elif k == 'LEFT' and sel - rows >= 0:
            sel -= rows
        elif k == 'RIGHT' and sel + rows < len(JEZYKI):
            sel += rows
        elif k == 'BACK':
            txt = txt[:-1]
        elif k == 'ESC' and force:
            return
        elif k == 'ENTER':
            if txt.isdigit() and 1 <= int(txt) <= len(JEZYKI):
                sel = int(txt) - 1
            break
        elif len(k) == 1 and k.isdigit() and len(txt) < 2:
            txt += k
    LANG = codes[sel]
    with open(LANG_FILE, 'w') as f:
        f.write(LANG + '\n')


def ensure_admin():
    # Uprawnienia administratora (OpenVPN i zapora) - gdy ich brak, uruchom sie jeszcze raz przez UAC
    if ctypes.windll.shell32.IsUserAnAdmin():
        return
    if getattr(sys, 'frozen', False):
        exe, params = sys.executable, ''
    else:
        exe, params = sys.executable, f'"{os.path.abspath(__file__)}"'
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', exe, params, WORK_DIR, 1)
    sys.exit(0)


def main():
    ensure_admin()
    enable_vt()
    ctypes.windll.kernel32.SetConsoleTitleW('[ GHOST-NET ] VPN MANAGER PRO // FULL_GITHUB_EDITION // by MRGREGOR85')
    os.system('color 0A')
    out(C_FG)
    app = App()
    apply_window(app.win_full)
    choose_language()
    if not os.path.exists(OPENVPN_EXE):
        say(t('no_openvpn', d=BIN_DIR))
        pause()
        return
    try:
        app.run()
    except KeyboardInterrupt:
        out(ESC + '[0m')
        say()


if __name__ == '__main__':
    main()
