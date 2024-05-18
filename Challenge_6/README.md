### GECC 2024 Challenge VI : Joyeux plan de table
Tout le monde est là, c'est l'heure du pique-nique, et huit informaticiens en plus de vous-même ont répondu présent pour ce repas de fin d'année.
Le retour à moto s'est bien déroulé et vous voilà arrivé sur place avec les denrées alimentaires qui vont bien.

En tant qu'immense optimisateur que vous êtes et comme vous souhaitez que le niveau des conversations soit d'un très haut niveau scientifique,
vous réalisez que le plan de table doit absolument mettre toutes les chances de votre côté pour que ce moment de convivialité soit une réussite critique.

Vous allez vous retrouver à 9 autour d'une table parfaitement régulière en forme d'ennéagone (le nom des polygones à 9 côtés).
Chaque convive sera assis à l'un des neuf coins de la table. Chaque convive a deux voisins : un à sa gauche et un à sa droite.
Comme 9 est un nombre impair, chaque convive placé voit aussi 2 personnes en face de lui.
Chaque sommet étant en face d'une arête, ce sont les deux personnes aux coins de cette arête opposée qui sont considérées comme étant en face.
Regardons cela sur un schéma :

<br>

<div align="center">
  <img src="https://github.com/MunMaks/GECC-2024/blob/main/Challenge_6/table.png" alt="image1" width="300" height="300">
</div>

<br>

Les convives seront installés aux coins de l'ennéagone.
Pointons un convive en particulier, celui en rouge foncé.
Ses deux voisins `(V)` du convive au point rouge sont en vert foncé et les deux convives en face `(F)` sont aux points bleus.

Chacun des 9 convives (dont vous-même) arrive au pique-nique de manière neutre avec 0 unité de joie,
mais la joie de chaque convive est affectée à la hausse ou à la baisse par les personnes voisines et les personnes situées en face.
Pour le convive placé au point rouge, les deux voisins `(V)` et les deux personnes en face `(F)` peuvent influer sur sa joie.
La joie de toute la tablée est la somme des joies des 9 convives présents au pique-nique.
Vous avez réalisé une enquête préalable pour savoir comment la joie de chacun serait affectée en fonction des personnes à côté ou en face.
Les résultats de cette enquête sont vos données personnalisées pour ce challenge.

La clé pour résoudre ce challenge est le maximum d'unités de joie que peut atteindre la tablée parmi tous les placements possibles des 9 convives.

Les neuf convives sont des informaticiens de la cité Descartes :
```Carine, Daniel, Chloé, David, Nawel, Denis, Tita, Philippe et vous-même.```

<br>
<b>
Parmi tous les placements possibles des convives, quel est le maximum de joie que peut atteindre la tablée ?
</b>

<br>
<br>
Voici vos données personnalisées pour ce challenge :
<br>

```
Vous perdriez 1316 unités de joie en étant à coté de Carine.
Vous perdriez 946 unités de joie en étant en face de Carine.
Vous gagneriez 387 unités de joie en étant à coté de Daniel.
Vous gagneriez 195 unités de joie en étant en face de Daniel.
Vous perdriez 450 unités de joie en étant à coté de Chloé.
Vous perdriez 406 unités de joie en étant en face de Chloé.
Vous gagneriez 825 unités de joie en étant à coté de David.
Vous gagneriez 457 unités de joie en étant en face de David.
Vous perdriez 340 unités de joie en étant à coté de Nawel.
Vous perdriez 340 unités de joie en étant en face de Nawel.
Vous perdriez 94 unités de joie en étant à coté de Denis.
Vous gagneriez 731 unités de joie en étant en face de Denis.
Vous perdriez 1368 unités de joie en étant à coté de Tita.
Vous perdriez 102 unités de joie en étant en face de Tita.
Vous perdriez 737 unités de joie en étant à coté de Philippe.
Vous perdriez 139 unités de joie en étant en face de Philippe.
Carine gagnerait 1192 unités de joie en étant à coté de Vous.
Carine gagnerait 883 unités de joie en étant en face de Vous.
Carine gagnerait 231 unités de joie en étant à coté de Daniel.
Carine gagnerait 602 unités de joie en étant en face de Daniel.
Carine gagnerait 725 unités de joie en étant à coté de Chloé.
Carine gagnerait 448 unités de joie en étant en face de Chloé.
Carine perdrait 155 unités de joie en étant à coté de David.
Carine perdrait 268 unités de joie en étant en face de David.
Carine gagnerait 1078 unités de joie en étant à coté de Nawel.
Carine perdrait 271 unités de joie en étant en face de Nawel.
Carine gagnerait 565 unités de joie en étant à coté de Denis.
Carine gagnerait 440 unités de joie en étant en face de Denis.
Carine perdrait 850 unités de joie en étant à coté de Tita.
Carine perdrait 280 unités de joie en étant en face de Tita.
Carine gagnerait 1207 unités de joie en étant à coté de Philippe.
Carine perdrait 825 unités de joie en étant en face de Philippe.
Daniel gagnerait 216 unités de joie en étant à coté de Vous.
Daniel gagnerait 431 unités de joie en étant en face de Vous.
Daniel perdrait 1430 unités de joie en étant à coté de Carine.
Daniel gagnerait 924 unités de joie en étant en face de Carine.
Daniel gagnerait 289 unités de joie en étant à coté de Chloé.
Daniel perdrait 14 unités de joie en étant en face de Chloé.
Daniel perdrait 572 unités de joie en étant à coté de David.
Daniel gagnerait 835 unités de joie en étant en face de David.
Daniel gagnerait 201 unités de joie en étant à coté de Nawel.
Daniel gagnerait 453 unités de joie en étant en face de Nawel.
Daniel perdrait 110 unités de joie en étant à coté de Denis.
Daniel gagnerait 268 unités de joie en étant en face de Denis.
Daniel gagnerait 1388 unités de joie en étant à coté de Tita.
Daniel gagnerait 446 unités de joie en étant en face de Tita.
Daniel perdrait 75 unités de joie en étant à coté de Philippe.
Daniel gagnerait 222 unités de joie en étant en face de Philippe.
Chloé perdrait 1259 unités de joie en étant à coté de Vous.
Chloé perdrait 710 unités de joie en étant en face de Vous.
Chloé gagnerait 1258 unités de joie en étant à coté de Carine.
Chloé gagnerait 97 unités de joie en étant en face de Carine.
Chloé perdrait 166 unités de joie en étant à coté de Daniel.
Chloé gagnerait 12 unités de joie en étant en face de Daniel.
Chloé gagnerait 1110 unités de joie en étant à coté de David.
Chloé gagnerait 366 unités de joie en étant en face de David.
Chloé perdrait 672 unités de joie en étant à coté de Nawel.
Chloé gagnerait 356 unités de joie en étant en face de Nawel.
Chloé gagnerait 1398 unités de joie en étant à coté de Denis.
Chloé perdrait 88 unités de joie en étant en face de Denis.
Chloé perdrait 585 unités de joie en étant à coté de Tita.
Chloé perdrait 549 unités de joie en étant en face de Tita.
Chloé perdrait 945 unités de joie en étant à coté de Philippe.
Chloé gagnerait 313 unités de joie en étant en face de Philippe.
David gagnerait 1471 unités de joie en étant à coté de Vous.
David perdrait 280 unités de joie en étant en face de Vous.
David perdrait 236 unités de joie en étant à coté de Carine.
David perdrait 894 unités de joie en étant en face de Carine.
David gagnerait 1195 unités de joie en étant à coté de Daniel.
David perdrait 671 unités de joie en étant en face de Daniel.
David perdrait 799 unités de joie en étant à coté de Chloé.
David gagnerait 819 unités de joie en étant en face de Chloé.
David gagnerait 193 unités de joie en étant à coté de Nawel.
David perdrait 86 unités de joie en étant en face de Nawel.
David perdrait 1352 unités de joie en étant à coté de Denis.
David gagnerait 944 unités de joie en étant en face de Denis.
David perdrait 652 unités de joie en étant à coté de Tita.
David perdrait 984 unités de joie en étant en face de Tita.
David perdrait 1153 unités de joie en étant à coté de Philippe.
David gagnerait 322 unités de joie en étant en face de Philippe.
Nawel gagnerait 942 unités de joie en étant à coté de Vous.
Nawel gagnerait 34 unités de joie en étant en face de Vous.
Nawel gagnerait 961 unités de joie en étant à coté de Carine.
Nawel perdrait 241 unités de joie en étant en face de Carine.
Nawel perdrait 979 unités de joie en étant à coté de Daniel.
Nawel gagnerait 298 unités de joie en étant en face de Daniel.
Nawel gagnerait 224 unités de joie en étant à coté de Chloé.
Nawel gagnerait 90 unités de joie en étant en face de Chloé.
Nawel perdrait 58 unités de joie en étant à coté de David.
Nawel perdrait 435 unités de joie en étant en face de David.
Nawel perdrait 1313 unités de joie en étant à coté de Denis.
Nawel perdrait 607 unités de joie en étant en face de Denis.
Nawel perdrait 1395 unités de joie en étant à coté de Tita.
Nawel gagnerait 247 unités de joie en étant en face de Tita.
Nawel gagnerait 422 unités de joie en étant à coté de Philippe.
Nawel gagnerait 578 unités de joie en étant en face de Philippe.
Denis gagnerait 448 unités de joie en étant à coté de Vous.
Denis gagnerait 323 unités de joie en étant en face de Vous.
Denis gagnerait 1466 unités de joie en étant à coté de Carine.
Denis gagnerait 848 unités de joie en étant en face de Carine.
Denis gagnerait 73 unités de joie en étant à coté de Daniel.
Denis gagnerait 844 unités de joie en étant en face de Daniel.
Denis gagnerait 1439 unités de joie en étant à coté de Chloé.
Denis perdrait 289 unités de joie en étant en face de Chloé.
Denis gagnerait 19 unités de joie en étant à coté de David.
Denis gagnerait 152 unités de joie en étant en face de David.
Denis perdrait 34 unités de joie en étant à coté de Nawel.
Denis perdrait 757 unités de joie en étant en face de Nawel.
Denis gagnerait 1085 unités de joie en étant à coté de Tita.
Denis perdrait 116 unités de joie en étant en face de Tita.
Denis gagnerait 1242 unités de joie en étant à coté de Philippe.
Denis perdrait 407 unités de joie en étant en face de Philippe.
Tita perdrait 764 unités de joie en étant à coté de Vous.
Tita gagnerait 103 unités de joie en étant en face de Vous.
Tita gagnerait 590 unités de joie en étant à coté de Carine.
Tita gagnerait 587 unités de joie en étant en face de Carine.
Tita perdrait 716 unités de joie en étant à coté de Daniel.
Tita gagnerait 924 unités de joie en étant en face de Daniel.
Tita gagnerait 451 unités de joie en étant à coté de Chloé.
Tita perdrait 633 unités de joie en étant en face de Chloé.
Tita perdrait 1373 unités de joie en étant à coté de David.
Tita perdrait 244 unités de joie en étant en face de David.
Tita perdrait 1155 unités de joie en étant à coté de Nawel.
Tita perdrait 223 unités de joie en étant en face de Nawel.
Tita perdrait 1364 unités de joie en étant à coté de Denis.
Tita perdrait 949 unités de joie en étant en face de Denis.
Tita perdrait 464 unités de joie en étant à coté de Philippe.
Tita gagnerait 935 unités de joie en étant en face de Philippe.
Philippe gagnerait 1261 unités de joie en étant à coté de Vous.
Philippe perdrait 749 unités de joie en étant en face de Vous.
Philippe gagnerait 752 unités de joie en étant à coté de Carine.
Philippe gagnerait 922 unités de joie en étant en face de Carine.
Philippe perdrait 117 unités de joie en étant à coté de Daniel.
Philippe perdrait 188 unités de joie en étant en face de Daniel.
Philippe gagnerait 467 unités de joie en étant à coté de Chloé.
Philippe gagnerait 983 unités de joie en étant en face de Chloé.
Philippe perdrait 30 unités de joie en étant à coté de David.
Philippe perdrait 833 unités de joie en étant en face de David.
Philippe perdrait 1015 unités de joie en étant à coté de Nawel.
Philippe gagnerait 475 unités de joie en étant en face de Nawel.
Philippe gagnerait 889 unités de joie en étant à coté de Denis.
Philippe perdrait 483 unités de joie en étant en face de Denis.
Philippe gagnerait 1062 unités de joie en étant à coté de Tita.
Philippe perdrait 869 unités de joie en étant en face de Tita.
```
