from random import randint
from lib.generation_liste_maps import generation_liste
from lib.input import *
import pygame

pygame.font.init()
pygame.mixer.init()

#J'ai fait une régression qui ma donner que chaque taille de font compte pour 0.6805789px pour le texte "Wasted"
#Et que la largeur est 3.58 x la hauteur

bop = pygame.mixer.Sound("sound/pop-331049.mp3")

screenXY=(1920,1080)
windowXY=(0.6*screenXY[0],0.6*screenXY[1])
background_labyrintheXY=(0.86*windowXY[0],0.97*windowXY[1])
background_scoreXY=(0.1*windowXY[0],0.97*windowXY[1])
background_wastedXY=(windowXY[0],0.25*windowXY[1])
text_wastedXY=(0.98*background_wastedXY[1]*3.58,0.98*background_wastedXY[1])
victory_bannerXY=(0.8*windowXY[0], 0.8*windowXY[1])

taille_font_wasted=text_wastedXY[1]//0.6805789

pos_background_labyrinthe=(0.0156*windowXY[0],0.0139*windowXY[1])
pos_background_score=(0.89*windowXY[0],0.0139*windowXY[1])
pos_background_wasted=(0,windowXY[1]/2-background_wastedXY[1]/2)
pos_text_wasted=(windowXY[0]/2-text_wastedXY[0]/2,windowXY[1]/2-text_wastedXY[1]/2)
pos_victory_banner=(windowXY[0]/2-victory_bannerXY[0]/2, windowXY[1]/2-victory_bannerXY[1]/2)

background=pygame.image.load("img/background.jpg")
background=pygame.transform.scale(background,windowXY)

victory_banner=pygame.image.load("img/victoire.png")
victory_banner=pygame.transform.scale(victory_banner,victory_bannerXY)

background_labyrinthe=pygame.Surface(background_labyrintheXY)
background_labyrinthe.fill((0,0,0))

background_score=pygame.Surface(background_scoreXY)
background_score.fill((255,255,255))

background_wasted=pygame.Surface(background_wastedXY)
background_wasted.fill((255,0,0))
text_wasted_font=pygame.font.SysFont(None,round(text_wastedXY[1]/0.6805789),True)
text_wasted=pygame.font.Font.render(text_wasted_font,"Wasted",True,(255,255,255))


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
        if len(pos_joueur)!=2:
            print("Y a 2 nombres pour une coordonnées en 2D idiots, génération aléatoire...")
            pos_joueur=[]
    else:
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
    bop.play(loops=0, maxtime=0, fade_ms=0)

    
    for j in commande:
        grille_joueur[pos_joueur[1]][pos_joueur[0]]=" "
        if j=="d":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][1]=="0":
                pos_joueur[0]+=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                nbr_murs+=1
                screen=affichage_wasted(screen)
        elif j=="q":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][0]=="0":
                pos_joueur[0]-=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                nbr_murs+=1
                screen=affichage_wasted(screen)
        elif j=="z":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][2]=="0":
                pos_joueur[1]-=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                nbr_murs+=1
                screen=affichage_wasted(screen)
        elif j=="s":
            if grille_murs[pos_joueur[1]][pos_joueur[0]][3]=="0":
                pos_joueur[1]+=1
                if grille_joueur[pos_joueur[1]][pos_joueur[0]]=="*":
                    nbr_etoiles+=1
            else:
                nbr_murs+=1
                screen=affichage_wasted(screen)
        else:
            print(j+" : La commande n'est pas reconnu")
    grille_joueur[pos_joueur[1]][pos_joueur[0]]="O"
    return [grille_joueur,pos_joueur,nbr_etoiles,nbr_murs,screen]

def affichage_wasted(screen):
    screen.blit(background_wasted,pos_background_wasted)
    screen.blit(text_wasted,pos_text_wasted)
    pygame.display.flip()
    pygame.time.wait(1000)
    return screen

def affichage(grille_joueur,nbr_etoiles,nbr_murs,screen,caseXY,sous_marin,etoile,case):

    assert type(grille_joueur)==list, "grille_joueur n'est pas une liste"
    assert type(nbr_etoiles)==int, "nbr_etoiles n'est pas un int"
    assert type(nbr_murs)==int, "nbr_murs n'est pas un int"

    screen.blit(background,(0,0))
    screen.blit(background_labyrinthe,pos_background_labyrinthe)
    screen.blit(background_score,pos_background_score)
    for y in range(len(grille_joueur)):
        for x in range(len(grille_joueur)):
            screen.blit(case,(pos_background_labyrinthe[0]+(x+0.05)*caseXY[0],pos_background_labyrinthe[1]+(y+0.05)*caseXY[1]))
            if grille_joueur[y][x]=='O':
                screen.blit(sous_marin,(pos_background_labyrinthe[0]+(x+0.05)*caseXY[0],pos_background_labyrinthe[1]+(y+0.05)*caseXY[1]))
            elif grille_joueur[y][x]=='*':
                screen.blit(etoile,(pos_background_labyrinthe[0]+(x+0.05)*caseXY[0],pos_background_labyrinthe[1]+(y+0.05)*caseXY[1]))

    pygame.display.flip()

    return screen

def play():
    '''
    Fonction pour le lancement du jeu, initialisation des variables puis boucle de jeu
    '''
    #Initialisation avec input joueur
    nbr_etoiles,nbr_murs,isPlay=0,0,True
    sous_marin=pygame.image.load("img/sousmarin.png")
    etoile=pygame.image.load("img/etoile.png")

    taille_grille=input_taille_grille()
    caseXY=(background_labyrintheXY[0]/taille_grille,background_labyrintheXY[1]/taille_grille)
    case=pygame.Surface((caseXY[0]*0.9,caseXY[1]*0.9))
    case.fill((255,255,255))
    sous_marin=pygame.transform.scale(sous_marin,(caseXY[0]*0.9,caseXY[1]*0.9))
    etoile=pygame.transform.scale(etoile,(caseXY[0]*0.9,caseXY[1]*0.9))

    pos_joueur=input_pos_joueur()

    grille_joueur,grille_murs,pos_joueur=creation_grille_joueur(taille_grille,pos_joueur)

    pygame.init()
    screen=pygame.display.set_mode(windowXY)

    #Gestion du son/musique :
    son = pygame.mixer.Sound('sound/epical-music-background-337255.mp3')
    son.play(loops=-1, maxtime=0, fade_ms=0)

    while isPlay:#Boucle de jeu
        screen=affichage(grille_joueur,nbr_etoiles,nbr_murs,screen,caseXY,sous_marin,etoile,case)
        pygame.time.wait(50)
        commande=""
        while commande=="":
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    isPlay=False
                    commande='quit'
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
        if commande!='quit':
            grille_joueur,pos_joueur,nbr_etoiles,nbr_murs,screen=action(commande,grille_joueur,grille_murs,pos_joueur,nbr_etoiles,nbr_murs,screen) # type: ignore
        else:
            pygame.quit()
        if nbr_etoiles==taille_grille**2-1:
            screen=affichage(grille_joueur,nbr_etoiles,nbr_murs,screen,caseXY,sous_marin,etoile,case)
            screen.blit(victory_banner, pos_victory_banner)

            pygame.mixer.Sound.stop(son)
            son_victory = pygame.mixer.Sound('sound/Voicy_macarena.mp3')
            son_victory.play(loops=0, maxtime=0, fade_ms=0)

            pygame.display.flip()
            print("Bien joué, tu as touché",nbr_murs,"murs et attrapé",nbr_etoiles,"étoiles. GG ou pas")
            pygame.time.wait(20000)
            isPlay=False
            pygame.quit()