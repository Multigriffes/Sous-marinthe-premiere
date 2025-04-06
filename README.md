# Sous-marinthe-premiere le jeu :

*Projet de fin d'année de NSI de première*

> [!IMPORTANT]
***Les consignes ayant changée, deux fichier sont présent afin de pouvoir jouer aux deux jeux différents.  
La doc devrait expliquer de manière clair quand des différences sont présentes***

# Principe de base :

> [!IMPORTANT]  
Les coordonnées du joueur sont dans la liste pos_joueur de la forme `[X,Y]` avec X vers la "droite" et Y vers le "bas".  
Néanmoins, pour accéder à une position dans la grille du joueur ou celle des murs, il faut commencer par donner le Y et ensuite le X.  
Cela vient du fait que la grille est générée comme une liste de ligne et non une liste de colonnes.  
Cela afin que l'affichage dans la console et la compréhension soit simplifié.

> [!IMPORTANT]
Toutes les cartes sont enregistrées dans une grande liste `liste_maps` qui stocke toutes les cartes d'une taille `x` à l'indice `x-2`.  
Les murs présent dans une case `[X,Y]` sont enregistrés sous forme d'une string `"0000"` qui correspond à `"gauche,droite,haut,bas"` avec 1 pour un mur.
Cette liste est générée en important un autre fichier et la fonction `generation_liste` qui elle stocke toutes les cartes.

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

**La fonction va prendre comme variable :**

- `taille_grille`, la taille de la grille entrée par le joueur formaté
- `pos_joueur`, la position du joueur entrée par le joueur formaté

---
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

**La fonction va prendre comme variable :**

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

---
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

```python  
if grille_murs[pos_joueur[1]][pos_joueur[0]][X]=="0":
   pos_joueur[0]-=1
   if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
       nbr_etoiles+=1
```

Dans l'éventualité où il y est un mur du coté souhaité, on diffuse un message d'amour puis on incrémente le conteur de murs.

```python  
else:
    print("C'est un MUR CHEHHHHH !!!!!!!!!!")
    nbr_murs+=1
```

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

- 1<sup>ère</sup> consigne :

```python
return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
```

- 2<sup>ème</sup> consigne :

```python
return [grille_joueur,pos_joueur,nbr_murs]
```

## affichage() :

**La fonction va prendre comme variable :**

- `grille_joueur`, la grille de positionnement visuel actuelle
- `nbr_murs`, le nombre de murs précèdement touchés
- 1<sup>ère</sup> consigne :
  - `nbr_etoiles`, le nombre d'étoiles précèdement touchées

---
Tout les types sont vérifiés.  
On fait une boucle qui affiche ligne après ligne `grille_joueur` puis on `print` les information en fonction de la consigne :

```python
print("=====================================")
for i in grille_joueur:
    print(i)
print("Nombres d'étoiles obtenues :", nbr_etoiles)
print("Nombres de murs touchés :", nbr_murs)
print("=====================================")
```

Le tout est englobé dans des `print("=====================================")` pour améliorer la lisibilitée

## play() :

**Initialisation des variables par default ou mise à zero :**

- `nbr_murs=0`, Le nombre de murs touchés initiale, càd 0
- `isPlay=True`, Variable qui controle la boucle principale de jeu, `True` pour que ça tourne LOL
- `taille_grille=""`, La variable qui va recevoir la taille de la grille en input, initialisé pour permettre l'utilisation d'une boucle `while` pour l'input
- `pos_joueur`, La variable qui va recevoir la position donnée par l'utilisateur, initialisé pour permettre l'utilisation d'une boucle `while`
- 1<sup>ère</sup> consigne :
  - `nbr_etoiles=0`, Le nombre d'étoiles touchées initiale, càd zero

```python
nbr_etoiles,nbr_murs,isPlay,taille_grille,pos_joueur=0,0,True,"",['default']
```

---

### Traitement des inputs de taille et de position joueur :

> J'ai découvert ici le `try` et tout ce qui l'entoure, c'est une ptn de dinguerie !!!

**Premièrement** la taille de la map.  
Une boucle `while` est initié afin de parer les entrées vide ou incorrectes.  
On essaye (`try`) de transformer cette entrée en `int` car c'est un `string` par défault, si cela ne marche pas (`except`) on réinitialise la variable pour refaire un tour de boucle.  
Si ça marche (`else`) on transforme l'entrée en `int` puis on vérifie qu'elle soit `<=` à 15 sinon on refait un tour.

```python
while taille_grille=="":
    taille_grille=input("Taille de la grille souhaitée : ")
    try:
        int(taille_grille)
    except:
        taille_grille=""
    else:
        taille_grille=int(taille_grille)
        if taille_grille>15:
            taille_grille=""
```

**Deuxièmement** la position du départ souhaité.  
Une boucle `while` est initié afin de parer les entrées vide ou incorrectes.  
On met `a=0` pour l'utiliser comme compteur plus polyvalent.  
Ensuite si l'entrée est celle par défault ou vide, on laisse passer pour faire un tour ou sortir une liste vide afin qu'elle soit générée plus tard.

```python
if pos_joueur!=['default'] and pos_joueur!=[]:
```

Dans le cas contraire, on va itérer dans cette `string` transformée en `list` (afin de permettre la suppresion).  
A chaque caractère on essaye de le transformer en `int`, si ça marche on incrémente notre conteur sinon on vérifie si c'est une virgule pour la garder ou sinon supprimer l'intru.

```python
if pos_joueur!=['default'] and pos_joueur!=[]:
    for i in range(len(pos_joueur)):
        try:
            int(pos_joueur[a])
        except:
            if pos_joueur[a]==',':
                a+=1
            else:
                del pos_joueur[a]
        else:
            a+=1
```

Enfin, on itère dans cette liste de chiffre et de virgule pour reformer les potentiels nombres :
> Ici, j'ai passé 15 mille ans avant de me rendre compte que `list/string[:X]` n'incluait pas `X`. J'ai peut être cassé plusieurs clavier.

On initialise notre compteur `a=0`, notre `pos_joueur_temp=[]` et `isVirgule=False`.  
Si c'est une virgule on le note, sinon on regarde si il y a une entrée précèdente dans la liste temporaire. Si ce n'est pas le cas on rajoute simplement le chiffre dans la liste temporaire.  
Sinon, on vérifie si il y avait une virgule avant dans ce cas on `.append()` juste le chiffre, si il y en a pas on rajoute le chiffre à la chaine de chiffre du nombre précèdent.  
Enfin on note le fait que ce n'était pas une virgule.

```python
pos_joueur_temp,isVirgule,a=[],False,0
for i in pos_joueur:
    if i==',':
        isVirgule=True
    else:
        try:
            pos_joueur_temp[a-1]
        except:
            pos_joueur_temp.append(i)
            a+=1
        else:
            if isVirgule:
                pos_joueur_temp.append(i)
                a+=1
            else:
                pos_joueur_temp[a-1]=pos_joueur_temp[a-1][0:len(pos_joueur_temp[a-1])]+i
        isVirgule=False
```

**Dernière étape,** on passe dans cette dernière liste temporaire pour y transformer toutes les chaines de chiffres en nombres.  
On transfère la temporaire dans la principale avec toujours le `.copy()`.

```python
for i in range(len(pos_joueur_temp)):
    pos_joueur_temp[i]=int(pos_joueur_temp[i])
pos_joueur=pos_joueur_temp.copy()
```

### Récupération des variables générées :

On met une variable `info_init` qui va contenir toutes les infos que renvoie `creation_grille_joueur` en lui donnant les inputs du joueur.  
On met ensuite individuelement à jour chaque variable que l'on va réutiliser.

- 1<sup>ère</sup> consigne :

```python
info_init=creation_grille_joueur(taille_grille,pos_joueur)
grille_joueur,grille_murs,pos_joueur=info_init[0],info_init[1],info_init[2]
```

- 2<sup>ème</sup> consigne :

```python
info_init=creation_grille_joueur(taille_grille,pos_joueur)
grille_joueur,grille_murs,pos_joueur,pos_joueur_init,pos_sortie=info_init[0],info_init[1],info_init[2],info_init[3],info_init[4]
```

### Boucle de jeu ENFINNN !!! :

```python
while isPlay:
```

On commence par afficher grâce à la fonction homonyme et les variables souhaitées (`nbr_etoiles` ou pas) :

```python
affichage(grille_joueur,nbr_etoiles,nbr_murs)
```

On récupère ensuite les commandes du joueur en minuscule. Tant que c'est vide on redemande.

```python
commande=""
while commande=="":
    commande=str(input("Action souhaitée : ")).lower()
```

On vérifie que ce soit `"exit"` sinon on met à jour toutes les variables changées par la fonction `action()` auquel on à passé les variables spécifique à la consigne :

```python
if commande=="exit":
    isPlay=False
```

- 1<sup>ère</sup> consigne :

```python
else:
    info_mouv=action(commande,grille_joueur,grille_murs,pos_joueur,nbr_etoiles,nbr_murs)
    grille_joueur,pos_joueur,nbr_etoiles,nbr_murs=info_mouv[0],info_mouv[1],info_mouv[2],info_mouv[3]
```

- 2<sup>ème</sup> consigne :

```python
else:
    info_mouv=action(commande,grille_joueur,grille_murs,pos_joueur,pos_joueur_init,pos_sortie,nbr_murs)
    grille_joueur,pos_joueur,nbr_murs=info_mouv[0],info_mouv[1],info_mouv[2]
```

**Enfin,** on vérifie la condition de victoire de la consigne et c'est GG!

- 1<sup>ère</sup> consigne :

```python
if nbr_etoiles==taille_grille**2-1:
    print("Bien joué, tu as touché",nbr_murs,"murs et attrapé",nbr_etoiles,"étoiles. GG ou pas")
    isPlay=False
```

- 2<sup>ème</sup> consigne :

```python
if pos_joueur==pos_sortie:
    print("Bien joué, tu as recommencé",nbr_murs,"fois avant de gagner. GG ou pas")
    isPlay=False
```

# Le créateur de maps :

## Un jour peut être si j'ai pas la flemme
