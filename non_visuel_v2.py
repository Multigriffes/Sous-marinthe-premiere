from random import randint

map5=([("1011"),("0110"),("1011"),("0011"),("0110")],
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

    if pos_joueur == [] :
        pos_joueur = [randint(0,taille_grille-1), randint(0,taille_grille-1)]
    else :
        assert pos_joueur[0] <= taille_grille-1 or pos_joueur[1] <= taille_grille-1, "Position hors du terrain"
        assert len(pos_joueur) == 2 , "Y a 2 nombres pour une coordonnées en 2D idiots"

    #creation de la grille du joueur :

    grille_joueur = [["*" for i in range(taille_grille)] for b in range(taille_grille)]
    grille_joueur[pos_joueur[1]][pos_joueur[0]] = "O"

    grille_murs = map5 #à gérer pour changement de map

    return [grille_joueur,grille_murs,pos_joueur]

def action(commande:str,grille_joueur:list,grille_murs:list,pos_joueur:list,nbr_etoiles:int,nbr_murs:int):
    """

    """

    assert type(commande) == str, "L'input n'est pas un string"
    commande=commande.lower
    
    if commande=="d" or commande=="droite":
        if grille_murs[pos_joueur[1]][pos_joueur[0]][1]=="0":
            grille_joueur[pos_joueur[1]][pos_joueur[0]]=""
            pos_joueur[0]+=1
            if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                nbr_etoiles+=1
            grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
            return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
        else:
            print("C'est un MUR CHEHHHHH !!!!!!!!!!")
            nbr_murs+=1
            return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
    elif commande=="g" or commande=="gauche":
        if grille_murs[pos_joueur[1]][pos_joueur[0]][0]=="0":
            grille_joueur[pos_joueur[1]][pos_joueur[0]]=""
            pos_joueur[0]-=1
            if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                nbr_etoiles+=1
            grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
            return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
        else:
            print("C'est un MUR CHEHHHHH !!!!!!!!!!")
            nbr_murs+=1
            return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
    elif commande=="h" or commande=="haut":
        if grille_murs[pos_joueur[1]][pos_joueur[0]][2]=="0":
            grille_joueur[pos_joueur[1]][pos_joueur[0]]=""
            pos_joueur[1]-=1
            if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                nbr_etoiles+=1
            grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
            return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
        else:
            print("C'est un MUR CHEHHHHH !!!!!!!!!!")
            nbr_murs+=1
            return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
    elif commande=="b" or commande=="bas":
        if grille_murs[pos_joueur[1]][pos_joueur[0]][3]=="0":
            grille_joueur[pos_joueur[1]][pos_joueur[0]]=""
            pos_joueur[1]+=1
            if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                nbr_etoiles+=1
            grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
            return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
        else:
            print("C'est un MUR CHEHHHHH !!!!!!!!!!")
            nbr_murs+=1
            return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
    else:
        print("La direction n'est pas reconnu")
        return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]
    
def play():
    nbr_etoiles,nbr_murs=0,0
    isPlay=True
    taille_grille=input("Taille de la grille souhaitée : ")
    pos_joueur=input("Position du joueur initiale si souhaité sinon laisser vide : ")
    info_init=creation_grille_joueur(taille_grille,pos_joueur)
    grille_joueur=info_init[0]
    grille_murs=info_init[1]
    pos_joueur=info_init[2]

    while isPlay:
        #Affichage
        for i in range(taille_grille):
            print(grille_joueur[i])

        commande=str(input("Action souhaitée : "))
        info_mouv=action(commande,grille_joueur,grille_murs,pos_joueur,nbr_etoiles,nbr_murs)
        grille_joueur=info_mouv[0]
        pos_joueur=info_mouv[1]
        nbr_etoiles=info_mouv[2]
        nbr_murs=info_mouv[3]
        if commande=="q" or commande=="quit":
            isPlay=False

play()