"""
    GECC 2024 Challenge IV : La moto à Zipstein
    Université Gustave Eiffel 11/04/2024
    MUNAITPASOV Maksat

pylint fourth.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.0/10, +0.00)
"""


def lire_fichier_et_ajouter_liste(nom_fichier: str) -> list[str]:
    """
        lire un fichier et renvoie la liste de string
    """
    lignes = []

    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            lignes.append(ligne.strip())

    return lignes


def valid_idx(engines: list[str], i: int, j: int) -> bool:
    """
        Renvoie True si les indices sont bonnes
    """
    return (0 <= i < len(engines)) and\
            (0 <= j < len(engines[i]))



def number_from_str(engines: list[str], i: int, j: int) -> int:
    """
        Renvoie un nombre d'apres ses coordonees
        pour voir les cases voisines
    """
    res = ''
    idx = 0

    if valid_idx(engines, i, j - 1) and (engines[i][j - 1].isdigit()):
        idx -= 1
        if valid_idx(engines, i, j - 2) and (engines[i][j - 2].isdigit()):
            idx -= 1

    for cmpt in (idx, idx + 1, idx + 2):
        if valid_idx(engines, i, j + cmpt) and engines[i][j + cmpt].isdigit():
            res += engines[i][j + cmpt]
        else:
            break

    return int(res)




def only_two_nums(engines: list[str], i: int, j: int) -> list:
    """
        Renvoie deux nombres differents d'apres les cases voisines
    """

    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0),           (1, 0),
                  (-1, 1),  (0, 1),  (1, 1)]

    numbers_set = set()
    coords_i, coords_j = 0, 0

    for x, y in directions:
        coords_i, coords_j = i + x, j + y

        if valid_idx(engines, coords_i, coords_j) and \
            engines[coords_i][coords_j].isdigit():
            number = number_from_str(engines, coords_i, coords_j)
            numbers_set.add(number)
            if len(numbers_set) == 2:
                break

    return list(numbers_set)




def nearby_number(engines: list[str], row: int, col: int) -> bool:
    """
        Renvoie True s'il y a un nombre dans les cases voisines
        sinon False
    """
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (valid_idx(engines, row + i, col + j)) and\
                engines[row + i][col + j].isdigit():
                return True
    return False



def simplifier_engine(engines: list[str]) -> list[str]:
    """
        Nettoyage des symboles inutiles
    """
    row, col = len(engines), len(engines[0])

    engines_simple = [[' '] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if engines[i][j] in ['*', '#'] and nearby_number(engines, i, j):
                engines_simple[i][j] = engines[i][j]
            elif engines[i][j].isdigit():
                engines_simple[i][j] = engines[i][j]

    return engines_simple


def calcul_puiss(engines_simple: list[str]) -> int:
    """
        Calcule la puissance d'apres liste de string
    """
    row, col = len(engines_simple), len(engines_simple[0])

    total_power_add = 0     # addition
    total_power_sous = 0    # soustraction

    for i in range(row):
        for j in range(col):

            if engines_simple[i][j] == "*":
                lst = only_two_nums(engines_simple, i, j)
                if len(lst) == 2:
                    total_power_add += abs(lst[0] * lst[1])

            elif engines_simple[i][j] == "#":
                lst = only_two_nums(engines_simple, i, j)
                if len(lst) == 2:
                    total_power_sous -= abs(lst[0] * lst[1])

    return total_power_add + total_power_sous



def main() -> None:
    """
        l'entree de notre programme
    """
    new_engines = lire_fichier_et_ajouter_liste("four.txt")
    engines_simple = simplifier_engine(new_engines)
    print(f"resultat: {calcul_puiss(engines_simple)}")


if __name__ == '__main__':
    main()
