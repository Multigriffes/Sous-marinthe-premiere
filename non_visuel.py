from random import randint

def creation_grille_joueur(taille_grille:int=5,pos_joueur:list=[]):
    assert type(taille_grille)==int ;"la taille de la grille n'est pas un int"
    if pos_joueur==[]:
        pos_joueur=[randint(0,taille_grille),randint(0,taille_grille)]
    grille_joueur=