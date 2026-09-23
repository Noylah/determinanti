import sys
from rich.console import Console
from output import print_mat

console = Console()

def input_matrice():
    matrice = []

    console.print("[magenta][bold]Inserisci i valori separati da uno spazio.")
    input1 = console.input("[magenta]Riga 1: [/]")

    if not input1:
        console.print("[red][Errore] Inserisci i valori separati da uno spazio.")
        sys.exit(1)

    try:
        riga1 = [int(x) for x in input1.split()]   
    except ValueError:
        console.print("[red][Errore] I valori non sono validi, inserisci numeri interi.")
        sys.exit(1)

    matrice.append(riga1)

    for i in range(1, len(riga1)):
        riga_input = console.input(f"[magenta]Riga {i+1}: [/]")
        try:
            riga = [int(x) for x in riga_input.split()]
        except ValueError:
            console.print("[red][Errore] I valori non sono validi, inserisci numeri interi.")
            sys.exit(1)
        if not riga:
            console.print("[red][Errore] Inserisci i valori separati da uno spazio.")
            sys.exit(1)
        if len(riga) != len(riga1):
            console.print("[red][Errore] Il numero di valori deve essere sempre uguale")
            sys.exit(1)
        matrice.append(riga)

    return matrice