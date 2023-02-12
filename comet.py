import pygame
import random


# creer class pour gerer les cometes
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image de la comette
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 2)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # verifier si le nombre de cometes est de 0
        if len(self.comet_event.all_comets) == 0:
            print("evenement fini")
            # remetrre la barre a 0
            self.comet_event.reset_percent()
            # apparaitre les 2 premiers monstres()
            self.comet_event.game.start()
            # self.comet_event.game.spawn_monster()
            # self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 410:
            print("sol")
            # retirer boule de feu
            self.remove()

            # si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("evenement fini")
                # remetrre la jauge de vie au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            print("joueur toucher")
            # retirer la boule de feu
            self.remove()
            # subir 15 points de degats
            self.comet_event.game.player.damage(15)
