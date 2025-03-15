import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

API_ENDPOINT = "https://32125.vercel.app/health"

def check_api_status():
    try:
        with console.status("[bold blue]Checking API status...", spinner="dots"):
            response = requests.get(API_ENDPOINT, timeout=5)
            if response.status_code == 200 and response.json().get("status") == "ok":
                return True, "ONLINE"
            else:
                return False, "ERROR"
    except Exception:
        return False, "OFFLINE"

def create_status_table():
    is_online, status_text = check_api_status()
    
    table = Table(show_header=False, show_edge=False, box=None)
    table.add_column("Label", style="cyan")
    table.add_column("Status", style="bold")
    
    status_style = "bold green" if is_online else "bold red"
    table.add_row("API STATUS:", Text(status_text, style=status_style))
    
    return table