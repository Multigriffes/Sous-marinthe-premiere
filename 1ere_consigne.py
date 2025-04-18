from random import randint
from generation_liste_maps import generation_liste
import pygame

color={"blanc":(255,255,255),"noir":(0,0,0)}

sous_marin=pygame.image.load("img/sousmarin.png")
etoile=pygame.image.load("img/etoile.png")
background=pygame.Surface((550,550))
background.fill(color["blanc"])


#Creation des grilles
def creation_grille_joueur(taille_grille:int,pos_joueur:list=[]):
    """
    Cette fonction créé la liste représentant la grille et représente le joueur dessus à l'aide 
    d'un "O" et les cases vides avec un "*"
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

    #Création de la grille du joueur
    grille_joueur = [["*" for i in range(taille_grille)] for b in range(taille_grille)]
    grille_joueur[pos_joueur[1]][pos_joueur[0]] = "O"

    #Choix de le map en fonction du nbr de cases
    grille_murs = generation_liste()[taille_grille-2][randint(0,len(generation_liste()[taille_grille-2])-1)]

    return [grille_joueur,grille_murs,pos_joueur]

def action(commande:str,grille_joueur:list,grille_murs:list,pos_joueur:list,nbr_etoiles:int,nbr_murs:int,screen):
    """
    La fonction gère les action du joueur et sont influence sur les diffèrentes variables du jeu
    """

    assert type(commande) == str, "commande n'est pas un string"
    assert type(grille_joueur) == list, "grille_joueur n'est pas un list"
    assert type(grille_murs) == tuple, "grille_murs n'est pas un tuple"
    assert type(pos_joueur) == list, "pos_joueur n'est pas un list"
    assert type(nbr_etoiles) == int, "nbr_etoiles n'est pas un int"
    assert type(nbr_murs) == int, "nbr_murs n'est pas un int"
    
    for j in commande:
        grille_joueur[pos_joueur[1]][pos_joueur[0]]=" "
        if j=="d":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][1]=="0":
                pos_joueur[0]+=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                nbr_murs+=1
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
        elif j=="g" or j=="q":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][0]=="0":
                pos_joueur[0]-=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                nbr_murs+=1
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
        elif j=="h" or j=="z":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][2]=="0":
                pos_joueur[1]-=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                nbr_murs+=1
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
        elif j=="b" or j=="s":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][3]=="0":
                pos_joueur[1]+=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                nbr_murs+=1
                print("C'est un MUR CHEHHHHH !!!!!!!!!!")
        else:
            print(j+" : La commande n'est pas reconnu")
    grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
    return grille_joueur,pos_joueur,nbr_etoiles,nbr_murs

def affichage(grille_joueur,nbr_etoiles,nbr_murs,screen):

    assert type(grille_joueur)==list, "grille_joueur n'est pas une liste"
    assert type(nbr_etoiles)==int, "nbr_etoiles n'est pas un int"
    assert type(nbr_murs)==int, "nbr_murs n'est pas un int"

    screen.blit(background,(0,0))


    pygame.display.flip()

    return screen

def input_taille_grille():
    '''
    La fonction va gérer la demande de l'input du joueur pour la taille de la grille
    '''
    taille_grille=""
    while taille_grille=="":
        taille_grille=input("Taille de la grille souhaitée entre 2 et 15 : ")
        try:
            int(taille_grille)
        except:
            taille_grille=""
        else:
            taille_grille=int(taille_grille)
            if taille_grille>15 or taille_grille<2:
                taille_grille=""
    return taille_grille

def input_pos_joueur():
    '''
    La fonction va gérer la demande de l'input joueur pour la position du joueur
    '''
    pos_joueur=['default']
    while pos_joueur==['default']:
        pos_joueur=list(input("Position du joueur initiale si souhaité sinon laisser vide : "))
        #Nettoyage de la liste de string de la position
        if pos_joueur!=['default'] and pos_joueur!=[]:#Vérification du besoin de nettoyer la liste
            a=0
            for i in range(len(pos_joueur)):#Suppression de tout ce qui n'est pas un chiffre ou une virguel
                try:
                    int(pos_joueur[a])
                except:
                    if pos_joueur[a]==',':
                        a+=1
                    else:
                        del pos_joueur[a]
                else:
                    a+=1
            pos_joueur_temp,isVirgule,a=[],False,0
            for i in pos_joueur:#Rassemblement des potentiels nombre séparés par des virgules
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
                            pos_joueur_temp[a-1]=pos_joueur_temp[a-1]+i
                    isVirgule=False
            for i in range(len(pos_joueur_temp)):#Transformation des str de nombre en int
                pos_joueur_temp[i]=int(pos_joueur_temp[i])
            pos_joueur=pos_joueur_temp.copy()
    return pos_joueur

def play():
    '''
    Fonction pour le lancement du jeu, initialisation des variables puis boucle de jeu
    '''
    #Initialisation avec input joueur
    nbr_etoiles,nbr_murs,isPlay=0,0,True

    taille_grille=input_taille_grille()

    pos_joueur=input_pos_joueur()

    grille_joueur,grille_murs,pos_joueur=creation_grille_joueur(taille_grille,pos_joueur)

    pygame.init()
    screen=pygame.display.set_mode((750,550))
    screen.blit(background,(0,0))
    pygame.display.flip()

    while isPlay:#Boucle de jeu
        screen=affichage(grille_joueur,nbr_etoiles,nbr_murs,screen)
        pygame.time.wait(500)
        #Instructions de jeu et mise à jour des variables
        commande=""
        while commande=="":
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    isPlay=False
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_z or event.key==pygame.K_UP:
                        commande="z"
                    if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                        commande="s"
                    if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                        commande="d"
                    if event.key==pygame.K_q or event.key==pygame.K_LEFT:
                        commande="q"
                if event.type==pygame.KEYUP:
                    commande=""

        grille_joueur,pos_joueur,nbr_etoiles,nbr_murs,screen=action(commande,grille_joueur,grille_murs,pos_joueur,nbr_etoiles,nbr_murs,screen) # type: ignore

        if nbr_etoiles==taille_grille**2-1:
            print("Bien joué, tu as touché",nbr_murs,"murs et attrapé",nbr_etoiles,"étoiles. GG ou pas")
            pygame.time.wait(5000)
            isPlay=False
            pygame.quit()