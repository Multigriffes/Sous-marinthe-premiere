# Sous-marinthe-premiere le jeu

*Projet de fin d'année de NSI de première*

## Principe de base :

> [!IMPORTANT]  
Les coordonnées du joueur sont dans la liste pos_joueur de la forme `[X,Y]` avec X vers la "droite" et Y vers le "bas".  
Néanmoins, pour accéder à une position dans la grille du joueur ou celle des murs, il faut commencer par donner le Y et ensuite le X. Cela vient du fait que la grille est générée comme une liste de ligne et non une liste de colonnes.  
Cela afin que l'affichage dans la console et la compréhension soit simplifié.

Toutes les cartes sont enregistrées dans une grande liste `liste_maps` qui stocke toutes les cartes d'une taille `x` à l'indice `x-2`.

Le joueur évolue dans une grille carré où il est représenté par un 'O' et potentiellement la sortie par un 'S'. Des murs sont présents comme un labyrinthe mais ils ne sont pas montré au joueur, il doit les deviner au fur et à mesure de la partie.

```python
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

- creation_grille_joueur()
- action()
- play()
- affichage()

## creation_grille_joueur() :

**Premièrement,** la fonction va vérifier la cohérence des coordonnées données en entrée, le cas échéant en générer des nouvelles aléatoirement :

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

Une ligne est rajouté pour la 2<sup>ème</sup> consigne afin de sauvegarder les coordonnées initiales. Le `.copy()` sert à ne pas lier les deux listes :

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
pos_joueur_init=pos_joueur.copy()
```

Aussi on rajoute le creation des coordonnées de la sortie tout en vérifiant que ce ne sont pas les mêmes que celles du joueur (peu de chance) :

```python
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
**Enfin,** on retourne toutes les variables générées/crées pour pouvoir les utiliser en dehors de cette fonction

```python
return [grille_joueur,grille_murs,pos_joueur,pos_joueur_init,pos_sortie]
```
