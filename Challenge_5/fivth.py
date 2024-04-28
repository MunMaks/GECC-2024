"""
    GECC 2024 Challenge V : Remplissage en catastrophe
    Université Gustave Eiffel 12/04/2024
    MUNAITPASOV Maksat

pylint fivth.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.0/10, +0.00)
"""

def remplissages_possibles(produits: list[tuple], capacite_sac: int) -> list[list[str]]:
    """
        Renvoie une liste de tous les remplissages possibles
        du sac à dos avec les produits disponibles.
    """
    n = len(produits)
    res = []

    # tous les remplissages possibles
    def backtrack(index: int, current_weight: int, current_items: list) -> None:
        """
            Backtracking fonction
        """
        if current_weight <= capacite_sac:
            res.append(current_items[:])

        for i in range(index, n):

            current_items.append(produits[i][0])    # ajouter le produit
            current_weight += produits[i][1]        # ajouter son poids

            backtrack(i + 1, current_weight, current_items) # le produit suivant

            # retirer le produit et son poids
            # pour essayer d'autres combinaisons
            current_items.pop()
            current_weight -= produits[i][1]

    backtrack(0, 0, [])
    return res


def remplissages_optimaux(produits: list[tuple], capacite_sac: int):
    """
        Renvoie les remplissages optimaux en espace et en nombre d'objets.
    """
    remplissages = remplissages_possibles(produits, capacite_sac)

    min_objets = 100000     # une valeur grande
    meilleur_remplissages = []

    # le nombre min d'objets parmi tous les remplissages possibles
    for remplissage in remplissages:
        poids_remplissage = sum(poids for _, poids in produits if _ in remplissage)
        if poids_remplissage == capacite_sac:
            min_objets = min(min_objets, len(remplissage))
            meilleur_remplissages.append(remplissage)

    return meilleur_remplissages


def lire_fichier(nom_fichier: str) -> list[tuple]:
    """
        Lit un fichier et renvoie la liste de string
    """
    res = []

    with open(nom_fichier, "r", encoding = "utf-8") as fichier:
        for ligne in fichier:
            ligne = ligne.split()
            nom = " ".join(ligne[:-1])
            poids = int(ligne[-1])
            res.append((nom, poids))
    return res




def result(remplissages: list[list[str]]):
    """
        Calcule le nombre de manieres differentes pour remplir le sac a dos
    """
    if not remplissages:
        return 0

    # sac_curr = sac a dos actuel
    min_length = min(len(sac_curr) for sac_curr in remplissages)
    count = sum(1 for sac_curr in remplissages if len(sac_curr) == min_length)

    return count


def main() -> None:
    """
        l'entree de notre programme
    """

    # a changer si vous voulez essayer votre version
    produits = lire_fichier("five.txt")
    capacite_sac = 17000  # en grammes

    remplissages = remplissages_optimaux(produits, capacite_sac)
    print(f"Le nombre de manières pour remplir sac à dos: {result(remplissages)}")


if __name__ == '__main__':
    main()
