from random import randint

liste_map=(((('1011', '0110'), ('1011', '0101')), (('1010', '0111'), ('1001', '0101'))), ((('1010', '0010', '0111'), ('1100', '1000', '0111'), ('1101', '1001', '0111')), (('1011', '0110', '1110'), ('1110', '1000', '0100'), ('1001', '0101', '1101'))), ((('1010', '0010', '0110', '1110'), ('1000', '0101', '1000', '0100'), ('1100', '1011', '0100', '1100'), ('1001', '0111', '1001', '0101')), (('1010', '0010', '0110', '1110'), ('1000', '0101', '1000', '0100'), ('1100', '1011', '0100', '1100'), ('1001', '0111', '1001', '0101'))), ((('1011', '0110', '1011', '0011', '0110'), ('1010', '0101', '1110', '1110', '1100'), ('1001', '0010', '0000', '0001', '0101'), ('1010', '0101', '1000', '0111', '1110'), ('1101', '1011', '0001', '0011', '0101')), (('1011', '0110', '1011', '0011', '0110'), ('1010', '0101', '1110', '1110', '1100'), ('1001', '0010', '0000', '0001', '0101'), ('1010', '0101', '1000', '0111', '1110'), ('1101', '1011', '0001', '0011', '0101'))), ((('1110', '1110', '1011', '0010', '0111', '1110'), ('1100', '1001', '0010', '0101', '1010', '0101'), ('1000', '0010', '0100', '1010', '0000', '0110'), ('1000', '0101', '1000', '0000', '0101', '1100'), ('1100', '1011', '0001', '0100', '1011', '0101'), ('1001', '0011', '0111', '1001', '0011', '0111')), (('1110', '1110', '1011', '0010', '0111', '1110'), ('1100', '1001', '0010', '0101', '1010', '0101'), ('1000', '0010', '0100', '1010', '0000', '0110'), ('1000', '0101', '1000', '0000', '0101', '1100'), ('1100', '1011', '0001', '0100', '1011', '0101'), ('1001', '0011', '0111', '1001', '0011', '0111'))), ((('1010', '0010', '0111', '1010', '0011', '0110', '1110'), ('1101', '1000', '0010', '0100', '1110', '1101', '1100'), ('1011', '0100', '1001', '0100', '1001', '0010', '0101'), ('1110', '1001', '0110', '1001', '0010', '0101', '1110'), ('1001', '0110', '1000', '0010', '0000', '0011', '0101'), ('1110', '1001', '0000', '0101', '1100', '1011', '0110'), ('1001', '0011', '0101', '1011', '0001', '0011', '0101')), (('1010', '0010', '0111', '1010', '0011', '0110', '1110'), ('1101', '1000', '0010', '0100', '1110', '1101', '1100'), ('1011', '0100', '1001', '0100', '1001', '0010', '0101'), ('1110', '1001', '0110', '1001', '0010', '0101', '1110'), ('1001', '0110', '1000', '0010', '0000', '0011', '0101'), ('1110', '1001', '0000', '0101', '1100', '1011', '0110'), ('1001', '0011', '0101', '1011', '0001', '0011', '0101'))), ((('1010', '0010', '0010', '0111', '1010', '0010', '0010', '0110'), ('1001', '0000', '0001', '0010', '0000', '0100', '1001', '0100'), ('1110', '1000', '0010', '0000', '0001', '0001', '0010', '0100'), ('1100', '1001', '0100', '1101', '1011', '0110', '1000', '0100'), ('1000', '0010', '0000', '0111', '1110', '1100', '1000', '0100'), ('1001', '0000', '0001', '0010', '0001', '0100', '1000', '0100'), ('1010', '0100', '1110', '1000', '0010', '0101', '1000', '0100'), ('1001', '0101', '1001', '0001', '0101', '1011', '0001', '0101')), (('1010', '0010', '0010', '0111', '1010', '0010', '0010', '0110'), ('1001', '0000', '0001', '0010', '0000', '0100', '1001', '0100'), ('1110', '1000', '0010', '0000', '0001', '0001', '0010', '0100'), ('1100', '1001', '0100', '1101', '1011', '0110', '1000', '0100'), ('1000', '0010', '0000', '0111', '1110', '1100', '1000', '0100'), ('1001', '0000', '0001', '0010', '0001', '0100', '1000', '0100'), ('1010', '0100', '1110', '1000', '0010', '0101', '1000', '0100'), ('1001', '0101', '1001', '0001', '0101', '1011', '0001', '0101'))))

#Creation des grilles
def creation_grille_joueur(taille_grille:int,pos_joueur:list=[]):
    """
    Cette fonction créé la liste représentant la grille et représente le joueur dessus à l'aide 
    d'un "O" et les cases vides avec un "*"
    """
    
    assert type(taille_grille)==int ;"la taille de la grille n'est pas un int"
    assert taille_grille>1, "Grille trop petite"
    assert taille_grille<=15 ;"On a pas autant de map que ça, 15 pas plus"
    assert type(pos_joueur)==list ;"la position du joueur n'est pas une liste"


    #Génération ou vérification des coordonnée du joueur
    if pos_joueur!=[]:
        if pos_joueur[0] > taille_grille-1 or pos_joueur[1] > taille_grille-1:
            print("Position hors du terrain, génération aléatoire...")
            pos_joueur=[]
        if len(pos_joueur)!=2 and len(pos_joueur)!=0:
            print("Y a 2 nombres pour une coordonnées en 2D idiots, génération aléatoire...")
            pos_joueur=[]
    if pos_joueur == [] :
        pos_joueur = [randint(0,taille_grille-1), randint(0,taille_grille-1)]

    #Creation de la grille du joueur
    grille_joueur = [["*" for i in range(taille_grille)] for b in range(taille_grille)]
    grille_joueur[pos_joueur[1]][pos_joueur[0]] = "O"

    #Choix de le map en fonction du nbr de cases
    grille_murs = liste_map[taille_grille-2][randint(0,len(liste_map[taille_grille-2])-1)]

    return [grille_joueur,grille_murs,pos_joueur]

def action(commande:str,grille_joueur:list,grille_murs:list,pos_joueur:list,nbr_etoiles:int,nbr_murs:int):
    """

    """

    assert type(commande) == str, "commande n'est pas un string"
    assert type(grille_joueur) == list, "grille_joueur n'est pas un list"
    assert type(grille_murs) == tuple, "grille_murs n'est pas un tuple"
    assert type(pos_joueur) == list, "pos_joueur n'est pas un list"
    assert type(nbr_etoiles) == int, "nbr_etoiles n'est pas un int"
    assert type(nbr_murs) == int, "nbr_murs n'est pas un int"
    
    for j in commande:
        if j=="d" or j=="droite":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][1]=="0":
                grille_joueur[pos_joueur[1]][pos_joueur[0]]=" "
                pos_joueur[0]+=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
                grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
        elif j=="g" or j=="gauche" or j=="q":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][0]=="0":
                grille_joueur[pos_joueur[1]][pos_joueur[0]]=" "
                pos_joueur[0]-=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
                grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
        elif j=="h" or j=="haut" or j=="z":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][2]=="0":
                grille_joueur[pos_joueur[1]][pos_joueur[0]]=" "
                pos_joueur[1]-=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
                grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
        elif j=="b" or j=="bas" or j=="s":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][3]=="0":
                grille_joueur[pos_joueur[1]][pos_joueur[0]]=" "
                pos_joueur[1]+=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
                grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
            else:
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
                nbr_murs+=1
        else:
            print(j+" : La commande n'est pas reconnu")
    return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs]

def affichage(grille_joueur,nbr_etoiles,nbr_murs):
    print("=====================================")
    for i in grille_joueur:
        print(i)
    print("Nombres d'étoiles obtenues : ", nbr_etoiles)
    print("Nombres de murs touchés : ", nbr_murs)
    print("=====================================")

def play():
    #Initialisation avec input joueur
    nbr_etoiles,nbr_murs,isPlay,taille_grille,pos_joueur=0,0,True,"",['default']

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

    while pos_joueur==['default']:
        pos_joueur=list(input("Position du joueur initiale si souhaité sinon laisser vide : "))
        #Nettoyage de la liste de string de la position
        a=0
        if pos_joueur!=['default'] and pos_joueur!=[]:
            for i in range(len(pos_joueur)):
                try:
                    int(pos_joueur[a])
                except:
                    del pos_joueur[a]
                else:
                    pos_joueur[a]=int(pos_joueur[a]) # type: ignore
                    a+=1

    info_init=creation_grille_joueur(taille_grille,pos_joueur)
    grille_joueur,grille_murs,pos_joueur=info_init[0],info_init[1],info_init[2]

    while isPlay:
        #Affichage
        affichage(grille_joueur,nbr_etoiles,nbr_murs)
        
        #Instructions de jeu et mise à jour des variables
        commande=""
        while commande=="":
            commande=str(input("Action souhaitée : ")).lower()
        
        if commande=="exit":
            isPlay=False

        info_mouv=action(commande,grille_joueur,grille_murs,pos_joueur,nbr_etoiles,nbr_murs)
        grille_joueur,pos_joueur,nbr_etoiles,nbr_murs=info_mouv[0],info_mouv[1],info_mouv[2],info_mouv[3]

        if nbr_etoiles==taille_grille**2-1:
            print("Bien joué, tu as touché",nbr_murs,"murs et attrapé",nbr_etoiles,"étoiles. GG ou pas")
            isPlay=False
        