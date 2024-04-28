"""
    GECC 2024 Challenge III : Tournée d'invitations 
    Université Gustave Eiffel 10/04/2024
    MUNAITPASOV Maksat

pylint third.py    
--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

"""
import itertools    # permutations


def lire_fichier(nom_fichier: str) -> dict:
    """
        lire un fichier d'apres le format suivant:
        Copernic à Lavoisier = 1033
        depart  , , arrive , , pas 
indice:    0     1    2     3   4
    """
    res = {}

    with open(nom_fichier, "r", encoding="utf-8") as fptr:

        for ligne in fptr:
            ligne = ligne.split()
            depart = ligne[0]
            arrive = ligne[2]
            pas = ligne[4]
            res[(depart, arrive)] = int(pas)    # depart, arrive
            res[(arrive, depart)] = int(pas)    # reciproque
    return res


def obtenir_batiments(distances: dict[tuple]) -> list[str]:
    """
        Renvoie la liste de tous les immeubles dans distances
    """
    batiments_set = set()
    for (depart, _) in distances.keys():
        batiments_set.add(depart)
    return list(batiments_set)


def calculate_distance(path: str, distances: dict[tuple]) -> int:
    """
        Effectue les calcul pour le chemins chosis
    """
    distance = 0
    longueur_chemin = len(path)
    for i in range(longueur_chemin - 1):
        distance += distances[(path[i], path[i + 1])]
    return distance


def dijkstra(distances: dict[tuple]) -> tuple:
    """
        Effectue le recherche de chemin le plus court et le plus efficase
    """
    batiments = obtenir_batiments(distances)

    all_permutations = itertools.permutations(batiments)

    meilleure_distance = 100000    # une valeur tres grande
    meilleur_chemin = None

    for permutation in all_permutations:
        for i, batiment in enumerate(permutation):
            for j in range(len(permutation)):

                # pour ne pas avoir deux batiments voisins qui porte le meme nom
                # par exemple ... - IUT - Lavoisier - Lavoisier - ...
                if j not in (i, i - 1, i + 1):

                    chemin_actuel = permutation[:j] + \
                                            (batiment,) + \
                                            permutation[j:]

                    # la distance de chemin aleatoire
                    curr_dist = calculate_distance(chemin_actuel, distances)

                    # mettre a jour la distance
                    if curr_dist < meilleure_distance:
                        meilleure_distance = curr_dist
                        meilleur_chemin = chemin_actuel

    return meilleure_distance, meilleur_chemin


def main() -> None:
    """
        Main function
    """
    distances = lire_fichier("three.txt")

    resultat, chemin = dijkstra(distances)
    print(f"le chemin: \n{chemin} et l'inverse \n{chemin[::-1]}\n")
    print(f"La distance entre les 7 batiments est de : {resultat}")


if __name__ == '__main__':
    main()
