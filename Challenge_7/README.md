### GECC 2024 Challenge VII : Casser la routine Tant d'émotions pour ce repas et sa préparation.
En se creusant un peu la tête, on arrive quand même à faire des choses bien.
Il y a eu des maladresses, certes, mais il y a aussi eu des coups d'éclat.
C'est quand même plaisant de rencontrer les collègues dans un cadre décontracté qui change de l'ambiance habituelle au travail.
Optimiser, bien faire, créer de la valeur ajoutée avec un peu de réflexion restent des activités qui font du bien quand on s'y prend avec méthode et application.
Dans votre mémoire, ce pique-nique restera un doux souvenir venu rompre la routine.

La routine offre une certaine stabilité, mais elle est aussi probablement la première source d'ennui.
Cultiver les petites choses qui font du bien est la clé pour atténuer les répétitions apparentes du quotidien et conserver l'envie et l'engagement dans ce que l'on fait.
Pour évaluer mathématiquement votre santé mentale, vous décidez alors de modéliser informatiquement le caractère routinier ou aléatoire de vos activités.

En informatique, on utilise des suites récurrentes modulaires pour produire des générateurs d'entiers pseudo-aléatoires. 
Le comportement de ces suites, quand elles sont bien établies, est particulièrement imprévisible.


$\ s_0 = 3, \qquad \forall n > 0 : s_n = 4 \cdot s_{n-1} + 6 \mod{7} \$

$\ t_0 = 11, \qquad \forall n > 0 : t_n = 10 \cdot t_{n-1} + 4 \mod{13} \$

$\ u_0 = 2, \qquad \forall n > 0 : u_n = 2 \cdot u_{n-1} \mod{3} \$

$\ v_0 = 9, \qquad \forall n > 0 : v_n = 12 \cdot v_{n-1} + 3 \mod{20} \$

$\ w_0 = 12, \qquad \forall n > 0 : w_n = 14 \cdot w_{n-1} + 6 \mod{16} \$



<br>
<div align="center">
  <img src="https://github.com/MunMaks/GECC-2024/blob/main/Challenge_7/suites.png" alt="image1" width="900" height="100">
</div>
<br>


L'exemple au dessus présente 5 suites linéaires et modulaires prenant une période gloable de 12 à partir du rang $n_0 = 3$.
Le 5-uplet prend les valeurs $(3, 4, 1, 3, 2)$ au cran $n_0 = 3$, puis tous les 12 crans, le même 5-uplet de valeurs revient. 
Ces derniers sont encadrés en noir (au crans 3, 15 et 27).


Tels les grands sages philosophes, on a besoin de vous pour mesurer la période d'un phénomène répétitif.
Très utilisés dans les générateurs de nombres pseudo-aléatoires, le processus utilise des suites congruentielles linéaires
pour un maximum de création tout en restant ultimement périodique.
Une suite congruentielle linéaire est définie par un quadruplet $a, b, u_0, p$ de quatre nombres entiers
dont les trois premiers sont modulaires (ce sont des restes modulo $p$).
La suite modulaire associée $(u_n)_{n \in \mathbb{N}}$ est récurissivement définie par sa première valeur $u_0$ puis avec la formule de récurence linéaire suivante :



$\ \forall n > 0 : u_n = ( a \times u_{n-1} + b ) \mod{p} \$


De telles suites finissent toujours par devenir périodiques à partir d'un certain cran, en particulier parce que :
<ul>
  <li>Sauf pour la première valeur, les valeurs ne dépendent que de la précédente. </li>
  <li>Comme les valeurs sont définies modulo $p$, il n'y a qu'un nombre fini de $p$ valeurs possibles différentes.</li>
</ul>

Ainsi dès qu'une telle suite repasse par une valeur visitée, et bien elle se met à cycler sur son dernier parcours de valeurs.
Le but de ce challenge est maintenant de calculer la période globale d'un n-uplet de ces suites.

Imaginons qu'ils y aient seulement trois suites modulaires linéaires, chacune décrite par son quadruplet, comme il suit :

```
1 2 0 5
2 2 1 4
5 2 3 7
```


Appelons $u_n$, $v_n$ et $w_n$ les trois suites décritent respectivement par $(1, 2, 0, 5)$, $(2, 2, 1, 4)$ et $(5, 2, 3, 7)$. On a donc : 

$(u_0, v_0, w_0) = (0, 1, 3)$

ainsi que :

$\ \forall n > 0 : u_n = ( u_{n-1} + 2 ) \mod{5}, v_n = ( 2v_{n-1} + 2 ) \mod{4} \text{ et } w_n = ( 5w_{n-1} + 2 ) \mod{7} \$

Avec ces données, on peut calculer les valeurs des trois suites :

```
0  (0, 1, 3)
1  (2, 0, 3)
2  (4, 2, 3)
3  (1, 2, 3)
4  (3, 2, 3)
5  (0, 2, 3)
6  (2, 2, 3)
7  (4, 2, 3)
8  (1, 2, 3)
9  (3, 2, 3)
10 (0, 2, 3)
11 (2, 2, 3)
12 (4, 2, 3)
...
```

Comme $(5*3 + 2) \mod{7}$ vaut $3$ car $17 = 7 \times 2 + 3$, la suite $(w_n)_{n \in \mathbb{N}}$ est constante et donc périodique de période $1$ dès sa première valeur.
Elle vaut tout le temps $3$.


La suite $(v_n)_{n \in \mathbb{N}}$ devient constante à partir de sa troisième valeur.
Elle est ultimement périodique de période $1$ à partir de $v_2$.

La suite $(u_n)_{n \in \mathbb{N}}$ est périodique de période 5 en cyclant dès sa première valeur sur les valeurs  $\ 0 \rightarrow 2 \rightarrow 4 \rightarrow 1 \rightarrow 3 \rightarrow 0 \rightarrow \dots \$.


Sur l'ensemble de ces trois suites, le processus est ultimement périodique de période $5$ à partir de $n=2$. Pour $n=2$,
les trois suites valent $(4, 2, 3)$ et commence à cycler sur les valeurs suivantes :

```
n = 2 (4, 2, 3)
n = 3 (1, 2, 3)
n = 4 (3, 2, 3)
n = 5 (0, 2, 3)
n = 6 (2, 2, 3)
n = 7 (4, 2, 3) # vecteurs de valeurs déjà atteints pour n=2 --> le schéma va donc se reproduire indéfiniment
```

Le phénomène global (ce triplet de suite) étant ultimement périodique de période $5$, la réponse au problème serait alors $5$.
Cette période mesure à quel point ça varie mais pas trop.
Contrairement à l'exemple, vous devrez calculer la période globale d'un phénomène associé à 12 suites différentes.
Elles seront elles aussi décrites par des quadruplets $(a, b, u_0, p)$.

<br>
<b>
Quelle est la période globale du 12-uplet de suites modélisant vos principales activités ?
</b>
<br>

Voici vos données personnalisées pour ce challenge, ce sont les 12 quadruplets décrisant les suites modélisant le caractère changeant de vos principales activités :

```
2577 857 1866 2700
3380 8744 4290 8862
639 2322 707 3544
3334 2747 4534 4871
906 4285 4216 5767
1422 1634 1348 2927
1510 651 2032 4539
1158 738 63 1279
593 3491 3387 4513
2865 2734 3176 6770
6609 7268 4903 9261
5788 958 1883 7459
```
