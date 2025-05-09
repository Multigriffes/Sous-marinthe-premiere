import pygame

"""fichier pour comprendre la gestion de l'image avec pygame"""

screen = pygame.display.set_mode((500, 500))

# on charge une image pour la stocker dans une variable, ici image
image = pygame.image.load('mon_image.png')
# on transforme la taille de l'image et on stocke cette image déformée dans l'ancienne variable image
# pour écraser l'ancienne (il existe plein d'autres fonctionnalités pour transformer une image avec pygame !)
image = pygame.transform.scale(image, (10, 10))
# on affiche l'image sur l'écran
screen.blit(image, (0, 0))

# A votre tour implémentez des images dans votre code et jouer avec les outils de transformation que procure pygame !!!
