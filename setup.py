import pygame
pygame.init()
# titre du jeux
pygame.display.set_caption("jeux de meteorite")
# dimension de l'ecran
screen = pygame.display.set_mode((1000, 600))
# mettre une image en arriere plan du jeux
background = pygame.image.load('assets/bg.jpg')

running = True
while running:

    # appliquer l'arriere plan du jeux et definir sa taille
    screen.blit(background, (0, -300))
    # mettre a jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        # permet de dire que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            print("fermeture de la fenetre")


