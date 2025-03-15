from rich.console import Console

console = Console()

def get_thread_count():
    while True:
        console.print("[magenta]Threads:[/magenta] ", end="")
        user_input = console.input()
        
        try:
            thread_count = int(user_input)
            if thread_count < 1:
                console.print("[bold red]Thread count must be at least 1.[/bold red]")
                continue
            return thread_count
        except ValueError:
            console.print("[bold red]Please enter a valid number.[/bold red]")