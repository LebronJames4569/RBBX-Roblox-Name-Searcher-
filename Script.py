import requests
import random
import string
import time
import os
import sys
import shutil

# Constants
DEFAULT_USERNAME_LENGTH = 5
DEFAULT_FILE = 'valid.txt'
DEFAULT_BIRTHDAY = '2000-01-01'

# Global settings
USERNAME_LENGTH = DEFAULT_USERNAME_LENGTH
FILE = DEFAULT_FILE
BIRTHDAY = DEFAULT_BIRTHDAY


# Color formatting - all green theme except for taken usernames
class bcolors:
    HEADER = '\033[92m'  # Green
    OKGREEN = '\033[92m'  # Green
    OKBLUE = '\033[92m'   # Green
    WARNING = '\033[92m'  # Green
    FAIL = '\033[91m'     # Red for taken usernames
    CYAN = '\033[92m'     # Green
    PURPLE = '\033[92m'   # Green
    MAGENTA = '\033[92m'  # Green
    ORANGE = '\033[92m'   # Green
    LIGHT_BLUE = '\033[92m'  # Green
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WHITE = '\033[92m'    # Green


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_term_width(default=50):
    """Return the terminal width, falling back to `default` if unavailable."""
    try:
        width = shutil.get_terminal_size().columns
        return max(40, width)
    except Exception:
        return default


def build_box(title, body_lines, min_width=30, pad=2):
    """
    Build a centered box string for given title and lines.
    """
    term_w = get_term_width()
    content_lines = [title] + body_lines
    inner_max = max(len(strip_ansi(s)) for s in content_lines)
    inner_w = max(min_width, inner_max + pad * 2)
    if inner_w + 4 > term_w:
        inner_w = term_w - 4
        if inner_w < 20:
            inner_w = 20

    left_margin = (term_w - (inner_w + 4)) // 2

    horizontal = '═' * inner_w
    top = ' ' * left_margin + f'╔{horizontal}╗'
    bottom = ' ' * left_margin + f'╚{horizontal}╝'

    def format_line(s):
        s_plain = strip_ansi(s)
        padding_needed = inner_w - len(s_plain)
        left_pad = padding_needed // 2
        right_pad = padding_needed - left_pad
        return ' ' * left_margin + f'║' + ' ' * left_pad + s + ' ' * right_pad + f'║'

    lines = [top]
    lines.append(format_line(bcolors.BOLD + title + bcolors.ENDC))
    lines.append(' ' * left_margin + f'╠' + '═' * inner_w + f'╣')
    for bl in body_lines:
        lines.append(format_line(bl))
    lines.append(bottom)
    return '\n'.join(lines)


def strip_ansi(s):
    """Remove basic ANSI sequences for width measuring."""
    import re
    ansi_re = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_re.sub('', s)


def animate_ascii_art():
    """Simple intro animation centered to terminal width."""
    clear_screen()
    logo = [
        "OooOOo.  o.oOOOo.  o.oOOOo.  o      O ",
        "o     `o  o     o   o     o   O    o  ",
        "O      O  O     O   O     O    o  O   ",
        "o     .O  oOooOO.   oOooOO.     oO    ",
        "OOooOO'   o     `O  o     `O    Oo    ",
        "o    o    O      o  O      o   o  o   ",
        "O     O   o     .O  o     .O  O    O  ",
        "O      o  `OooOO'   `OooOO'  O      o ",
        "                                       ",
        "                                       ",
    ]
    clear_screen()
    term_w = get_term_width()
    print(bcolors.OKGREEN + bcolors.BOLD)  # Green for ASCII art
    for line in logo:
        print(line.center(term_w))
        time.sleep(0.03)
    print(bcolors.ENDC)
    time.sleep(0.3)


def display_main_menu_ascii():
    """Small header banner centered."""
    title = "RBBX Username Seacher"
    box = build_box(title, [" "], min_width=30)
    print(bcolors.OKGREEN + box + bcolors.ENDC)  # Green header


def display_main_menu():
    """Main menu display using dynamic boxes."""
    body = [
        f"{bcolors.OKGREEN}1.{bcolors.ENDC} Start Checking Usernames",
        f"{bcolors.OKGREEN}2.{bcolors.ENDC} Settings",
        f"{bcolors.OKGREEN}3.{bcolors.ENDC} Exit",
    ]
    menu_box = build_box("MAIN MENU", body, min_width=30)
    print(bcolors.OKGREEN + menu_box + bcolors.ENDC)  # Green main menu
    
    settings_lines = [
        f"Username length : {bcolors.OKGREEN}{USERNAME_LENGTH}{bcolors.ENDC}",
        f"Birthday        : {bcolors.OKGREEN}{BIRTHDAY}{bcolors.ENDC}",
        f"Output file     : {bcolors.OKGREEN}{FILE}{bcolors.ENDC}",
    ]
    print(bcolors.OKGREEN + build_box("Current Settings", settings_lines, min_width=30) + bcolors.ENDC)  # Green settings


def display_settings_menu():
    """Settings menu with dynamic box rendering and handling."""
    global USERNAME_LENGTH, FILE, BIRTHDAY

    while True:
        clear_screen()
        display_main_menu_ascii()  # This will show green header
        body = [
            f"{bcolors.OKGREEN}1.{bcolors.ENDC} Username Length : {bcolors.OKGREEN}{USERNAME_LENGTH}{bcolors.ENDC}",
            f"{bcolors.OKGREEN}2.{bcolors.ENDC} Birthday        : {bcolors.OKGREEN}{BIRTHDAY}{bcolors.ENDC}",
            f"{bcolors.OKGREEN}3.{bcolors.ENDC} Output File     : {bcolors.OKGREEN}{FILE}{bcolors.ENDC}",
            f"{bcolors.OKGREEN}4.{bcolors.ENDC} Back to Main Menu",
        ]
        print(bcolors.OKGREEN + build_box("SETTINGS", body, min_width=36) + bcolors.ENDC)  # Green settings menu

        choice = input(f"\n{bcolors.OKGREEN}Select option (1-4): {bcolors.ENDC}").strip()
        if choice == '1':
            try:
                new_length = int(input(f"{bcolors.OKGREEN}Enter username length (current: {USERNAME_LENGTH}): {bcolors.ENDC}").strip())
                if new_length >= 3:
                    USERNAME_LENGTH = new_length
                    print(f"{bcolors.OKGREEN}[+] Username length updated to {USERNAME_LENGTH}{bcolors.ENDC}")
                else:
                    print(f"{bcolors.OKGREEN}[-] Must be at least 3{bcolors.ENDC}")
            except ValueError:
                print(f"{bcolors.OKGREEN}[-] Invalid number{bcolors.ENDC}")
            input(f"{bcolors.OKGREEN}Press Enter to continue...{bcolors.ENDC}")
        elif choice == '2':
            new_birthday = input(f"{bcolors.OKGREEN}Enter birthday (YYYY-MM-DD) (current: {BIRTHDAY}): {bcolors.ENDC}").strip()
            if len(new_birthday) == 10 and new_birthday[4] == '-' and new_birthday[7] == '-':
                BIRTHDAY = new_birthday
                print(f"{bcolors.OKGREEN}[+] Birthday updated to {BIRTHDAY}{bcolors.ENDC}")
            else:
                print(f"{bcolors.OKGREEN}[-] Invalid date format{bcolors.ENDC}")
            input(f"{bcolors.OKGREEN}Press Enter to continue...{bcolors.ENDC}")
        elif choice == '3':
            new_file = input(f"{bcolors.OKGREEN}Enter output filename (current: {FILE}): {bcolors.ENDC}").strip()
            if new_file:
                FILE = new_file
                print(f"{bcolors.OKGREEN}[+] Output file set to {FILE}{bcolors.ENDC}")
            else:
                print(f"{bcolors.OKGREEN}[-] Filename cannot be empty{bcolors.ENDC}")
            input(f"{bcolors.OKGREEN}Press Enter to continue...{bcolors.ENDC}")
        elif choice == '4':
            break
        else:
            print(f"{bcolors.OKGREEN}[-] Invalid option{bcolors.ENDC}")
            time.sleep(1)


def success(username):
    print(f"{bcolors.OKGREEN}🎉 [+] FOUND AVAILABLE USERNAME: {username}{bcolors.ENDC}")
    with open(FILE, 'a+', encoding='utf-8') as f:
        f.write(f"{username}\n")


def taken(username):
    print(f"{bcolors.FAIL}[-] {username} is taken{bcolors.ENDC}")


def make_username(length):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def check_username(username):
    url = f'https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday={BIRTHDAY}'
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json',
        'Referer': 'https://www.roblox.com/',
        'Origin': 'https://www.roblox.com',
    }
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()
    return response.json()


def start_checking():
    clear_screen()
    display_main_menu_ascii()  # Green header
    lines = [
        f"Username length : {bcolors.OKGREEN}{USERNAME_LENGTH}{bcolors.ENDC}",
        f"Birthday        : {bcolors.OKGREEN}{BIRTHDAY}{bcolors.ENDC}",
        f"Output file     : {bcolors.OKGREEN}{FILE}{bcolors.ENDC}",
    ]
    print(bcolors.OKGREEN + build_box("Starting username check", lines, min_width=36) + bcolors.ENDC)  # Green box
    print(f"\n{bcolors.OKGREEN}Searching for first available username... (Ctrl+C to stop){bcolors.ENDC}\n")

    attempts = 0
    start_time = time.time()
    try:
        while True:
            attempts += 1
            try:
                username = make_username(USERNAME_LENGTH)
                data = check_username(username)
                if isinstance(data, dict) and data.get('code') == 0:
                    success(username)
                    break
                else:
                    taken(username)
            except requests.exceptions.HTTPError as e:
                status = getattr(e.response, 'status_code', None)
                if status == 429:
                    print(f"{bcolors.OKGREEN}[!] Rate limited. Waiting 5 seconds...{bcolors.ENDC}")
                    time.sleep(5)
                else:
                    print(f"{bcolors.OKGREEN}HTTP error {status}: {e}{bcolors.ENDC}")
                    time.sleep(2)
            except requests.exceptions.RequestException as e:
                print(f"{bcolors.OKGREEN}Network error: {e}{bcolors.ENDC}")
                time.sleep(2)
            except Exception as e:
                print(f"{bcolors.OKGREEN}Error: {e}{bcolors.ENDC}")
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{bcolors.OKGREEN}[!] Script interrupted by user{bcolors.ENDC}")
        return

    elapsed = time.time() - start_time
    print(f"\n{bcolors.OKGREEN}✨ SUCCESS! Found available username in {elapsed:.2f} seconds{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}📊 Total attempts: {attempts}{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}🚀 Speed: {attempts/elapsed:.1f} usernames/second{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}💾 Username saved to: {FILE}{bcolors.ENDC}")
    input(f"{bcolors.OKGREEN}Press Enter to return to main menu...{bcolors.ENDC}")


def main():
    animate_ascii_art()
    time.sleep(0.2)
    while True:
        clear_screen()
        display_main_menu_ascii()  # Green header
        display_main_menu()  # Green menus
        choice = input(f"\n{bcolors.OKGREEN}Select option (1-3): {bcolors.ENDC}").strip()
        if choice == '1':
            start_checking()
        elif choice == '2':
            display_settings_menu()
        elif choice == '3':
            print(f"\n{bcolors.OKGREEN}Thank you for using Roblox Username Checker!{bcolors.ENDC}")
            sys.exit(0)
        else:
            print(f"{bcolors.OKGREEN}[-] Invalid option. Please select 1-3.{bcolors.ENDC}")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{bcolors.OKGREEN}Thank you for using Roblox Username Checker!{bcolors.ENDC}")
        sys.exit(0)