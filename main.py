from rich.console import Console
from output import print_mat
from input import input_matrice

console = Console()

# Matrice di Partenza
matrice = input_matrice()

# Controllo Validità Matrice Quadrata
def check_matrice(matrice: list[list[int]]):
    ordine_matrice = len(matrice)
    try:
        if len(matrice) == 0:
            return False
        for i in range(ordine_matrice):
            if len(matrice[i-1]) != ordine_matrice:
                return False
        return True
    except TypeError:
        return False

# Funzioni Utili
def is_posizizone_pari(pos):
    somma_pos = pos[0] + pos[1]
    if somma_pos % 2 == 0:
        return True
    return False

# Metodo Matrici 2x2
def metodo_diagonale(matrice):
    determinante = (matrice[0][0] * matrice[1][1]) - (matrice[0][1] * matrice[1][0])
    return determinante

# Metodo Matrici 3x3
def metodo_sarrus(matrice):
    diag_principale = (matrice[0][0] * matrice[1][1] * matrice[2][2]) + (matrice[0][1] * matrice[1][2] * matrice[2][0]) + (matrice[0][2] * matrice[1][0] * matrice[2][1])
    diag_secondaria = (matrice[0][2] * matrice[1][1] * matrice[2][0]) + (matrice[0][0] * matrice[1][2] * matrice[2][1]) + (matrice[0][1] * matrice[1][0] * matrice[2][2])
    determinante = diag_principale - diag_secondaria
    return determinante

# Metodo Matrici 4x4 o superiori
def metodo_laplace(matrice):
    ordine_matrice = len(matrice)
    pos = [0, 0]
    determinante = 0
    for _n in range(ordine_matrice): 
        sottomatrice = []
        for r in range(ordine_matrice): # Riga
            nuova_riga = []
            for c in range(ordine_matrice): # Colonna
                if r == pos[0] or c == pos[1]: # Esclusione Riga e Colonna Elemento
                    continue
                else:
                    nuova_riga.append(matrice[r][c])
            if len(nuova_riga) != 0:
                sottomatrice.append(nuova_riga)
        sotto_det = calcolo_determinante(sottomatrice)
        elemento = matrice[pos[0]][pos[1]]
        if is_posizizone_pari(pos):
            determinante += sotto_det * elemento
        else:
            determinante += sotto_det * -elemento
        pos = [0, pos[1] + 1]
    return determinante

# Switch Case per Calcolo
def calcolo_determinante(matrice):
    match len(matrice):
        case 1:
            return matrice[0][0]
        case 2:
            return metodo_diagonale(matrice)
        case 3:
            return metodo_sarrus(matrice)
        case _:
            return metodo_laplace(matrice)


def main():
    if not check_matrice(matrice):
        console.print("[red][Errore] La matrice non è quadrata o non è valida.")
        return 1
    print_mat(matrice, calcolo_determinante(matrice))
    return 0


if __name__ == '__main__':
    main()
