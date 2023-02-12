import pygame
from comet import Comet


# create une classe pour gerer les evement avant que les comettes ne tombent
class CometFallEvent:

    # lors du chargement -> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour stocker nos comettes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    # ajouter 10 comettes
    def meteor_fall(self):
        # boucle permettant de ajouter 10 comettes
        for i in range(1, 10):
            # apparaitre 1 premiere comette
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'evenement est totalemnt charger
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de cometes")
            self.meteor_fall()
            # self.reset_percent()
            self.fall_mode = True  # activer la pluie de comete

    def update_bar(self, surface):
        # ajouter du pourcentage a la barre
        self.add_percent()

        # barre noir en arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0,  # laxe des x
            surface.get_height() - 20,  # laxe des y
            surface.get_width(),  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
        #   barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # laxe des x
            surface.get_height() - 20,  # laxe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
