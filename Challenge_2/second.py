"""
    GECC 2024 Challenge II : Émulsion et coagulation
    Université Gustave Eiffel 09/04/2024
    MUNAITPASOV Maksat

pylint second.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.0/10, +0.00)
"""


def lire_fichier(nom_fichier: str) -> tuple:
    """
        Effectue la lecture d'un fichier
    """
    lignes = []

    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            lignes.append(ligne.strip())

    return lignes



def transforme(array_str: list[str]) -> list[list[int]]:
    """
        Transforme une liste de strings en liste de liste d'entiers
    """
    return [[int(number) for number in mot] for mot in array_str]



def trouver_voisins(grille: list[list[int]], i: int, j: int) -> list[tuple]:
    """
        Trouve les voisins d'un pixel dans une grille
    """
    voisins = []
    directions = [  (0, 1),     # a droite
                    (0, -1),    # a gauche
                    (1, 0),     # en bas
                    (-1, 0) ]   # en haut

    row, col = len(grille), len(grille[0])

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < row and 0 <= nj < col:
            voisins.append((ni, nj))

    return voisins



def explorer_zone(grille: list[list[int]], i: int, j: int,\
                  couleur: int, visite: list[list[int]]) -> int:
    """
        Explore une zone de pixels voisins de même couleur
    """
    # deja vu ou n'est pas la meme couleur
    if visite[i][j] or grille[i][j] != couleur:
        return 0

    visite[i][j] = 1    # deja vu
    poids = 1
    for ni, nj in trouver_voisins(grille, i, j):
        poids += explorer_zone(grille, ni, nj, couleur, visite)
    return poids



def facteur_coagulation(grille: list[list[int]]):
    """
        Calcule le facteur de coagulation
    """
    row, col = len(grille), len(grille[0])
    visite = [ [0 for _ in range(row)] for _ in range(col) ]
    facteur = 0

    for i in range(row):
        for j in range(col):
            if not visite[i][j]:

                couleur = grille[i][j]      # couleur = {1, ..., 9}

                poids_zone = explorer_zone(grille, i, j, couleur, visite) - 1

                if poids_zone > 0:
                    facteur += poids_zone
    return facteur



def main() -> None:
    """
        l'entree de notre programme
    """
    echantillon_2 = lire_fichier("two.txt")     # a changer si vous voulez avoir autre resultat

    array_num = transforme(echantillon_2)

    resultat = facteur_coagulation(array_num)

    print("Le facteur de coagulation est :", resultat)


if __name__ == '__main__':
    main()