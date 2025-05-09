import pygame

"""fichier pour comprendre comment utiliser la souris sur pygame"""

# variable pour les images
personnage = pygame.Surface((100, 100))
personnage.fill((255, 0, 0))
background = pygame.Surface((500, 500))

# donnée relative à la souris
mousePos = [0, 0]
isPressed = False

# variables de jeu
screen = pygame.display.set_mode((500, 500))
running = True

# boucle générale
while running:

    # affichage
    screen.blit(background, (0, 0))
    # on affiche le personnage en fonction de la position de la souris
    screen.blit(personnage, mousePos)

    # on récupère à chaque frame la position de la souris et si le joueur clique avec la souris
    mousePos = pygame.mouse.get_pos()
    isPressed = pygame.mouse.get_pressed(num_buttons=3)[0]

    # mise à jour de l'écran
    pygame.display.flip()

    # on parcourt les évènements de pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


# à toi de jouer : fait en sorte que la souris soit au milieu du rectangle !
