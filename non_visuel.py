from random import randint

map1=([("1011"),("0110"),("1011"),("0011"),("0110")],
[("1010"),("0101"),("1110"),("1110"),("1100")],
[("1001"),("0010"),("0000"),("0001"),("0101")],
[("1010"),("0101"),("1000"),("0111"),("1110")],
[("1101"),("1011"),("0001"),("0011"),("0101")])

#Creation des grilles
def creation_grille_joueur(taille_grille:int=5,pos_joueur:list=[]):
    """
    Cette fonction créé la liste représentant la grille et représente le joueur dessus à l'aide 
    d'un "0" et les cases vides avec un "*"
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


#Déplacement
def action(direction:str,grille_joueur,grille_mures,pos_joueur,nbr_cases_touche,nbr_etoiles_touche):
    
    #Droite
    if direction=="d" or direction=="droite":
        if grille_mures[pos_joueur[0]][pos_joueur[1]][1]=="0": #Vérification de la présence d'un mur
            #MàJ de la position
            grille_joueur[pos_joueur[0]][pos_joueur[1]]=""
            pos_joueur[1]+=1
            #Ajout du score si étoile
            if grille_joueur[pos_joueur[0]][pos_joueur[1]]=="*":
                nbr_etoiles_touche+=1
            #MàJ de la position
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
            return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]
        else:
            print("C'est un mur !!! p'tite merde d")
            nbr_cases_touche+=1
            return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]
    
    #Gauche
    elif direction=="g" or direction=="gauche":
        if grille_mures[pos_joueur[0]][pos_joueur[1]][0]=="0":
            grille_joueur[pos_joueur[0]][pos_joueur[1]]=""
            pos_joueur[1]-=1
            if grille_joueur[pos_joueur[0]][pos_joueur[1]]=="*":
                nbr_etoiles_touche+=1
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
            return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]
        else:
            print("C'est un mur !!! p'tite merde g")
            nbr_cases_touche+=1
            return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]
    
    #Bas
    elif direction=="b" or direction=="bas":
        if grille_mures[pos_joueur[0]][pos_joueur[1]][3]=="0":
            grille_joueur[pos_joueur[0]][pos_joueur[1]]=""
            pos_joueur[0]+=1
            if grille_joueur[pos_joueur[0]][pos_joueur[1]]=="*":
                nbr_etoiles_touche+=1
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
            return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]
        else:
            print("C'est un mur !!! p'tite merde b")
            nbr_cases_touche+=1
            return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]
    
    #Haut
    elif direction=="h" or direction=="haut":
        if grille_mures[pos_joueur[0]][pos_joueur[1]][2]=="0":
            grille_joueur[pos_joueur[0]][pos_joueur[1]]=""
            pos_joueur[0]-=1
            if grille_joueur[pos_joueur[0]][pos_joueur[1]]=="*":
                nbr_etoiles_touche+=1
            grille_joueur[pos_joueur[0]][pos_joueur[1]]="O"
            return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]
        else:
            print("C'est un mur !!! p'tite merde h")
            nbr_cases_touche+=1
            return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]
    
    #Non reconnue
    else:
        print("La direction n'est pas reconnu")
        return [grille_joueur,pos_joueur,nbr_cases_touche,nbr_etoiles_touche]


def play():
    #Initialisation :
    isplay=True
    nbr_etoiles_touche=0
    nbr_cases_touche=0
    taille_grille=int(input("Taille de la grille souhaitée : "))
    pos_joueur=list(input("Position du joueur initiale si souhaité sinon laisser vide : "))
    info_init=creation_grille_joueur(taille_grille,pos_joueur)
    grille_joueur=info_init[0]
    grille_mures=info_init[1]
    pos_joueur=info_init[2]

    #Boucle de jeu
    while isplay==True:
        #Affichage
        for i in range(taille_grille):
            print(grille_joueur[i])
        for i in range(taille_grille):
            print(grille_mures[i])
        
        #Input du joueur
        direction=input("Direction souhaitée : ")
        
        #Déplacement et MàJ des variables
        info_mouv=action(direction,grille_joueur,grille_mures,pos_joueur,nbr_cases_touche,nbr_etoiles_touche)
        grille_joueur=info_mouv[0]
        pos_joueur=info_mouv[1]
        nbr_cases_touche=info_mouv[2]
        nbr_etoiles_touche=info_mouv[3]
    
        #Debug
        if direction=="u":
            print(grille_mures[pos_joueur[0]][pos_joueur[1]][0],grille_mures[pos_joueur[0]][pos_joueur[1]][1],grille_mures[pos_joueur[0]][pos_joueur[1]][2],grille_mures[pos_joueur[0]][pos_joueur[1]][3])
            print(nbr_cases_touche,nbr_etoiles_touche)
        elif direction=="q" or direction=="quitte" or direction=="quit":
            isplay=False


play()
#test2