from random import randint
from lib.generation_liste_maps import generation_liste
import pygame
pygame.init()


# 0=menu selection mode de jeu
# 1=menu selection taille mode de jeu 1
# 2=menu selection pos mode de jeu 1
# 3=menu selection taille mode de jeu 2
# 4=menu selection pos mode de jeu 2


def affichage(window,etape):
    if etape==0:
        window=affichage_menu_mode_jeu(window)
    elif etape==1:
        window=affichage_menu_taille_grille(window)
    elif etape==3:
        window=affichage_menu_taille_grille(window)

    return window



def size_computing_menu_mode_jeu(window):
# ____________________________________________________________
    # Création des textes
    title=title_font.render("Sous-Marinthe",False,(255, 122, 33))
    text_mode_jeu_1=title_font.render("Collecte toutes les étoiles",False,(0,0,0))
    text_mode_jeu_2=title_font.render("Atteint la porte",False,(0,0,0))
    text_createurs=title_font.render("Jonas Tourvieille, Baptiste Rigollet",False,(0,0,0))
# ____________________________________________________________
    # Taille des surfaces
    windowXY=window.get_size()
    backgroundXY=(windowXY[0]*1,windowXY[1]*1)
    titleXY=(backgroundXY[0]*0.8,backgroundXY[1]*0.3)
    background_mode_jeuXY=(backgroundXY[0]*0.3,backgroundXY[1]*0.5)
    icon_mode_jeuXY=(0.775*background_mode_jeuXY[0],0.7*background_mode_jeuXY[1])
    text_mode_jeuXY=(0.8*background_mode_jeuXY[0],0.22*background_mode_jeuXY[1])
    text_createursXY=(0.4*backgroundXY[0],backgroundXY[1]*0.05)

# ____________________________________________________________
    # Création des surfaces pleine
    background_mode_jeu=pygame.Surface(background_mode_jeuXY)
    background_mode_jeu.fill((110, 105, 92))

# ____________________________________________________________
    # Scaling des élèments
    background=pygame.transform.scale(background_image,backgroundXY)
    title=pygame.transform.scale(title,titleXY)
    icon_mode_jeu_1=pygame.transform.scale(etoile_image,icon_mode_jeuXY)
    icon_mode_jeu_2=pygame.transform.scale(porte_image,icon_mode_jeuXY)
    text_mode_jeu_1=pygame.transform.scale(text_mode_jeu_1,text_mode_jeuXY)
    text_mode_jeu_2=pygame.transform.scale(text_mode_jeu_2,text_mode_jeuXY)
    text_createurs=pygame.transform.scale(text_createurs,text_createursXY)

    
# ____________________________________________________________
    # Position des élèments
    background_pos=(0,0)
    title_pos=(backgroundXY[0]/2-titleXY[0]/2,backgroundXY[1]*0.03)
    background_mode_jeu_1_pos=(backgroundXY[0]*0.13,backgroundXY[1]*0.35)
    background_mode_jeu_2_pos=(backgroundXY[0]-backgroundXY[0]*0.13-background_mode_jeuXY[0],backgroundXY[1]*0.35)
    icon_mode_jeu_1_pos=(background_mode_jeu_1_pos[0]+background_mode_jeuXY[0]/2-icon_mode_jeuXY[0]/2,background_mode_jeu_1_pos[1]+background_mode_jeuXY[1]*0.01)
    icon_mode_jeu_2_pos=(background_mode_jeu_2_pos[0]+background_mode_jeuXY[0]/2-icon_mode_jeuXY[0]/2,background_mode_jeu_2_pos[1]+background_mode_jeuXY[1]*0.01)
    text_mode_jeu_1_pos=(background_mode_jeu_1_pos[0]+background_mode_jeuXY[0]/2-text_mode_jeuXY[0]/2,background_mode_jeu_1_pos[1]+background_mode_jeuXY[1]*0.75)
    text_mode_jeu_2_pos=(background_mode_jeu_2_pos[0]+background_mode_jeuXY[0]/2-text_mode_jeuXY[0]/2,background_mode_jeu_2_pos[1]+background_mode_jeuXY[1]*0.75)
    text_createurs_pos=(background_mode_jeuXY[0]*0.05,backgroundXY[1]-text_createursXY[1])

# ____________________________________________________________

    return background_mode_jeuXY,background_mode_jeu,background,title,icon_mode_jeu_1,icon_mode_jeu_2,text_mode_jeu_1,text_mode_jeu_2,text_createurs,background_pos,title_pos,background_mode_jeu_1_pos,background_mode_jeu_2_pos,icon_mode_jeu_1_pos,icon_mode_jeu_2_pos,text_mode_jeu_1_pos,text_mode_jeu_2_pos,text_createurs_pos


def affichage_menu_mode_jeu(window):
    background_mode_jeuXY,background_mode_jeu,background,title,icon_mode_jeu_1,icon_mode_jeu_2,text_mode_jeu_1,text_mode_jeu_2,text_createurs,background_pos,title_pos,background_mode_jeu_1_pos,background_mode_jeu_2_pos,icon_mode_jeu_1_pos,icon_mode_jeu_2_pos,text_mode_jeu_1_pos,text_mode_jeu_2_pos,text_createurs_pos=size_computing_menu_mode_jeu(window)
    
    window.blit(background,background_pos)
    window.blit(title,title_pos)
    if background_mode_jeu_1_pos[0]<pygame.mouse.get_pos()[0]<background_mode_jeu_1_pos[0]+background_mode_jeuXY[0] and background_mode_jeu_1_pos[1]<pygame.mouse.get_pos()[1]<background_mode_jeu_1_pos[1]+background_mode_jeuXY[1]:
        background_mode_jeu.fill((148, 139, 115))
        window.blit(background_mode_jeu,background_mode_jeu_1_pos)
        background_mode_jeu.fill((110, 105, 92))
    else:
        window.blit(background_mode_jeu,background_mode_jeu_1_pos)
    if background_mode_jeu_2_pos[0]<pygame.mouse.get_pos()[0]<background_mode_jeu_2_pos[0]+background_mode_jeuXY[0] and background_mode_jeu_2_pos[1]<pygame.mouse.get_pos()[1]<background_mode_jeu_2_pos[1]+background_mode_jeuXY[1]:
        background_mode_jeu.fill((148, 139, 115))
        window.blit(background_mode_jeu,background_mode_jeu_2_pos)
        background_mode_jeu.fill((110, 105, 92))
    else:
        window.blit(background_mode_jeu,background_mode_jeu_2_pos)
    window.blit(icon_mode_jeu_1,icon_mode_jeu_1_pos)
    window.blit(icon_mode_jeu_2,icon_mode_jeu_2_pos)
    window.blit(text_mode_jeu_1,text_mode_jeu_1_pos)
    window.blit(text_mode_jeu_2,text_mode_jeu_2_pos)
    window.blit(text_createurs,text_createurs_pos)

    pygame.display.flip()
    return window


def size_computing_menu_taille_grille(window):
# ____________________________________________________________
    # Création des textes
    text_taille_2=title_font.render("2",False,(0,0,0))
    text_taille_3=title_font.render("3",False,(0,0,0))
    text_taille_4=title_font.render("4",False,(0,0,0))
    text_taille_5=title_font.render("5",False,(0,0,0))
    text_taille_6=title_font.render("6",False,(0,0,0))
    text_taille_7=title_font.render("7",False,(0,0,0))
    text_taille_8=title_font.render("8",False,(0,0,0))
    text_taille_9=title_font.render("9",False,(0,0,0))
    text_taille_10=title_font.render("10",False,(0,0,0))
    text_taille_11=title_font.render("11",False,(0,0,0))
    text_taille_12=title_font.render("12",False,(0,0,0))
    text_taille_13=title_font.render("13",False,(0,0,0))
    text_taille_14=title_font.render("14",False,(0,0,0))
    text_taille_15=title_font.render("15",False,(0,0,0))
    title_menu_taille_grille=title_font.render("Choisi la taille de la grille",False,(0,0,0))
    title_menu_pos_grille=title_font.render("Choisi la position de départ",False,(0,0,0))
# ____________________________________________________________
    # Taille des surfaces
    windowXY=window.get_size()
    backgroundXY=(windowXY[0]*1,windowXY[1]*1)
    titleXY=(backgroundXY[0]*0.8,backgroundXY[1]*0.15)
    background_tailleXY=(backgroundXY[0]*0.08,backgroundXY[1]*0.1)
    text_tailleXY=(1*background_tailleXY[0],1*background_tailleXY[1])

# ____________________________________________________________
    # Création des surfaces pleine


# ____________________________________________________________
    # Scaling des élèments
    background=pygame.transform.scale(background_image,backgroundXY)
    title_menu_taille_grille=pygame.transform.scale(title_menu_taille_grille,titleXY)
    text_taille_2=pygame.transform.scale(text_taille_2,text_tailleXY)
    text_taille_3=pygame.transform.scale(text_taille_3,text_tailleXY)
    text_taille_4=pygame.transform.scale(text_taille_4,text_tailleXY)
    text_taille_5=pygame.transform.scale(text_taille_5,text_tailleXY)
    text_taille_6=pygame.transform.scale(text_taille_6,text_tailleXY)
    text_taille_7=pygame.transform.scale(text_taille_7,text_tailleXY)
    text_taille_8=pygame.transform.scale(text_taille_8,text_tailleXY)
    text_taille_9=pygame.transform.scale(text_taille_9,text_tailleXY)
    text_taille_10=pygame.transform.scale(text_taille_10,text_tailleXY)
    text_taille_11=pygame.transform.scale(text_taille_11,text_tailleXY)
    text_taille_12=pygame.transform.scale(text_taille_12,text_tailleXY)
    text_taille_13=pygame.transform.scale(text_taille_13,text_tailleXY)
    text_taille_14=pygame.transform.scale(text_taille_14,text_tailleXY)
    text_taille_15=pygame.transform.scale(text_taille_15,text_tailleXY)
    
# ____________________________________________________________
    # Position des élèments
    background_pos=(0,0)
    title_menu_taille_grille_pos=(backgroundXY[0]/2-titleXY[0]/2,backgroundXY[1]*0.03)
    text_taille_pos=(0.1*backgroundXY[0],0.3*backgroundXY[1])

# ____________________________________________________________
    return backgroundXY,background,title_menu_taille_grille,text_taille_2,text_taille_3,text_taille_4,text_taille_5,text_taille_6,text_taille_7,text_taille_8,text_taille_9,text_taille_10,text_taille_11,text_taille_12,text_taille_13,text_taille_14,text_taille_15,background_pos,title_menu_taille_grille_pos,text_taille_pos


def affichage_menu_taille_grille(window):
    backgroundXY,background,title_menu_taille_grille,text_taille_2,text_taille_3,text_taille_4,text_taille_5,text_taille_6,text_taille_7,text_taille_8,text_taille_9,text_taille_10,text_taille_11,text_taille_12,text_taille_13,text_taille_14,text_taille_15,background_pos,title_menu_taille_grille_pos,text_taille_pos=size_computing_menu_taille_grille(window)

    window.blit(background,background_pos)
    window.blit(title_menu_taille_grille,title_menu_taille_grille_pos)
    for i in range(14):
        if i<7:
            if i==0:
                window.blit(text_taille_2,(text_taille_pos[0]+backgroundXY[0]*0.12*i,text_taille_pos[1]))
            elif i==1:
                window.blit(text_taille_3,(text_taille_pos[0]+backgroundXY[0]*0.12*i,text_taille_pos[1]))
            elif i==2:
                window.blit(text_taille_4,(text_taille_pos[0]+backgroundXY[0]*0.12*i,text_taille_pos[1]))
            elif i==3:
                window.blit(text_taille_5,(text_taille_pos[0]+backgroundXY[0]*0.12*i,text_taille_pos[1]))
            elif i==4:
                window.blit(text_taille_6,(text_taille_pos[0]+backgroundXY[0]*0.12*i,text_taille_pos[1]))
            elif i==5:
                window.blit(text_taille_7,(text_taille_pos[0]+backgroundXY[0]*0.12*i,text_taille_pos[1]))
            elif i==6:
                window.blit(text_taille_8,(text_taille_pos[0]+backgroundXY[0]*0.12*i,text_taille_pos[1]))
        else:
            print(i)
            if i==7:
                window.blit(text_taille_9,(text_taille_pos[0]+backgroundXY[0]*0.12*(i-7),text_taille_pos[1]+backgroundXY[1]*0.25))
            elif i==8:
                window.blit(text_taille_10,(text_taille_pos[0]+backgroundXY[0]*0.12*(i-7),text_taille_pos[1]+backgroundXY[1]*0.25))
            elif i==9:
                window.blit(text_taille_11,(text_taille_pos[0]+backgroundXY[0]*0.12*(i-7),text_taille_pos[1]+backgroundXY[1]*0.25))
            elif i==10:
                window.blit(text_taille_12,(text_taille_pos[0]+backgroundXY[0]*0.12*(i-7),text_taille_pos[1]+backgroundXY[1]*0.25))
            elif i==11:
                window.blit(text_taille_13,(text_taille_pos[0]+backgroundXY[0]*0.12*(i-7),text_taille_pos[1]+backgroundXY[1]*0.25))
            elif i==12:
                window.blit(text_taille_14,(text_taille_pos[0]+backgroundXY[0]*0.12*(i-7),text_taille_pos[1]+backgroundXY[1]*0.25))
            elif i==13:
                window.blit(text_taille_15,(text_taille_pos[0]+backgroundXY[0]*0.12*(i-7),text_taille_pos[1]+backgroundXY[1]*0.25))

    pygame.display.flip()
    return window


def action(etape,event):
    if etape==0:
        if event.type==pygame.MOUSEBUTTONDOWN:
            background_mode_jeuXY,background_mode_jeu,background,title,icon_mode_jeu_1,icon_mode_jeu_2,text_mode_jeu_1,text_mode_jeu_2,text_createurs,background_pos,title_pos,background_mode_jeu_1_pos,background_mode_jeu_2_pos,icon_mode_jeu_1_pos,icon_mode_jeu_2_pos,text_mode_jeu_1_pos,text_mode_jeu_2_pos,text_createurs_pos=size_computing_menu_mode_jeu(window)
            if background_mode_jeu_1_pos[0]<pygame.mouse.get_pos()[0]<background_mode_jeu_1_pos[0]+background_mode_jeuXY[0] and background_mode_jeu_1_pos[1]<pygame.mouse.get_pos()[1]<background_mode_jeu_1_pos[1]+background_mode_jeuXY[1]:
                etape=1  
            elif background_mode_jeu_2_pos[0]<pygame.mouse.get_pos()[0]<background_mode_jeu_2_pos[0]+background_mode_jeuXY[0] and background_mode_jeu_2_pos[1]<pygame.mouse.get_pos()[1]<background_mode_jeu_2_pos[1]+background_mode_jeuXY[1]:
                etape=3
    elif etape==1:
        pass
        
    elif etape==2:
        pass

    elif etape==3:
        pass

    elif etape==4:
        pass
    
    return etape


# ____________________________________________________________
# Calcule de la taille initiale de la fenetre
window=pygame.display.set_mode()
windowXY=window.get_size()
windowXY=(windowXY[0]*0.8,windowXY[1]*0.8)
window=pygame.display.set_mode((windowXY),pygame.RESIZABLE)
# ____________________________________________________________
# Création des fonts
title_font=pygame.font.SysFont(None,300,False)
# ____________________________________________________________
# Chargement des images
background_image=pygame.image.load("img/background.jpg")
victory_banner_image=pygame.image.load("img/victoire.png")
etoile_image=pygame.image.load("img/etoile.png")
porte_image=pygame.image.load("img/porte.png")
sous_marin_image=pygame.image.load("img/sousmarin.png")
    
# ____________________________________________________________






etape,run=0,True
window=affichage(window,etape)
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN:
            etape=action(etape,event)
            print("Action de l'utilisateur")
        elif event.type==pygame.VIDEORESIZE or event.type==pygame.VIDEOEXPOSE:
            print("Window size changed")
    window=affichage(window,etape)
pygame.quit()