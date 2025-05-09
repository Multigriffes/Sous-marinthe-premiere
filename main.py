import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True

# sandwich en rouge
sandwich = pygame.Surface((200, 200))
sandwich.fill((255, 0, 0))
# rectangle du sandwich
sandwich_rect = sandwich.get_rect()

# mouette en bleu
mouette = pygame.Surface((100, 100))
mouette.fill((0, 0, 255))
# rectangle de la mouette
mouette_rect = mouette.get_rect()

background = pygame.Surface((500, 500))

# à utiliser uniquement avec la programmation orientée objet
# pygame.sprite.collide_mask(sprite1, sprite2)

while running:

    # si les rectangles correspondant aux images entrent en collision
    if sandwich_rect.colliderect(mouette_rect):
        print("collision")

    # affichage
    screen.blit(background, (0, 0))
    # on affiche l'image à la position du rectangle lui correspondant
    screen.blit(sandwich, sandwich_rect)
    screen.blit(mouette, mouette_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mouette_rect.y -= 10
            elif event.key == pygame.K_DOWN:
                mouette_rect.y += 10
            elif event.key == pygame.K_RIGHT:
                mouette_rect.x += 10
            elif event.key == pygame.K_LEFT:
                mouette_rect.x -= 10



