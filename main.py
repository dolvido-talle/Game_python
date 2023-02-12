
import time
import pygame
import math
from game import Game
from player import Player

pygame.init()


# definir une clock pour les fps
clock= pygame.time.Clock()
FPS= 75

# titre du jeux
pygame.display.set_caption("jeux de meteorite")

# dimension de l'ecran
screen = pygame.display.set_mode((1000, 600))

# mettre une image en arriere plan du jeux
background = pygame.image.load('assets/bg.jpg')

# importer une banniere
banner= pygame.image.load('assets/banner.png')
banner= pygame.transform.scale(banner,(500,500))
banner_rect= banner.get_rect()
banner_rect.x=math.ceil(screen.get_width()/4)

# importer charger le button pour lancer la partie
play_button=pygame.image.load('assets/button.png')
play_button=pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y= math.ceil(screen.get_height()/1.7)
# charger le joueur
# player= Player()


# charger jeux
game = Game()

# boucle pour l'ouverture et fermeture de la fenetre

running = True
while running:

    # appliquer l'arriere plan du jeux et definir sa taille
    screen.blit(background, (0, -300))
     # verifier si le jeu a commencer ou non
    if game.is_playing:
        game.update(screen)

        # verifier si le jeu n'a pas commencer
    else:

        # ajouter un ecran de bienvenu
        screen.blit(play_button, play_button_rect)
        screen.blit(banner,banner_rect)


    # mettre a jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        # permet de dire que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            print("fermeture de la fenetre")


            # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_1:
                # mettre pause
                time_duration = 3
                time.sleep(time_duration)


            if event.key == pygame.K_SPACE:

                if game.is_playing:

                  game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancer
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')



        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier si la souris est en collison avec le boutton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
              game.start()
              # jouer le son
              game.sound_manager.play('click')

            # quelle touche a été utilisée
            # if event.key==pygame.K_RIGHT:
            #   game.player.move_right()
            # elif event.key==pygame.K_LEFT:
            #   game.player.move_left()
    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)