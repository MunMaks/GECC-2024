"""
    GECC 2024 Challenge I : Le message est codé
    Université Gustave Eiffel 08/04/2024
    MUNAITPASOV Maksat

pylint first.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.0/10, +0.00)

le message codé:
abcdefghijklmnopqrstuvwxyz

ock kbgncack zcubnbxjxbsgk ! ystk jyci fabuujoocgx ktaosgxc uc vczb
wtb kc eackcgxjbx j ystk. ysxac njejnbxc j ackstvac vck easfucock ckx yajbocgx
cdncexbsggcuuc. ystk jyci jfsavc uj kbxtjxbsg jycn bgxcuubmcgnc cx vcxcaobgjxbsg,
cx uc acktuxjx ejauc vc utb-ococ. nsgxbgtci j jzzasgxca uck easfucock jycn ncxxc
rjfbucxc acojawtjfuc, nja uc osgvc j fcksbg vc ecaksggck njejfuck vc xastyca vck
ksutxbsgk nsooc ystk uc zjbxck. cgnsac tgc zsbk, xstxck ock zcubnbxjxbsgk esta
ncxxc acjubkjxbsg cdxajsavbgjbac !

fsozbi ejaybgx htkwt'j vbd prbklq-mujnc.


le résultat:
riexpbnjzaskgcmwyhouldqtvf

mes sinceres felicitations ! vous avez brillamment surmonte le defi
qui se presentait a vous. votre capacite a resoudre des problemes est vraiment
exceptionnelle. vous avez aborde la situation avec intelligence et determination,
et le resultat parle de lui-meme. continuez a affronter les problemes avec cette
habilete remarquable, car le monde a besoin de personnes capables de trouver des
solutions comme vous le faites. encore une fois, toutes mes felicitations pour
cette realisation extraordinaire !

bomfiz parvint jusqu'a dix whisky-glace
"""

def calculer_cle(mot: str) -> int:
    """
    Calcule le hash d'apres la formule
    """
    cle = 0
    for idx, lettre in enumerate(mot):
        cle = ((2 * cle) + ((idx + 1) * ord(lettre))) % 1000000

    return cle


def main() -> None:
    """
        l'entree principale
    """
                    # jfnvczmrbhluogsewakxtypdqi
    n = calculer_cle('riexpbnjzaskgcmwyhouldqtvf')

    print(f"Message personnel à déchiffrer, sa clé de déchiffrage: {n}")


if __name__ == '__main__':
    main()
