import time
from rich.console import Console
from rich.live import Live
from rich.text import Text
from rich.align import Align

console = Console()

DEVELOPER_CREDIT = 'Developed by @cleanest'

def animate_developer_credit():
    with Live(refresh_per_second=20, transient=True) as live:
        live.update(Align.center(Text("", style="italic magenta")))
        time.sleep(0.5)
        
        for i in range(len(DEVELOPER_CREDIT) + 1):
            current_text = DEVELOPER_CREDIT[:i]
            cursor = "█" if i < len(DEVELOPER_CREDIT) else ""
            live.update(Align.center(Text(f"{current_text}{cursor}", style="italic magenta")))
            time.sleep(0.1)
        
        live.update(Align.center(Text(DEVELOPER_CREDIT, style="bold italic magenta")))
        time.sleep(0.5)