### GECC 2024 Challenge III : Tournée d'invitations
Comme la date du pique-nique approche, il est temps pour vous de faire le tour de la cité Descartes
pour y inviter d'autres informaticiens dispersésun peu partout dans différents bâtiments.

<div align="center">
  <img src="https://github.com/MunMaks/GECC-2024/blob/main/Challenge_3/descartes.png" alt="image1" width="500" height="330">
</div>

En grand optimisateur, vous envisagez de profiter des deux heures de pause déjeuner pour distribuer en personne quelques invitations que vous avez soigneusement chiffrées.
Cependant, la pause déjeuner est également l'heure du repas et il est essentiel que vous consommiez votre propre repas.
Il est nécessaire de tenir toute la journée, donc il est important de manger un plat chaud pendant la pause déjeuner.
Sachant bien que vous connaissez la cité Descartes, vous savez parfaitement où trouver un four micro-ondes dans n'importe quel bâtiment que vous envisagez de visiter.

Après réflexion, vous planifiez un itinéraire passant par les 7 bâtiments suivants : 
le bâtiment Alexandra David-Néel, l'ESIEE, l'IUT, le bâtiment Copernic, le bâtiment Lavoisier, la Centrif', ainsi que le bâtiment Bienvenüe.
De plus, vous recherchez un trajet où vous pourrez réchauffer votre gamelle dans un micro-ondes et la récupérer plus tard une fois qu'elle sera chaude.
Le point de départ et d'arrivée n'ont pas d'importance, vous vous adapterez.
Cependant, vous devrez choisir un bâtiment que vous traverserez deux fois.
Étant donné que le temps de chauffe du micro-ondes est non négligeable, il n'est pas possible d'envisager un itinéraire qui passe deux fois de suite par le même bâtiment.
C'est à la fois compliqué et astucieux, à l'image de l'humour des scientifiques.
Ainsi, vous aurez un itinéraire optimal pour distribuer vos 7 invitations tout en prenant votre pause repas.


Un de vos collègues a calculé le nombre de pas nécessaire pour aller d'un bâtiment à un autre en utilisant des raccourcis piétons.
À partir de ces distances en nombre de pas,
veuillez calculer le nombre minimal de pas qui permettra de suivre le chemin optimal tout en tenant compte de votre contrainte de déjeuner.

<b>
Calculer le nombre de pas du trajet le plus court passant par les 7 bâtiments et même deux fois par un des 7 bâtiments (n'importe lequel mais pas de manière consécutive).
</b>

Voici vos données personnalisées pour ce challenge qui représentent le nombre de pas entre chaque couple de bâtiments :
```
David-Néel à ESIEE = 910
David-Néel à IUT = 1113
David-Néel à Copernic = 909
David-Néel à Lavoisier = 803
David-Néel à Centrif' = 973
David-Néel à Bienvenüe = 1084
ESIEE à IUT = 990
ESIEE à Copernic = 1208
ESIEE à Lavoisier = 955
ESIEE à Centrif' = 1231
ESIEE à Bienvenüe = 787
IUT à Copernic = 827
IUT à Lavoisier = 880
IUT à Centrif' = 927
IUT à Bienvenüe = 1104
Copernic à Lavoisier = 1033
Copernic à Centrif' = 1202
Copernic à Bienvenüe = 1183
Lavoisier à Centrif' = 1134
Lavoisier à Bienvenüe = 1051
Centrif' à Bienvenüe = 1217
```
