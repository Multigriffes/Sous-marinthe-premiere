import pygame

"""fichier pour comprendre comment faire bouger des images à l'aide des inputs gérés par pygame"""

# variable pour les images
personnage = pygame.Surface((100, 100))
# on colorie le personnage en rouge
personnage.fill((255, 0, 0))
# variable qui stocke la position en y du personnage
y = 400
# fond noir
background = pygame.Surface((500, 500))

# variables de jeu
screen = pygame.display.set_mode((500, 500))
running = True

# boucle générale
while running:

    # on affiche d'abord le fond d'écran
    screen.blit(background, (0, 0))
    # puis on affiche le personnage
    screen.blit(personnage, (400, y))
    # on met à jour l'écran /!\ à ne pas oublier /!\
    pygame.display.flip()

    # on parcourt les évènements de pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # si un des évènements dans la liste des évènements de pygame est : "une touche est pressée"
        if event.type == pygame.KEYDOWN:
            # si la touche pressée est la flèche du haut
            if event.key == pygame.K_UP:
                # on fait monter notre personnage vers le haut
                y -= 10
