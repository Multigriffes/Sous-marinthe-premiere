from random import randint
from generation_liste_maps import generation_liste
from lib.py import *

#Creation des grilles
def creation_grille_joueur(taille_grille:int,pos_joueur:list=[]):
    """
    Cette fonction créé la liste représentant la grille et représente le joueur dessus à l'aide 
    d'un "O" et les cases vides avec un "*" et la sortie avec un "S"
    """
    
    assert type(taille_grille)==int ,"la taille de la grille n'est pas un int"
    assert taille_grille>1, "Grille trop petite"
    assert taille_grille<=15 ,"On a pas autant de map que ça, 15 pas plus"
    assert type(pos_joueur)==list ,"la position du joueur n'est pas une liste"


    #Génération ou vérification des coordonnée du joueur
    if pos_joueur!=[]:
        if pos_joueur[0] > taille_grille-1 or pos_joueur[1] > taille_grille-1:
            print("Position hors du terrain, génération aléatoire...")
            pos_joueur=[]
        if len(pos_joueur)!=2 and len(pos_joueur)!=0:
            print("Y a 2 nombres pour une coordonnées en 2D idiots, génération aléatoire...")
            pos_joueur=[]
    if pos_joueur == []:
        pos_joueur = [randint(0,taille_grille-1), randint(0,taille_grille-1)]
    pos_joueur_init=pos_joueur.copy()
    
    #Génération des coordonnée de la sortie
    pos_sortie=pos_joueur
    while pos_joueur==pos_sortie:
        pos_sortie=[randint(0,taille_grille-1),randint(0,taille_grille-1)]

    #Création de la grille du joueur
    grille_joueur = [["*" for i in range(taille_grille)] for b in range(taille_grille)]
    grille_joueur[pos_joueur[1]][pos_joueur[0]] = "O"
    grille_joueur[pos_sortie[1]][pos_sortie[0]] = "S"


    #Choix de le map en fonction du nbr de cases
    grille_murs = generation_liste()[taille_grille-2][randint(0,len(generation_liste()[taille_grille-2])-1)]

    return [grille_joueur,grille_murs,pos_joueur,pos_joueur_init,pos_sortie]

def action(commande:str,grille_joueur:list,grille_murs:list,pos_joueur:list,pos_joueur_init:list,pos_sortie:list,nbr_murs:int):
    """
    La fonction gère les action du joueur et sont influence sur les diffèrentes variables du jeu
    """

    assert type(commande) == str, "commande n'est pas un string"
    assert type(grille_joueur) == list, "grille_joueur n'est pas un list"
    assert type(grille_murs) == tuple, "grille_murs n'est pas un tuple"
    assert type(pos_joueur) == list, "pos_joueur n'est pas un list"
    assert type(pos_joueur_init) == list, "pos_joueur_init n'est pas un list"
    assert type(pos_sortie) == list, "pos_sortie n'est pas un list"
    assert type(nbr_murs) == int, "nbr_murs n'est pas un int"
    
    for j in commande:
        grille_joueur[pos_joueur[1]][pos_joueur[0]]="*"
        if j=="d":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][1]=="0":
                pos_joueur[0]+=1
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
                pos_joueur=pos_joueur_init.copy()
        elif j=="g" or j=="q":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][0]=="0":
                pos_joueur[0]-=1
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
                pos_joueur=pos_joueur_init.copy()
        elif j=="h" or j=="z":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][2]=="0":
                pos_joueur[1]-=1
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
                pos_joueur=pos_joueur_init.copy()
        elif j=="b" or j=="s":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][3]=="0":
                pos_joueur[1]+=1
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
                pos_joueur=pos_joueur_init.copy()
        else:
            print(j+" : La commande n'est pas reconnu")
    grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
    grille_joueur[pos_sortie[1]][pos_sortie[0]]="S"
    return [grille_joueur,pos_joueur,nbr_murs]

def affichage(grille_joueur,nbr_murs):

    assert type(grille_joueur)==list, "grille_joueur n'est pas une liste"
    assert type(nbr_murs)==int, "nbr_murs n'est pas un int"

    print("=====================================")
    for i in grille_joueur:
        print(i)
    print("Nombres de murs touchés :", nbr_murs)
    print("=====================================")

def play():
    '''
    Fonction pour le lancement du jeu, initialisation des variables puis boucle de jeu
    '''
    #Initialisation avec input joueur
    nbr_murs,isPlay=0,True

    taille_grille=input_taille_grille()
    pos_joueur=input_pos_joueur()

    grille_joueur,grille_murs,pos_joueur,pos_joueur_init,pos_sortie=creation_grille_joueur(taille_grille,pos_joueur)

    while isPlay:#Boucle de jeu
        affichage(grille_joueur,nbr_murs)
        
        #Instructions de jeu et mise à jour des variables
        commande=""
        while commande=="":
            commande=str(input("Action souhaitée : ")).lower()
        
        if commande=="exit":
            isPlay=False
        else:
            grille_joueur,pos_joueur,nbr_murs=action(commande,grille_joueur,grille_murs,pos_joueur,pos_joueur_init,pos_sortie,nbr_murs) # type: ignore


        if pos_joueur==pos_sortie:
            print("Bien joué, tu as recommencé",nbr_murs,"fois avant de gagner. GG ou pas")
            isPlay=False
        