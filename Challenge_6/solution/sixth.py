"""
    GECC 2024 Challenge VI : Joyeux plan de table
    Université Gustave Eiffel 13/04/2024
    MUNAITPASOV Maksat

pylint sixth.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.0/10, +0.00)
"""
import itertools    # permutations


def lire_fichier(nom_fichier: str) -> tuple:
    """
        Pour lire le fichier et renvoie deux dictionnaires souhaitées

        # le format de chaque ligne:
        #      "Personne_1", "Action", "Combien", "...", "...",
        #            "...", "...", "...", "...", "Où", "...", "Personne_2"

        # ligne = ['Vous', 'perdriez', '1316', 'unités', 'de', \
        #            'joie', 'en', 'étant', 'à', 'coté', 'de', 'Carine.']

        # ligne = ['Carine', 'perdrait', '825', 'unités', 'de', \
        #            'joie', 'en', 'étant', 'en', 'face', 'de', 'Philippe.']
    """

    voisins = {}
    face_de = {}

    with open(nom_fichier, "r", encoding='utf-8') as fichier:
        gagne = ["gagneriez", "gagnerait"]
        # perd = ["perdriez", "perdrait"]   # supplémentaire

        for ligne in fichier:
            ligne = ligne.split()

            premier = ligne[0]
            deuxieme = ligne[-1][:-1]
            joie = int(ligne[2])

            if ligne[9] == "coté":
                voisins[(premier, deuxieme)] = joie if ligne[1] in gagne else -joie
            else:   # ligne[9] == ligne[-3] == "face"
                face_de[(premier, deuxieme)] = joie if ligne[1] in gagne else -joie

    return voisins, face_de


def voisins_et_en_face(indice: int, size: int) -> tuple:
    """
        Renvoie les indices des voisins et personnes qui sont en face
    """
    voisin_gauche = (indice - 1) % size
    voisin_droite = (indice + 1) % size

    face_de_gauche = (indice + (size // 2)) % size
    face_de_droite = (indice + (size // 2) + 1) % size

    return (voisin_gauche, voisin_droite,\
            face_de_gauche, face_de_droite)


def calcule_enneagone(enneagone: tuple, voisins: dict,\
                                 face_de: dict) -> int:
    """
        Renvoie la joie total d'un arrangement demandée
    """
    joie_totale = 0
    for indice, personne in enumerate(enneagone):
        voisin_un, voisin_deux, face_de_un, face_de_deux = \
            voisins_et_en_face(indice, size=9)

        joie_totale += voisins.get((personne, enneagone[voisin_un]), 0)
        joie_totale += voisins.get((personne, enneagone[voisin_deux]), 0)

        joie_totale += face_de.get((personne, enneagone[face_de_un]), 0)
        joie_totale += face_de.get((personne, enneagone[face_de_deux]), 0)

    return joie_totale


def meilleur_enneagone(personnes: list[str], voisins: dict, \
                       face_de: dict) -> int:
    """
        Renvoie le maximum de joie que peut atteindre la tablee 
    """
    permutations_personnes = itertools.permutations(personnes)
    max_joie = 0
    optimal_enneagone = None
    # compteur = 1

    for enneagone in permutations_personnes:
        joie = calcule_enneagone(enneagone, voisins, face_de)

        if joie >= max_joie:
            # compter le nombre de enneagones possibles
            # compteur = compteur + 1 if joie == max_joie else 1

            max_joie = joie
            optimal_enneagone = enneagone

    # print(f"il y a {compteur} enneagones possibles")
    return max_joie, optimal_enneagone


def main() -> None:
    """
        l'entree de notre programme
    """
    personnes = ['Vous', 'Carine', 'Daniel', 'Chloé', \
                'David', 'Nawel', 'Denis', 'Tita', 'Philippe']

    # a changer si vous voulez essayer votre propre version
    voisins_map, face_de_map = lire_fichier("six.txt")

    joie_max, enneagone_max = meilleur_enneagone(personnes, voisins_map, face_de_map)

    print(f"result: {joie_max}\nl'enneagone : {enneagone_max}")


if __name__ == '__main__':
    main()
