from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.table import Table

console = Console()

BANNER = '''
$$\\                                              
$$ |                                             
$$ |     $$\\   $$\\ $$$$$$$\\   $$$$$$\\   $$$$$$\\  
$$ |     $$ |  $$ |$$  __$$\\  \\____$$\\ $$  __$$\\ 
$$ |     $$ |  $$ |$$ |  $$ | $$$$$$$ |$$ |  \\__| 
$$ |     $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |      
$$$$$$$$\\\\$$$$$$  |$$ |  $$ |\\$$$$$$$ |$$ |      
\\________|\\______/ \\__|  \\__| \\_______|\\__|     
'''

def display_banner(status_table):
    banner_text = Text(BANNER, style="bold magenta")
    
    grid = Table.grid(expand=True)
    grid.add_row(Align.center(banner_text))
    grid.add_row("")
    grid.add_row(Align.center(status_table))
    
    console.print(Panel(
        grid,
        border_style="magenta",
        padding=(1, 2)
    ))
    console.print()