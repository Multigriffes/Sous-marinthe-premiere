import pygame

"""fichier pour comprendre comment gérer les inputs avec pygame"""
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True

while running:

    for event in pygame.event.get():

        # si un des évènements dans la liste des évènements de pygame est : "une touche est pressée"
        if event.type == pygame.KEYDOWN:
            # si la touche pressée est la flèche du haut
            if event.key == pygame.K_UP:
                print("UP")



