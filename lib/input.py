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