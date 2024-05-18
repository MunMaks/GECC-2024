### GECC 2024 Challenge V : Remplissage en catastrophe

Heureusement qu'il restait suffisamment de sans-plomb dans la moto.
Tout en restant raisonnable sur la route, vous êtes arrivé relativement rapidement chez vous.
Il n'est plus question de perdre davantage de temps, chaque seconde compte.
Vous ne devez pas non plus vous mettre en danger pour le chemin du retour.
En grand optimisateur que vous êtes, vous mesurez chacun de vos gestes pour être à la fois rapide et efficace.

Sur la moto et pour des raisons de sécurité, vous vous limiterez à votre fidèle sac à dos.
Celui-ci, bien robuste, peut contenir 17000 grammes d'emport (soit 17 kilos) sans risquer de craquer.
En dessous de cette limite de poids, vous n'utiliseriez pas de manière optimale votre sac à dos ; au-dessus, vous risqueriez de tout perdre durant le voyage.


<div align="center">
  <img src="https://github.com/MunMaks/GECC-2024/blob/main/Challenge_5/pic-nic.jpg" alt="image1" width="400" height="300">
</div>


Vous arrivez devant votre frigo avec votre sac à dos vide, et votre esprit fulgurant établit en un éclair la stratégie à adopter.
En tant que grand esprit, vous devez absolument remplir votre sac à dos à sa taille nominale, mais aussi opérer ce remplissage en un nombre minimal de mouvements.
Il vous faut donc un remplissage optimal en espace et en temps, car chaque seconde compte et votre capacité d'emport est limitée à 17 kilos de produits.

Dans le but de mesurer les possibilités, il vous faut calculer le nombre de remplissages optimaux en espace et en nombre de mouvements,
compte tenu du contenu de votre frigo ainsi que de la taille de votre sac.
Imaginons un instant que votre sac à dos n'ait qu'une capacité de 3000 grammes (3 kilos) et
que les plats disponibles soient seulement les produits suivants avec leur nom suivi de leur poids en grammes :
```
Céleri rémoulade 750
Bière artisanale 1500
Pommes Reinettes 2250
Olives à la grecque 750
Rôti de dinde 1500
```

Il y aurait alors `5` remplissages complets du sac à dos mais seulement `3` remplissages avec un nombre minimal d'objet. Les cinq remplissages complets sont :

```
* Céleri rémoulade, Bière artisanale, Olives à la grecque
* Céleri rémoulade, Pommes Reinettes
* Céleri rémoulade, Olives à la grecque, Rôti de dinde
* Bière artisanale, Rôti de dinde
* Pommes Reinettes, Olives à la grecque
```

Parmi ces `5` remplissages complets du sac à dos, les deux remplissages composés de trois produits ne sont pas minimaux en nombre d'objet.

Ainsi seuls les `3` remplissages suivants seraient optimaux en espace et en temps.

```
* Céleri rémoulade, Pommes Reinettes
* Bière artisanale, Rôti de dinde
* Pommes Reinettes, Olives à la grecque
```

Dans ce cas là, la réponse au challenge aurait été `3`.

<b>
Calculez le nombre de manières différentes de remplir complètement votre sac à dos avec un nombre minimal d'objet?
</b>


<br>On rappel que votre sac à dos à une capacité de `17000` grammes.

Voici aussi les produits possibles qui sont aussi des données personnalisées pour ce challenge :

```
Cabernet sauvignon 2500
Houmous pimenté 2050
Beignets de crevettes 1050
Bâtonnets de carotte 1200
Mayonnaise maison 1300
Toasts au saumon 1500
Muscat de Frontignan 2900
Fourme d'Ambert 1950
Jus d'ananas 3000
Tomates cerises 1500
Salade composée 2200
Julienas vieilles vignes 2900
Taboulé oriental 2000
Chorizo Ibérique 2650
Canapés au fromage frais 1950
Pain de campagne 2800
Saint-Nectaire Fermier 2200
Bouchées au canard 2650
Kiwis 2550
Citronnade maison 2400
```
