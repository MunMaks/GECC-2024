"""
    GECC 2024 Challenge VII : Casser la routine
    Université Gustave Eiffel 14/04/2024
    MUNAITPASOV Maksat

pylint seventh.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.0/10, +0.00)
"""

import math

def lire_fichier(nom_fichier: str) -> list:
    """
        lire un fichier
    """
    res = []

    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            res.append([int(element) for element in ligne.split()])
    return res


def find_period(a: int, b: int, u_0: int, p: int) -> int:
    """
    a, b, u_0, p sont les paramètres de la suite.
    u_(n+1) = (a * u_n + b) % p

    la fonction va simuler la suite pour trouver sa période.
    """
    seen = {}
    current = u_0
    index = 0
    while current not in seen:
        seen[current] = index
        current = (a * current + b) % p
        index += 1
    return index - seen[current]


def lcm(x: int, y: int) -> int:
    """
    lcm(x, y) calcule le PPCM (plus petit commun multiple) de deux nombres en utilisant
    leur produit divisé par leur PGCD (plus grand commun diviseur).
    ceci est réalisé avec math.gcd(x, y).
    """
    return x * y // math.gcd(x, y)


def lcm_multiple(values: list[int]) -> int:
    """
    lcm_multiple(values) étend cette idée pour une liste de valeurs
    en utilisant lcm() pour calculer le PPCM (plus petit commun multiple)
    """
    current_lcm = values[0]
    for number in values[1:]:
        current_lcm = lcm(current_lcm, number)
    return current_lcm


def main() -> None:
    """
        l'entree de notre programme
    """

    suites = lire_fichier("seven.txt")

    periods = [find_period(a, b, u0, p) for a, b, u0, p in suites]
    # print("Périodes individuelles des suites:", periods)

    # from functools import reduce
    # global_period = reduce(lcm, periods)
    global_period = lcm_multiple(periods)   # obtenir la période globale:

    print("\nPériode globale du 12-uplet:", global_period)  # hex(global_period)
    print("Pourtant, le Platon accepte: 18154357393346734000\n")


if __name__ == '__main__':
    main()
