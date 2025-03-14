from random import randint

map1=([("1011"),("0110"),("1011"),("0011"),("0110")],
[("1010"),("0101"),("1110"),("1110"),("1100")],
[("1001"),("0010"),("0000"),("0001"),("0101")],
[("1010"),("0101"),("1000"),("0111"),("1110")],
[("1101"),("1011"),("0001"),("0011"),("0101")])

#Creation des grilles
def creation_grille_joueur(taille_grille:int=5,pos_joueur:list=[]):
    """
    Cette fonction créé la liste représentant la grille et représente le joueur dessus à l'aide d'un "0" et les cases vides avec un "*"
    """

    assert type(taille_grille)==int ;"la taille de la grille n'est pas un int"
    assert type(pos_joueur)==list ;"la position du joueur n'est pas une liste"

    if pos_joueur==[]:
        pos_joueur=[randint(0,taille_grille-1),randint(0,taille_grille-1)]
    else:
        assert pos_joueur[0]>=taille_grille or pos_joueur[1]>=taille_grille;"les positions données sont en dehors du terrain"
    grille_joueur=[["*" for b in range(taille_grille)] for a in range(taille_grille)]
    grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
    grille_mures=map1 #à gérer pour changement de map
    return [grille_joueur,grille_mures,pos_joueur]

#MàJ variables globales
info_init=creation_grille_joueur()
grille_joueur=info_init[0]
grille_mures=info_init[1]
pos_joueur=info_init[2]

#Déplacement
def mouvement(direction:str,grille_joueur,grille_mures,pos_joueur):
    if direction=="d" or direction=="droite":
        if grille_mures[pos_joueur[0]][pos_joueur[1]][1]==0:
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="*"
            pos_joueur[0]+=1
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
            return [grille_joueur,pos_joueur]
    elif direction=="g" or direction=="gauche":
        if grille_mures[pos_joueur[0]][pos_joueur[1]][0]==0:
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="*"
            pos_joueur[0]-=1
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
            return [grille_joueur,pos_joueur]
    elif direction=="b" or direction=="bas":
        if grille_mures[pos_joueur[0]][pos_joueur[1]][3]==0:
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="*"
            pos_joueur[1]-=1
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
            return [grille_joueur,pos_joueur]
    elif direction=="h" or direction=="haut":
        if grille_mures[pos_joueur[0]][pos_joueur[1]][2]==0:
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="*"
            pos_joueur[1]+=1
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
            return [grille_joueur,pos_joueur]
    else:
        print("la direction n'est pas reconnu")

direction=input("Direction souhaitée : ")

#MàJ variables globales
info_mouv=mouvement(direction,grille_joueur,grille_mures,pos_joueur)
grille_joueur=info_init[0]
pos_joueur=info_init[1]

#print(info_init)
#print(grille_joueur)
#print(grille_mures)
#print(pos_joueur)

