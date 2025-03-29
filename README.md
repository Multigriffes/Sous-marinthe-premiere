# Sous-marinthe-premiere le jeu

*Projet de fin d'année de NSI de première*  
***Les consignes ayant changée, deux fichier sont présent afin de pouvoir jouer aux deux jeux différents.  
La doc devrait expliquer de manière clair quand des différences sont présentes***

## Principe de base :

> [!IMPORTANT]  
Les coordonnées du joueur sont dans la liste pos_joueur de la forme `[X,Y]` avec X vers la "droite" et Y vers le "bas".  
Néanmoins, pour accéder à une position dans la grille du joueur ou celle des murs, il faut commencer par donner le Y et ensuite le X.  
Cela vient du fait que la grille est générée comme une liste de ligne et non une liste de colonnes.  
Cela afin que l'affichage dans la console et la compréhension soit simplifié.

> [!IMPORTANT]
Toutes les cartes sont enregistrées dans une grande liste `liste_maps` qui stocke toutes les cartes d'une taille `x` à l'indice `x-2`.  
Les murs présent dans une case `[X,Y]` sont enregistrés sous forme d'une string `"0000"` qui correspond à `"gauche,droite,haut,bas"` avec 1 pour un mur.

Le joueur évolue dans une grille carré où il est représenté par un 'O' et éventuellement la sortie par un 'S'. Des murs sont présents comme un labyrinthe mais ils ne sont pas montré au joueur, il doit les deviner au fur et à mesure de la partie.

```text
['*', '*', '*', '*', '*']
['O', '*', '*', '*', '*']
['*', '*', '*', 'S', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
```

Au lancement de la boucle principale, le joueur se vera demander la taille de grille souhaité et la position de départ souhaité sinon elle sera généré aléatoirement. Il existe des maps de 2x2 jusqu'à du 15x15.

>Taille de la grille souhaitée :  
Position du joueur initiale si souhaité sinon laisser vide :

Le joueur peut ensuite se déplacer en entrant des déplacement avec `zqsd`. Il peut entrer plusieurs déplacements à la suite qui seront traités les uns après les autres.  

```text
Action souhaitée : ddz
=====================================
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', 'O']
['*', '*', ' ', ' ', ' ']
Nombres d'étoiles obtenues :  3
Nombres de murs touchés :  2
=====================================
```

## 1<sup>ère</sup> consigne :

Dans cette première consigne le joueur doit, tel Pac-Man, récupérer toutes les petites étoiles de la grille `'*'` afin de terminer le jeu en prenant le moins de murs.  
Un conteur s'incrémente à chaque étoile récupérée : `Nombres d'étoiles obtenues :  0`  
A chaque mur touché, le joueur est bloqué et un conteur de murs touché se voit agrémenté (idée de score) : `Nombres de murs touchés :  0`  
L'affichage type :

```text
Action souhaitée : ddz
=====================================
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', 'O']
['*', '*', ' ', ' ', ' ']
Nombres d'étoiles obtenues :  3
Nombres de murs touchés :  2
=====================================
```

*Etc...* Jusqu'à que toutes les étoiles soient ramassé ou le joueur se voit féliciter : `Bien joué, tu as touché 32 murs et attrapé 24 étoiles. GG ou pas`

## 2<sup>ème</sup> consigne :

Dans cette deuxième consigne, une sortie est généré et représenté par un `'S'`. Le joueur doit y parvenir en prenant le moins de murs possible.  
Cette version ajoute le fait qu'à chaque mur touché le joueur est renvoyé à sa position de départ initiale.

```text
=====================================
['*', '*', '*', '*', '*']
['*', 'S', '*', '*', '*']
['*', '*', '*', 'O', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
Nombres de murs touchés :  0
=====================================
Action souhaitée : z
```

```text
=====================================
['*', '*', '*', '*', '*']
['*', 'S', '*', 'O', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
Nombres de murs touchés :  0
=====================================
Action souhaitée : q
C'est un MUR CHEHHHHH !!!!!!!!!!
```

```text
=====================================
['*', '*', '*', '*', '*']
['*', 'S', '*', '*', '*']
['*', '*', '*', 'O', '*']
['*', '*', '*', '*', '*']
['*', '*', '*', '*', '*']
Nombres de murs touchés :  1
=====================================
```

Le jeu se termine quand le joueur atteind la sortie : `Bien joué, tu as recommencé 3 fois avant de gagner. GG ou pas`

# Le code :

Le jeu consiste en 3 fonctions principales et une fonction d'affichage :

- [creation_grille_joueur()](#creation_grille_joueur-)
- [action()](#action-)
- [affichage()](#affichage-)
- [play()](#play-)

Tout le formatage des entrées utilisateur est traité dans la fonction `play()` avant d'être passé aux fonction les utilisant. On ne va donc pas les traiter dans les autres fonctions.

## creation_grille_joueur() :

La fonction va prendre comme variable :

- `taille_grille`, la taille de la grille entrée par le joueur formaté
- `pos_joueur`, la position du joueur entrée par le joueur formaté

**Premièrement,** la fonction va vérifier la cohérence des coordonnées données en entrée, le cas contraire en générer des nouvelles aléatoirement :

```python
if pos_joueur!=[]:
    if pos_joueur[0] > taille_grille-1 or pos_joueur[1] > taille_grille-1:
        print("Position hors du terrain, génération aléatoire...")
        pos_joueur=[]
    if len(pos_joueur)!=2 and len(pos_joueur)!=0:
        print("Y a 2 nombres pour une coordonnées en 2D idiots, génération aléatoire...")
        pos_joueur=[]
if pos_joueur == [] :
    pos_joueur = [randint(0,taille_grille-1), randint(0,taille_grille-1)]
```

Dans la 2<sup>ème</sup> consigne on ajoute quelques ligne afin de sauvegarder les coordonnées initiales et rajouter la creation des coordonnées de la sortie tout en vérifiant que ce ne sont pas les mêmes que celles du joueur (peu de chance).  
Le `.copy()` sert à ne pas lier les deux listes :

```python
pos_joueur_init=pos_joueur.copy()
pos_sortie=pos_joueur
while pos_joueur==pos_sortie:
    pos_sortie=[randint(0,taille_grille-1),randint(0,taille_grille-1)]
```

---
**Ensuite,** on crée la grille d'affichage grâce à deux listes par compréhensions imbriquée.  
Une qui génère des `'*'` jusqu'à la taille de la grille.  
Et l'autre qui duplique cette même liste jusqu'à la taille de la grille.

```python
grille_joueur = [["*" for i in range(taille_grille)] for b in range(taille_grille)]
```

On place ensuite les élèments nécessaires sur la grille :

```python
grille_joueur[pos_joueur[1]][pos_joueur[0]] = "O"
grille_joueur[pos_sortie[1]][pos_sortie[0]] = "S"
```

---
**Puis,** on choisi la map aléatoirement parmie celles de la bonne taille.  
On a `taille_grille-2` car -1 pour les indices qui commence à 0, puis -1 pour les maps 1x1 qui n'existent pas.  
On utilise le `len()` pour s'adapter au nombre de maps d'une certaine taille et `-1` toujours pour une question d'indice.

```python
grille_murs = liste_map[taille_grille-2][randint(0,len(liste_map[taille_grille-2])-1)]
```

---
**Enfin,** on retourne toutes les variables modifiées/crées pour pouvoir les utiliser en dehors de cette fonction :

1<sup>ère</sup> consigne :

```python
return [grille_joueur,grille_murs,pos_joueur]
```

2<sup>ème</sup> consigne :

```python
return [grille_joueur,grille_murs,pos_joueur,pos_joueur_init_pos_sortie]
```

## action() :

La fonction va prendre comme variable :

- `commande`, l'input du joueur formaté
- `grille_joueur`, la grille de positionnement visuel actuelle
- `grille_murs`, la grille des murs de la maps choisie
- `pos_joueur`, la position du joueur actuelle
- `nbr_murs`, le nombre de murs précèdement touchés
- 1<sup>ère</sup> consigne :
  - `nbr_etoiles`, le nombre d'étoiles précèdement touchées
- 2<sup>ème</sup> consigne :
  - `pos_joueur_init`, la position du joueur de départ
  - `pos_sortie`, la position de la sortie

Tout les types sont vérifiés puis on initialise le traitement des commandes du joueur avec un boucle "`for j in commande:`" afin de traiter la possibilité de plusieurs déplacement/action à la suite.  
`j` représante un seule caractère de la string `commande`.

On remplace l'emplacement actuelle par `" "` ou `"*"` en fonction de la consigne.

```python
grille_joueur[pos_joueur[1]][pos_joueur[0]]=" "
```

### Traitement 1<sup>ère</sup> consigne type :

```python
if j=="g" or j=="q":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][0]=="0":
                pos_joueur[0]-=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
```

On vérifie le présence d'un mur du coté du déplacement (`X` le coté à vérifier).  
On modifie la position du joueur avec l'axe (`0`/`1`) et le sens (`+`/`-`) ligne 2.  
Enfin si la case atteinte contient une étoile, on incrémente le conteur d'étoiles.

>```python  
>if grille_murs[pos_joueur[1]][pos_joueur[0]][X]=="0":
>   pos_joueur[0]-=1
>   if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
>       nbr_etoiles+=1
>```

Dans l'éventualité où il y est un mur du coté souhaité, on diffuse un message d'amour puis on incrémente le conteur de murs.

>```python  
>else:
>    print("C'est un MUR CHEHHHHH !!!!!!!!!!")
>    nbr_murs+=1
>```

### Traitement 2<sup>ème</sup> consigne type :

```python
if j=="g" or j=="q":
    if grille_murs[pos_joueur[1]][pos_joueur[0]][0]=="0":
        pos_joueur[0]-=1
    else:
        print("C'est un MUR CHEHHHHH !!!!!!!!!!")
        nbr_murs+=1
        pos_joueur=pos_joueur_init.copy()
```

On vérifie le présence d'un mur du coté du déplacement (`X` le coté à vérifier).  
On modifie la position du joueur avec l'axe (`0`/`1`) et le sens (`+`/`-`) ligne 2.

```python
if grille_murs[pos_joueur[1]][pos_joueur[0]][X]=="0":
    pos_joueur[0]-=1
```

Dans l'éventualité où il y est un mur du coté souhaité, on diffuse un message d'amour puis on incrémente le conteur de murs enfin on met la position du joueur à la position initiale avec un `.copy()` pour ne pas lier les listes.

```python
else:
    print("C'est un MUR CHEHHHHH !!!!!!!!!!")
    nbr_murs+=1
    pos_joueur=pos_joueur_init.copy()
```

### Fin de fonction :

On met ensuite à jour les positions visuels dans la `grille_joueur` en dehors de la boucle pour le faire qu'une seule fois :  
Seulement `"O"` si consigne 1.

```python
grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
grille_joueur[pos_sortie[1]][pos_sortie[0]]="S"
```

**Enfin,** on retourne toutes les variables modifiées/crées pour pouvoir les utiliser en dehors de cette fonction :

1<sup>ère</sup> consigne :

```python
return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
```

2<sup>ème</sup> consigne :

```python
return [grille_joueur,pos_joueur,nbr_murs]
```

## Affichage() :

La fonction va prendre comme variable :

- `grille_joueur`, la grille de positionnement visuel actuelle
- `nbr_murs`, le nombre de murs précèdement touchés
- 1<sup>ère</sup> consigne :
  - `nbr_etoiles`, le nombre d'étoiles précèdement touchées

Tout les types sont vérifiés.  
On fait une boucle qui affiche ligne après ligne la `grille_joueur` puis on print les information en fonctionde la consigne :

```python
print("=====================================")
for i in grille_joueur:
    print(i)
print("Nombres d'étoiles obtenues :", nbr_etoiles)
print("Nombres de murs touchés :", nbr_murs)
print("=====================================")
```

Le tout est englobé dans des `print("=====================================")` pour améliorer la lisibilitée

## Play() :

