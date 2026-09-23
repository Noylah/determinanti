from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import ROUNDED

console = Console()

def print_mat(mat, title="Matrice", det=None):
    t = Table(box=ROUNDED, show_header=False, pad_edge=True)
    for _ in mat[0]:
        t.add_column(justify="center", width=5)
    for row in mat:
        t.add_row(*[f"{x:g}" for x in row])

    subtitle = f"[bold]det = {det:g}[/bold]" if det is not None else None
    console.print(Panel(t, title=f"[bold]Δ = {title} [/](Matrice {len(mat)}×{len(mat[0])})",
                        subtitle=subtitle, border_style="cyan", expand=False))   