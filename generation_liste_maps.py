def generation_liste():
    map_1_1=(("1111"))
    map_1_2=(("1111"))
    map_1=(map_1_1,map_1_2)
    map_2_1=(("1011","0110"),("1011","0101"))
    map_2_2=(("1011","0110"),("1011","0101"))
    map_2=(map_2_1,map_2_2)
    map_3_1=(("1010","0010","0111"),("1100","1000","0111"),("1101","1001","0111"))
    map_3_2=(("1010","0010","0111"),("1100","1000","0111"),("1101","1001","0111"))
    map_3=(map_3_1,map_3_2)
    map_4_1=(("1010","0010","0110","1110"),("1000","0101","1000","0100"),("1100","1011","0100","1100"),("1001","0111","1001","0101"))
    map_4_2=(("1010","0010","0110","1110"),("1000","0101","1000","0100"),("1100","1011","0100","1100"),("1001","0111","1001","0101"))
    map_4=(map_4_1,map_4_2)
    map_5_1=(("1011","0110","1011","0011","0110"),("1010","0101","1110","1110","1100"),("1001","0010","0000","0001","0101"),("1010","0101","1000","0111","1110"),("1101","1011","0001","0011","0101"))
    map_5_2=(("1011","0110","1011","0011","0110"),("1010","0101","1110","1110","1100"),("1001","0010","0000","0001","0101"),("1010","0101","1000","0111","1110"),("1101","1011","0001","0011","0101"))
    map_5=(map_5_1,map_5_2)
    map_6_1=(('1110', '1110', '1011', '0010', '0111', '1110'), ('1100', '1001', '0010', '0101', '1010', '0101'), ('1000', '0010', '0100', '1010', '0000', '0110'), ('1000', '0101', '1000', '0000', '0101', '1100'), ('1100', '1011', '0001', '0100', '1011', '0101'), ('1001', '0011', '0111', '1001', '0011', '0111'))
    map_6_2=(('1110', '1110', '1011', '0010', '0111', '1110'), ('1100', '1001', '0010', '0101', '1010', '0101'), ('1000', '0010', '0100', '1010', '0000', '0110'), ('1000', '0101', '1000', '0000', '0101', '1100'), ('1100', '1011', '0001', '0100', '1011', '0101'), ('1001', '0011', '0111', '1001', '0011', '0111'))
    map_6=(map_6_1,map_6_2)
    map_7_1=(('1010', '0010', '0111', '1010', '0011', '0110', '1110'), ('1101', '1000', '0010', '0100', '1110', '1101', '1100'), ('1011', '0100', '1001', '0100', '1001', '0010', '0101'), ('1110', '1001', '0110', '1001', '0010', '0101', '1110'), ('1001', '0110', '1000', '0010', '0000', '0011', '0101'), ('1110', '1001', '0000', '0101', '1100', '1011', '0110'), ('1001', '0011', '0101', '1011', '0001', '0011', '0101'))
    map_7_2=(('1010', '0010', '0111', '1010', '0011', '0110', '1110'), ('1101', '1000', '0010', '0100', '1110', '1101', '1100'), ('1011', '0100', '1001', '0100', '1001', '0010', '0101'), ('1110', '1001', '0110', '1001', '0010', '0101', '1110'), ('1001', '0110', '1000', '0010', '0000', '0011', '0101'), ('1110', '1001', '0000', '0101', '1100', '1011', '0110'), ('1001', '0011', '0101', '1011', '0001', '0011', '0101'))
    map_7=(map_7_1,map_7_2)
    map_8_1=(('1010', '0010', '0010', '0111', '1010', '0010', '0010', '0110'), ('1001', '0000', '0001', '0010', '0000', '0100', '1001', '0100'), ('1110', '1000', '0010', '0000', '0001', '0001', '0010', '0100'), ('1100', '1001', '0100', '1101', '1011', '0110', '1000', '0100'), ('1000', '0010', '0000', '0111', '1110', '1100', '1000', '0100'), ('1001', '0000', '0001', '0010', '0001', '0100', '1000', '0100'), ('1010', '0100', '1110', '1000', '0010', '0101', '1000', '0100'), ('1001', '0101', '1001', '0001', '0101', '1011', '0001', '0101'))
    map_8_2=(('1010', '0010', '0010', '0111', '1010', '0010', '0010', '0110'), ('1001', '0000', '0001', '0010', '0000', '0100', '1001', '0100'), ('1110', '1000', '0010', '0000', '0001', '0001', '0010', '0100'), ('1100', '1001', '0100', '1101', '1011', '0110', '1000', '0100'), ('1000', '0010', '0000', '0111', '1110', '1100', '1000', '0100'), ('1001', '0000', '0001', '0010', '0001', '0100', '1000', '0100'), ('1010', '0100', '1110', '1000', '0010', '0101', '1000', '0100'), ('1001', '0101', '1001', '0001', '0101', '1011', '0001', '0101'))
    map_8=(map_8_1,map_8_2)

    liste_maps=(map_1,map_2,map_3,map_4,map_5,map_6,map_7,map_8)
    print(liste_maps)

def creation_maps(taille:int):
    generated_one=((input() for i in range(taille)) for j in range(taille))
    return generated_one

def creation_map_intereactive(taille:int):
    grille_murs=[["" for i in range(taille)] for j in range(taille)]
    for i in range(taille):
        for j in range(taille):
            gauche,droite,haut,bas=False,False,False,False
            grille_murs[i][j]="X"
            print("=====================================")
            for a in grille_murs:
                print(a)
            print("=====================================")
            commande=input("zqsd pour murs : ")
            commande=commande.lower()
            for b in commande:
                if b=="z":     
                    haut = not haut
                elif b=="q":
                    gauche = not gauche
                elif b=="s":
                    bas = not bas
                elif b=="d":
                    droite = not droite
                else:
                    print(b+': commande non reconnue')
            murs_locaux=""
            if gauche:
                murs_locaux=murs_locaux+'1'
            else:
                murs_locaux=murs_locaux+'0'
            if droite:
                murs_locaux=murs_locaux+'1'
            else:
                murs_locaux=murs_locaux+'0'
            if haut:
                murs_locaux=murs_locaux+'1'
            else:
                murs_locaux=murs_locaux+'0'
            if bas:
                murs_locaux=murs_locaux+'1'
            else:
                murs_locaux=murs_locaux+'0'
            grille_murs[i][j]=murs_locaux
    print(grille_murs)