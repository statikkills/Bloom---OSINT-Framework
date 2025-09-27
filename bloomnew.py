# Bootstrap third-party dependencies (PC and Termux)
try:
    import sys as _sys
    import os as _os
    import subprocess as _subprocess
    import importlib as _importlib
except Exception:
    pass

def _ensure_dep(_module_name, _pip_name=None):
    try:
        _importlib.import_module(_module_name)
        return
    except Exception:
        pass
    _pkg = _pip_name or _module_name
    _commands = [
        [_sys.executable, "-m", "pip", "install", _pkg],
        [_sys.executable, "-m", "pip", "install", "--user", _pkg],
    ]
    for _cmd in _commands:
        try:
            _subprocess.check_call(_cmd)
            return
        except Exception:
            continue

# Ensure required packages
_ensure_dep("requests")
_ensure_dep("bs4", "beautifulsoup4")
_ensure_dep("pystyle")
_ensure_dep("phonenumbers")
_ensure_dep("ipwhois")
_ensure_dep("telebot", "pyTelegramBotAPI")

import requests
from bs4 import BeautifulSoup
from pystyle import *
import socket
import os
import csv
import time
import subprocess
import sys
import phonenumbers
import re
from ipwhois import IPWhois
import pystyle
import telebot
from telebot import types
import csv
import time
import json
import glob
from phonenumbers import geocoder, carrier, timezone
import ctypes
from ctypes import wintypes
import ipaddress

System.Title("Bloom Multitool")
try:
    if os.name == 'nt':
        os.system(f'mode con: cols=115 lines=58')
except Exception:
    pass

def _restart_program():
    os.system('cls' if os.name == 'nt' else 'clear')
    script_path = os.path.abspath(__file__)
    # Предпочитаем замену процесса, чтобы не накладывались экраны
    try:
        os.execv(sys.executable, [sys.executable, script_path])
    except Exception:
        # Фоллбэк для редких случаев
        if os.name == 'nt':
            cmd = f'"{sys.executable}" "{script_path}"'
            subprocess.Popen(cmd, shell=True)
        else:
            subprocess.Popen([sys.executable, script_path])
        os._exit(0)

def cls():
    input(f"\n\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}[@] {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}Нажмите Enter для перезапуска...{COLOR_CODE['RESET']}")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        show_banner()
    except Exception:
        pass
    # Перезапускаем код в текущем процессе, чтобы вернуться в меню
    with open(os.path.abspath(__file__), 'r', encoding='utf-8') as _f:
        _code = compile(_f.read(), os.path.abspath(__file__), 'exec')
        exec(_code, globals(), globals())



COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[38;2;154;2;2m",     
    "YELLOW": "\033[38;2;154;2;2m",    
    "RED": "\033[38;2;154;2;2m",       
    "CYAN": "\033[38;2;154;2;2m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[38;2;154;2;2m",
    "URL_L": "\033[38;2;154;2;2m",       
    "LI_G": "\033[38;2;154;2;2m",      
    "F_CL": "\033[0m",
    "DARK": "\033[38;2;154;2;2m",     
}

# Optional API key for Numverify (leave empty to skip)
NUMVERIFY_API_KEY = ""

banner = '''
                            ▀█████████▄   ▄█        ▄██████▄   ▄██████▄    ▄▄▄▄███▄▄▄▄  
                              ███    ███ ███       ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄
                              ███    ███ ███       ███    ███ ███    ███ ███   ███   ███
                             ▄███▄▄▄██▀  ███       ███    ███ ███    ███ ███   ███   ███
                            ▀▀███▀▀▀██▄  ███       ███    ███ ███    ███ ███   ███   ███
                              ███    ██▄ ███       ███    ███ ███    ███ ███   ███   ███
                              ███    ███ ███▌    ▄ ███    ███ ███    ███ ███   ███   ███
                            ▄█████████▀  █████▄▄██  ▀██████▀   ▀██████▀   ▀█   ███   █▀ 
                                         ▀                                                                                                                   
'''

banner2 = '''
       ╭─                   ─╮         ╭─                   ─╮  

         [1] - Поиск по бд               [5] - Web-crawler       
         [2] - HLR-Запрос                [6] - Обфусцировать код 
         [3] - WHOIS IP                  [0] - Выход
         [4] - Порт-скан                     

       ╰─                   ─╯         ╰─                   ─╯     
'''

banner3 = '''
            Coder - @statikkills
           ТГК - @statikkills_dev  
                                                       
     Price - FREE! Не подлежит продаже!    
'''
 
def show_banner():
    print(Colorate.Vertical(Colors.red_to_black,Center.XCenter(banner)))
    print(Colorate.Vertical(Colors.red_to_black,Center.XCenter(banner3)))
    print(Colorate.Vertical(Colors.red_to_black,Center.XCenter(banner2)))

# Отображение баннера при старте
show_banner()


choice = input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Выберите пункт {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')

if choice == '1':
    func1 = '''
    ─────────────────────────→ Поиск по локальным БД ←────────────────────────
      Введите данные для поиска. Поддерживается поиск телефонов/строк
      Что бы базы данных работали, нужно создать папку database в той же папке что и скрипт.
      В папке database можно хранить *.txt/*.csv/*.dat/*.log/*.sql файлы
    ──────────────────────────────────────────────────────────────────────────
    '''

    print(Center.XCenter(f"{COLOR_CODE['RED']}{func1}{COLOR_CODE['RESET']}"))

    # Баннер убран для соответствия общему дизайну

    # Утилиты
    def normalize_phone(phone):
        return re.sub(r'\D', '', phone)

    def search_in_file(file_path, search_variants):
        results = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    matches = {v for v in search_variants if v in line}
                    if matches:
                        results[line_num] = {
                            'content': line.strip(),
                            'matches': list(matches)
                        }
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='cp1251') as f:
                    for line_num, line in enumerate(f, 1):
                        matches = {v for v in search_variants if v in line}
                        if matches:
                            results[line_num] = {
                                'content': line.strip(),
                                'matches': list(matches)
                            }
            except:
                pass
        except:
            pass
        return results if results else None

    def scan_db_root(db_root):
        directories = []
        try:
            # Добавляем корень database как псевдодиректорию
            root_count = 0
            for ext in ('*.txt', '*.csv', '*.dat', '*.log', '*.sql'):
                root_count += len(glob.glob(os.path.join(db_root, ext)))
            directories.append({'name': '.', 'path': db_root, 'file_count': root_count})

            # Поддиректории
            for item in os.listdir(db_root):
                item_path = os.path.join(db_root, item)
                if os.path.isdir(item_path):
                    file_count = 0
                    for ext in ('*.txt', '*.csv', '*.dat', '*.log', '*.sql'):
                        # recursive=True, чтобы учитывать вложенные
                        file_count += len(glob.glob(os.path.join(item_path, '**', ext), recursive=True))
                    directories.append({'name': item, 'path': item_path, 'file_count': file_count})
        except Exception as e:
            print(f"\n\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}[@] {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}Ошибка сканирования: {e}")
        return sorted(directories, key=lambda x: x['name'])

    # Путь к БД: используем ./database
    db_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database')
    if not os.path.exists(db_root):
        print(f"\n\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}[@] {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}Папка database не найдена: {db_root}")
        cls()

    # Показ директорий
    dirs = scan_db_root(db_root)
    print(f"\n\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}[@] {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}Найдено директорий: {len(dirs)}")
    for d in dirs:
        print(f"\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}→ {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}{d['name']} ({d['file_count']} файлов)")

    # Ввод запроса
    query = input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Введите данные для поиска {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}').strip()
    if not query:
        cls()

    # Варианты поиска
    search_variants = [query]
    if re.match(r'^[\d\s\-\+\(\)]+$', query):
        clean_phone = normalize_phone(query)
        search_variants = [clean_phone]
        if len(clean_phone) > 10:
            search_variants.append(clean_phone[-10:])
            if clean_phone.startswith('7') and len(clean_phone) == 11:
                search_variants.append(clean_phone[1:])

    # Собираем все файлы
    all_files = []
    seen_files = set()
    for d in dirs:
        for ext in ('*.txt', '*.csv', '*.dat', '*.log', '*.sql'):
            # Для корня учитываем файлы непосредственно внутри
            for fp in glob.glob(os.path.join(d['path'], ext)):
                if fp not in seen_files:
                    seen_files.add(fp)
                    all_files.append(fp)
            # И также вложенные файлы
            for fp in glob.glob(os.path.join(d['path'], '**', ext), recursive=True):
                if fp not in seen_files:
                    seen_files.add(fp)
                    all_files.append(fp)

    if not all_files:
        print(f"\n\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}[@] {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}Файлы не найдены")
        cls()

    # Поиск
    all_results = []
    start_ts = time.time()
    processed = 0
    found_files = 0
    print(f"\n\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}[@] {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}Сканирование файлов...")
    for file_path in all_files:
        file_results = search_in_file(file_path, search_variants)
        processed += 1
        if file_results:
            found_files += 1
            all_results.append({
                'file': os.path.basename(file_path),
                'path': file_path,
                'results': file_results
            })

    elapsed = time.time() - start_ts
    print(f"\n\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}[@] {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}Готово за {elapsed:.1f} c. Найдено файлов: {found_files}")

    # Вывод результатов
    if not all_results:
        print(f"\n\t    {COLOR_CODE['YELLOW']}{COLOR_CODE['BOLD']}[@] {COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}Совпадения не найдены")
        cls()

    counter = 0
    print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')
    for file_result in all_results:
        filename = file_result['file']
        filepath = file_result['path']
        for line_num, match_data in file_result['results'].items():
            counter += 1
            print(f"\t{COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}{counter}. Файл: {filename}")
            print(f"\t{COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}   Путь: {filepath}")
            print(f"\t{COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}   Строка: {line_num}")
            print(f"\t{COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}   Совпадения: {', '.join(match_data['matches'])}")
            print(f"\t{COLOR_CODE['CYAN']}{COLOR_CODE['BOLD']}   Содержимое: {match_data['content']}")
            print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')

    cls()

if choice == '2':
  func2 = '''
  ─────────────────────────→ Инструкция ←─────────────────────────
            Для того чтобы проверить номер на валидность. Нужно
               Ввести номер с +. К примеру (+79000000000)
  ────────────────────────────────────────────────────────────────
  '''

  print(Center.XCenter(f"{COLOR_CODE['RED']}{func2}{COLOR_CODE['RESET']}"))
  search_value = input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Введите номер {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')

  try:
      # Очистка ввода, сохранение плюса
      cleaned_number = re.sub(r'[^\d+]', '', search_value)
      if cleaned_number.startswith('8') and len(cleaned_number) == 11:
          cleaned_number = '+7' + cleaned_number[1:]

      parsed_number = phonenumbers.parse(cleaned_number, None)

      if not phonenumbers.is_valid_number(parsed_number):
          print(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Неверный формат номера')
          cls()
      else:
          country = geocoder.description_for_number(parsed_number, "ru")
          operator = carrier.name_for_number(parsed_number, "ru")
          e164_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

          # Печать базовой информации
          print(f'\n\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}    → Информация о номере')
          print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')
          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Формат E164 → {e164_format}')
          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Страна → {country}')
          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Оператор → {operator}')

          # Numverify (если указан ключ)
          if NUMVERIFY_API_KEY:
              try:
                  number_digits = e164_format.replace('+', '')
                  resp = requests.get(
                      f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={number_digits}",
                      timeout=10
                  )
                  if resp.status_code == 200:
                      data = resp.json()
                      if data.get('valid', False):
                          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Локация → {data.get("location", "Неизвестно")}')
                          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Тип линии → {data.get("line_type", "Неизвестно")}')
                          print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Страна → {data.get("country_name", "Неизвестно")} ({data.get("country_code", "")})')
              except Exception:
                  pass

          # HTMLWeb (доп. сведения)
          try:
              number_digits = e164_format.replace('+', '')
              web_resp = requests.get(
                  f"https://htmlweb.ru/geo/api.php?json&telcod={number_digits}",
                  headers={
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                  },
                  timeout=10
              )
              if web_resp.status_code == 200:
                  web = web_resp.json()
                  print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Регион → {web.get("region", {}).get("name", "Неизвестно")}')
                  print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Индекс → {web.get("0", {}).get("post", "Неизвестно")}')
                  print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Автокод → {web.get("region", {}).get("autocod", "Неизвестно")}')
                  print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Бренд → {web.get("0", {}).get("oper_brand", "Неизвестно")}')
          except Exception:
              pass

          print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')
          cls()

  except phonenumbers.phonenumberutil.NumberParseException:
      print(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Неверный номер')
      cls()

if choice == '3':
    func3 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
                 Для того чтобы пробить IP-адрес, введите
                        адрес в формате (0.0.0.0)
    ────────────────────────────────────────────────────────────────
    '''

    print(Center.XCenter(f"{COLOR_CODE['RED']}{func3}{COLOR_CODE['RESET']}"))

    def safe_get_reverse_dns(target_ip):
        try:
            host, _, _ = socket.gethostbyaddr(target_ip)
            return host
        except Exception:
            return "Неизвестно"

    def fetch_rdap(target_ip):
        try:
            obj = IPWhois(target_ip)
            return obj.lookup_rdap(depth=1)
        except Exception as e:
            return {"error": str(e)}

    def fetch_geo(target_ip):
        try:
            resp = requests.get(
                f"http://ip-api.com/json/{target_ip}?fields=status,country,city,regionName,lat,lon,isp,org,as,asname,timezone,query",
                timeout=8,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            if resp.status_code == 200:
                data = resp.json()
                if data.get("status") == "success":
                    return data
        except Exception:
            pass
        return {}

    def print_section(title):
        print(f'\n\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}    → {title}')
        print(f'\t{COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}    ────────────────────────────────────────────────────────────────')

    ip_input = input(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Введите IP {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}').strip()

    # Валидация IP
    try:
        ip_obj = ipaddress.ip_address(ip_input)
        ip_str = str(ip_obj)
    except ValueError:
        print(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Неверный IP-адрес')
        cls()

    # RDAP
    rdap = fetch_rdap(ip_str)
    if rdap.get("error"):
        print(f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[BLOOM] Ошибка RDAP: {rdap["error"]}')

    # GEO
    geo = fetch_geo(ip_str)

    # Reverse DNS
    rdns = safe_get_reverse_dns(ip_str)

    # Вывод
    print_section("Информация об IP")
    print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      IP → {ip_str}')
    if rdap and not rdap.get("error"):
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      ASN → {rdap.get("asn", "Неизвестно")}')
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      AS Name → {rdap.get("asn_description", "Неизвестно")}')
        network = rdap.get("network", {})
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      CIDR → {network.get("cidr", "Неизвестно")}')
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Range → {network.get("start_address", "?")} - {network.get("end_address", "?")}')
        def _extract_emails_from_obj(obj):
            results = []
            contact = obj.get("contact", {}) or {}
            email_field = contact.get("email")
            if email_field:
                if isinstance(email_field, list):
                    for it in email_field:
                        if isinstance(it, dict) and it.get("value"):
                            results.append(str(it.get("value")))
                        else:
                            results.append(str(it))
                elif isinstance(email_field, dict) and email_field.get("value"):
                    results.append(str(email_field.get("value")))
                else:
                    results.append(str(email_field))
            # vCard parsing (RDAP often stores contacts here)
            vcard = obj.get("vcardArray")
            if isinstance(vcard, list) and len(vcard) > 1 and isinstance(vcard[1], list):
                for entry in vcard[1]:
                    try:
                        if isinstance(entry, list) and len(entry) >= 4:
                            if entry[0] == "email":
                                email_val = entry[3]
                                if isinstance(email_val, dict) and email_val.get("value"):
                                    results.append(str(email_val.get("value")))
                                else:
                                    results.append(str(email_val))
                    except Exception:
                        pass
            return results

        entities = rdap.get("objects", {})
        abuse_emails = []
        for obj in entities.values():
            roles = obj.get("roles", []) or []
            if "abuse" in roles or "noc" in roles or "technical" in roles:
                abuse_emails.extend(_extract_emails_from_obj(obj))
        unique_emails = sorted({e for e in abuse_emails if isinstance(e, str) and e})
        if unique_emails:
            print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Контакты (abuse/tech) → {", ".join(unique_emails)}')

    print_section("Геолокация и провайдер")
    if geo:
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Страна → {geo.get("country", "Неизвестно")}')
        city = geo.get("city") or "Неизвестно"
        region = geo.get("regionName") or "Неизвестно"
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Город/Регион → {city} / {region}')
        tz = geo.get("timezone") or "Неизвестно"
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Часовой пояс → {tz}')
        isp = geo.get("isp") or geo.get("org") or "Неизвестно"
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Провайдер → {isp}')
        lat, lon = geo.get("lat"), geo.get("lon")
        if lat is not None and lon is not None:
            print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Координаты → {lat}, {lon}')
    else:
        print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Данные гео недоступны')

    print_section("Дополнительно")
    print(f'\t{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}      Reverse DNS → {rdns}')

    cls()

if choice == '4':
    func4 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
      Для того чтобы посмотреть открытые или закрытые порты. Нужно
                 1. Ввести хост (пример: youtube.com)
             2. Ввести порт, который вы хотите просмотреть
    ────────────────────────────────────────────────────────────────
    '''

    print(Center.XCenter(f"{COLOR_CODE['RED']}{func4}{COLOR_CODE['RESET']}"))
    def check_port(domain, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((domain, port)) == 0:
                    return True
                else:
                    return False
        except Exception as e:
            return f'\n\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[BLOOM] ERROR!!!'

    if __name__ == "__main__":
        domain = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter host {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}').strip()
        port_str = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter port {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}').strip()
        try:
            port = int(port_str)
            result = check_port(domain, port)
            if result == True:
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Port {port} on {domain} {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}OPEN')
                cls()
            elif result == False:
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Port {port} on {domain} {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}CLOSE')
                cls()
            else:
                print(result)
                cls()
        except ValueError:
            print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}The port must be a number')
            cls()     

if choice == '5':
    func5 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
       Web Crawl - процедура сбора информации о новых или прошедших 
        обновление страницах. С целью последующей загрузки в индекс
                            поисковой системы. 
              1. Ввести ссылку (пример: https://youtube.com/)
    ────────────────────────────────────────────────────────────────
    '''

    print(Center.XCenter(f"{COLOR_CODE['RED']}{func5}{COLOR_CODE['RESET']}"))
    def crawl(url):
        try:
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                title = soup.title.text
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Title {COLOR_CODE["YELLOW"]}→{COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} {title}')


                links = soup.find_all('a')
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Url to websites {COLOR_CODE["YELLOW"]}→{COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} ({len(links)})')

                for link in links:
                    print(link.get('href'))
            else:
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Error {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} {response.status_code}')
                cls()

        except requests.RequestException as e:
            print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Error {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]} {str(e)}')
            cls()


    if __name__ == '__main__':
        url = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter URL {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
        crawl(url)
        cls() 
 
if choice == '6':
    func10 = '''
    ─────────────────────────→ Инструкция ←─────────────────────────
                Для того чтобы обфусцировать файл. Вам нужно
                       1. Выбрать метод обфускации
                  2. Ввести название файла с расширением
                3. Обозначить количество этапов обфускации
                  
    ────────────────────────────────────────────────────────────────
    '''

    print(Center.XCenter(f"{COLOR_CODE['RED']}{func10}{COLOR_CODE['RESET']}"))
    import os
    import sys
    import zlib
    import time
    import base64
    import marshal
    import py_compile

    # Lambda functions for encoding
    zlb = lambda in_: zlib.compress(in_)
    b16 = lambda in_: base64.b16encode(in_)
    b32 = lambda in_: base64.b32encode(in_)
    b64 = lambda in_: base64.b64encode(in_)
    mar = lambda in_: marshal.dumps(compile(in_, '<x>', 'exec'))


    class FileSize:
        def datas(self, z):
            for x in ['Byte', 'KB', 'MB', 'GB']:
                if z < 1024.0:
                    return "%3.1f %s" % (z, x)
                z /= 1024.0

        def __init__(self, path):
            if os.path.isfile(path):
                dts = os.stat(path).st_size
                print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Encoded File Size {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}%s' % self.datas(dts))


    def Encode(option, data, output):
        loop = int(input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Encode Count {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}'))
        if option == 1:
            xx = "mar(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
        elif option == 2:
            xx = "zlb(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
        elif option == 3:
            xx = "b16(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
        elif option == 4:
            xx = "b32(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
        elif option == 5:
            xx = "b64(data.encode('utf8'))[::-1]"
            heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
        elif option == 6:
            xx = "b16(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
        elif option == 7:
            xx = "b32(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
        elif option == 8:
            xx = "b64(zlb(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
        elif option == 9:
            xx = "zlb(mar(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
        elif option == 10:
            xx = "b16(mar(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
        elif option == 11:
            xx = "b32(mar(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
        elif option == 12:
            xx = "b64(mar(data.encode('utf8')))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
        elif option == 13:
            xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
        elif option == 14:
            xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
        elif option == 15:
            xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
            heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
        else:
            print("\n Invalid Option!")
            cls()

        for _ in range(loop):
            try:
                data = "exec((_)(%s))" % repr(eval(xx))
            except TypeError as s:
                print("TypeError: " + str(s))
                cls()

        with open(output, 'w') as f:
            f.write(heading + data)

        FileSize(output)

    # Используем глобальный cls() для единого поведения перезапуска с баннером


    # Entry point
    if __name__ == "__main__":
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}1. Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}2. Zlib')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}3. Base64 (b16)')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}4. Base64 (b32)')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}5. Base64 (b64)')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}6. Base64 (b16) + Zlib')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}7. Base64 (b32) + Zlib')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}8. Base64 (b64) + Zlib')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}9. Zlib + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}10. Base64 (b16) + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}11. Base64 (b32) + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}12. Base64 (b64) + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}13. Base64 (b16) + Zlib + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}14. Base64 (b32) + Zlib + Marshal')
        print(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}15. Base64 (b64) + Zlib + Marshal')

        try:
            option = int(input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}Enter option {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}'))
            file = input(f'\t    {COLOR_CODE["YELLOW"]}{COLOR_CODE["BOLD"]}[@] {COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}File Name {COLOR_CODE["YELLOW"]}→ {COLOR_CODE["BOLD"]}{COLOR_CODE["CYAN"]}')
            data = open(file, encoding="utf8").read()
            output = file.lower().replace('.py', '') + '_enc.py'
            Encode(option, data, output)
            cls()
        except Exception as e:
            print(f"Error: {str(e)}")
    cls()

if choice == '0':
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()

