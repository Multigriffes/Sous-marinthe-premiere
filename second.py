import pygame
pygame.init()

screen=pygame.display.set_mode((1000,900))

img1 = pygame.image.load("C:/Users/Multi/Documents/GitHub/Unique/Pygame/Apprentissage/img/Capture d’écran 2024-11-17 232615.png")
img1 = pygame.transform.scale(img1, (500,500))

img2 = pygame.image.load("C:/Users/Multi/Documents/GitHub/Unique/Pygame/Apprentissage/img/Capture d’écran 2024-11-17 232648.png")
img2 = pygame.transform.scale(img2, (500,500))

img3 = pygame.image.load("C:/Users/Multi/Documents/GitHub/Unique/Pygame/Apprentissage/img/Capture d’écran 2024-11-30 173711.png")
img3 = pygame.transform.scale(img3, (500,500))

img4 = pygame.image.load("C:/Users/Multi/Documents/GitHub/Unique/Pygame/Apprentissage/img/Capture d’écran 2024-12-02 230328.png")
img4 = pygame.transform.scale(img4, (500,500))

img5 = pygame.image.load("C:/Users/Multi/Documents/GitHub/Unique/Pygame/Apprentissage/img/Capture d’écran 2024-12-06 212933.png")
img5 = pygame.transform.scale(img5, (500,500))

img6 = pygame.image.load("C:/Users/Multi/Documents/GitHub/Unique/Pygame/Apprentissage/img/cheaters.png")
img6 = pygame.transform.scale(img6, (500,500))

img7 = pygame.image.load("C:/Users/Multi/Documents/GitHub/Unique/Pygame/Apprentissage/img/Mariste_logo.png")
img7 = pygame.transform.scale(img7, (500,500))


personnage = pygame.Surface((100,100))
personnage.fill((0,0,255))
posx = 1
posy = 1
a=0

running=True

keys = {"UP":False, "DOWN":False, "LEFT":False, "RIGHT":False}


while running:
    screen.fill((255,0,0))
    screen.blit(personnage,(posx,posy))
    pygame.display.flip()

    if keys["UP"] == True and keys["DOWN"]==False:
        posy-=1
    if keys["DOWN"] == True and keys["UP"]==False:
        posy+=1
    if keys["LEFT"] == True and keys["RIGHT"]==False:
        posx-=1
    if keys["RIGHT"] == True and keys["LEFT"]==False:
        posx+=1
        
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_z or event.key==pygame.K_UP:
                keys["UP"] = True 
            if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                keys["DOWN"] = True
            if event.key==pygame.K_q or event.key==pygame.K_LEFT:
                keys["LEFT"] = True
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                keys["RIGHT"] = True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_z or event.key==pygame.K_UP:
                keys["UP"] = False 
            if event.key==pygame.K_s or event.key==pygame.K_DOWN:
                keys["DOWN"] = False
            if event.key==pygame.K_q or event.key==pygame.K_LEFT:
                keys["LEFT"] = False
            if event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                keys["RIGHT"] = False
        
    