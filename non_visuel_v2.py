from random import randint

map1=([("1011"),("0110"),("1011"),("0011"),("0110")],
[("1010"),("0101"),("1110"),("1110"),("1100")],
[("1001"),("0010"),("0000"),("0001"),("0101")],
[("1010"),("0101"),("1000"),("0111"),("1110")],
[("1101"),("1011"),("0001"),("0011"),("0101")])


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