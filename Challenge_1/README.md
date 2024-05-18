### GECC 2024 Challenge I : Le message est codé
Vous avez reçu un nouveau message.

On dit que César chiffrait ses messages par décalage dans l'alphabet, malheureusement ici, c'est un peu plus compliqué.
Le chiffrement qui a été appliqué est une permutation aléatoire de l'alphabet latin (toutefois, que des minuscules et sans accent, donc seulement 26 symboles).
Mais la factorielle de 26, c'est déjà énorme et tester toutes les permutations pour déchiffrer le message ne semble pas une bonne stratégie.
Le message est en langue française et utilise toutes les lettres de l'alphabet latin. Sans plus d'information, vous devez déchiffrer votre message personnel.
Les caractères autres que les lettres minuscules (espaces, tirets et retours à la ligne) restent inchangés durant chiffrage et déchiffrage.


![image](https://github.com/MunMaks/GECC-2024/assets/98954111/039b697c-3e5c-47ed-895a-b2dc60aa370e)

Imaginons un instant que votre message chiffré soit le suivant :
```
abcdefghijklmnopqrstuvwxyz

elfh evmva wv wvxibkgvi xvg rmxilbzyov nvhhztv.

yzxsva oz jfvfv wf dztlm-gzcr zevx ovh kbqznzh wf uzpri.
```


Le premier mot, qui n'est pas un mot de la langue française, sera toujours l'ensemble des lettres de l'alphabet latin accolées.
Ici, même si ça ne saute pas au yeux, l'alphabet a été complètement renversé (inversion de a et z, b et y, c et x, etc...).

Le déchiffrement est donc un nouveau renversement complet qui devrait remettre les lettres dans le bon ordre.
Ainsi, "abcdefghijklmonpqrstuvwxyz" va devenir "zyxwvutsrqponmlkjihgfedcba" durant le déchiffrement.
Appliquant la règle sur tout le message, on arrive à reconstituer le texte qui suit.


Votre message, bien que généré aléatoirement, contiendra systématiquement toutes les lettres de l'alphabet latin.
Dans l'exemple au dessus, la dernière phrase est bien un pangramme, c'est à dire une phrase contenant au moins toutes les lettres latines de a à z.
Ces phrases sont souvent utilisées en calligraphie et pour illustrer les polices de caractères.


Ceci fait, il faudra maintenant calculer la clé prouvant votre résolution du problème; illustrant le fait que vous avez bel et bien déchiffrer votre message personnel.
La clé sera une grande valeur numérique entière construite à partir de la version déchiffrée de l'expression "abcdefghijklmonpqrstuvwxyz".
Ce calcul, associant un nombre entier à toute chaîne de caractères, a les caractéristiques d'une fonction de hashage (pour ceux qui connaissent).


Voici comment établir la clé numérique, cette dernière est calculée récursivement.
La clé du mot vide "" sera 0 par convention.
Ensuite pour tout mot ayant une dernière lettre c, donc de la forme wc avec w le sous mot préfixe contenant toutes les lettres sauf la dernière, la clé numérique sera:


$\\text{key}(wc) = \left( 2 \times \text{key}(w) + \text{position}(c) \times \text{ascii}(c) \right) \mod 1000000 \$


où $position(c)$ est un entier décrivant la position de $c$ dans le mot $wc$ ($1$ pour la première lettre, $2$ pour la seconde, ..., $n$ pour la $n^{ième}$ lettre )
et $ascii(c)$ est l'entier associé au symbole latin dans le code ascii.
Cette valeur dans le code ascii doit être entre $97$ et $122$ car les messages (et en particulier la première ligne) ne contiennent que des lettres minuscules.
En appliquant pas à pas la formule sur l'alphabet renversé, on obtiendrait ainsi les calculs suivants :

```
0                                                    # ""
122  = (2 * 0  + ( 1 ) * 122 ) % 1000000             # "z"
486  = (2 * 122  + ( 2 ) * 121 ) % 1000000           # "zy"
1332  = (2 * 486  + ( 3 ) * 120 ) % 1000000          # "zyx"
3140  = (2 * 1332  + ( 4 ) * 119 ) % 1000000         # "zyxw"
6870  = (2 * 3140  + ( 5 ) * 118 ) % 1000000         # "zyxwv"
14442  = (2 * 6870  + ( 6 ) * 117 ) % 1000000        # "zyxwvu"
29696  = (2 * 14442  + ( 7 ) * 116 ) % 1000000       # "zyxwvut"
60312  = (2 * 29696  + ( 8 ) * 115 ) % 1000000       # "zyxwvuts"
121650  = (2 * 60312  + ( 9 ) * 114 ) % 1000000      # "zyxwvutsr"
244430  = (2 * 121650  + ( 10 ) * 113 ) % 1000000    # "zyxwvutsrq"
490092  = (2 * 244430  + ( 11 ) * 112 ) % 1000000    # "zyxwvutsrqp"
981516  = (2 * 490092  + ( 12 ) * 111 ) % 1000000    # "zyxwvutsrqpo"
964462  = (2 * 981516  + ( 13 ) * 110 ) % 1000000    # "zyxwvutsrqpon"
930450  = (2 * 964462  + ( 14 ) * 109 ) % 1000000    # "zyxwvutsrqponm"
862520  = (2 * 930450  + ( 15 ) * 108 ) % 1000000    # "zyxwvutsrqponml"
726752  = (2 * 862520  + ( 16 ) * 107 ) % 1000000    # "zyxwvutsrqponmlk"
455306  = (2 * 726752  + ( 17 ) * 106 ) % 1000000    # "zyxwvutsrqponmlkj"
912502  = (2 * 455306  + ( 18 ) * 105 ) % 1000000    # "zyxwvutsrqponmlkji"
826980  = (2 * 912502  + ( 19 ) * 104 ) % 1000000    # "zyxwvutsrqponmlkjih"
656020  = (2 * 826980  + ( 20 ) * 103 ) % 1000000    # "zyxwvutsrqponmlkjihg"
314182  = (2 * 656020  + ( 21 ) * 102 ) % 1000000    # "zyxwvutsrqponmlkjihgf"
630586  = (2 * 314182  + ( 22 ) * 101 ) % 1000000    # "zyxwvutsrqponmlkjihgfe"
263472  = (2 * 630586  + ( 23 ) * 100 ) % 1000000    # "zyxwvutsrqponmlkjihgfed"
529320  = (2 * 263472  + ( 24 ) * 99 ) % 1000000     # "zyxwvutsrqponmlkjihgfedc"
61090  = (2 * 529320  + ( 25 ) * 98 ) % 1000000      # "zyxwvutsrqponmlkjihgfedcb"
124702  = (2 * 61090  + ( 26 ) * 97 ) % 1000000      # "zyxwvutsrqponmlkjihgfedcba"
```



La clé (ou valeur de hachage) de "zyxwvutsrqponmlkjihgfedcba" est donc <b><i>124702</i></b> et cela serait votre solution au problème
si des fois votre alphabet serait complètement renversé durant le déchiffrement 
(ce qui a peu de chance d'arriver : $1$ chance sur $26! = 403291461126605635584000000$).

Voici vos données personnalisées pour ce challenge. Il s'agit de votre message personnel à déchiffrer, quelle est sa clé de déchiffrage ?

```
abcdefghijklmnopqrstuvwxyz

ock kbgncack zcubnbxjxbsgk ! ystk jyci fabuujoocgx ktaosgxc uc vczb
wtb kc eackcgxjbx j ystk. ysxac njejnbxc j ackstvac vck easfucock ckx yajbocgx
cdncexbsggcuuc. ystk jyci jfsavc uj kbxtjxbsg jycn bgxcuubmcgnc cx vcxcaobgjxbsg,
cx uc acktuxjx ejauc vc utb-ococ. nsgxbgtci j jzzasgxca uck easfucock jycn ncxxc
rjfbucxc acojawtjfuc, nja uc osgvc j fcksbg vc ecaksggck njejfuck vc xastyca vck
ksutxbsgk nsooc ystk uc zjbxck. cgnsac tgc zsbk, xstxck ock zcubnbxjxbsgk esta
ncxxc acjubkjxbsg cdxajsavbgjbac !

fsozbi ejaybgx htkwt'j vbd prbklq-mujnc.
```


