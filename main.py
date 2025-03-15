# main.py
from rich.console import Console
from src.banner import display_banner
from src.api.health import create_status_table
from src.animations import animate_developer_credit
from src.checker import start_checking
from src.input import get_thread_count
from src.filter import filter_combos

console = Console()

def main():

    status_table = create_status_table()
    
    display_banner(status_table)
    
    animate_developer_credit()
    
    filter_combos()
    
    thread_count = get_thread_count()
    
    start_checking(thread_count)

if __name__ == "__main__":
    main()