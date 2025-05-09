import pygame

pygame.init()

sous_marin=pygame.image.load("img/sousmarin.png")
etoile=pygame.image.load("img/etoile.png")
background=pygame.image.load("img/background.jpg")
background=pygame.transform.scale(background,(1280, 720))
screen=pygame.display.set_mode((1280, 720))
background_labyrinthe=pygame.Surface((1100,700))
background_score=pygame.Surface((120,700))
background_labyrinthe.fill((0,0,0))
background_score.fill((255,255,255))
screen.blit(background,(0,0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c:
                screen.blit(background_labyrinthe,(20,10))
                screen.blit(background_score,(1160,10))
                pygame.display.flip()
