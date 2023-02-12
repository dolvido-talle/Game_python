import pygame
import random
import animation


# definir la classe monstre
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        # self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        # random.randint(0, 600) permet de dire que un monstre peut apparaitre entre 1000 et 1600
        self.rect.x = 1000 + random.randint(0, 600)
        self.rect.y = 440 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    # 10 score different pour alien
    def set_loot_amount(self, amount):
        self.loot_amount = amount

    # fonction pour infliger les degats
    def damage(self, amount):
        # if self.health - amount > amount:
        # infliger les degats
        self.health -= amount

        # verifier si son nouveau nombre de points de vie est <= 0
        if self.health <= 0:
            # reapparaitre comme un new monstre
            self.rect.x = 1000 + random.randint(0, 600)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # 10 : ajouter le nombre de points
            self.game.add_score(self.loot_amount)

            # si la barre d'evenement est charger au maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)
                # appel de methode pour essayer de declencher la pluie de cometes
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

        # fonction pour barre de vie

    def update_health_bar(self, surface):
        # definir une couleur pour jauge de vie(vert clair)
        #  bar_color = ( 111, 210, 46)
        #  # definir une couleur pour l'arriere plan de la jauge
        #  back_bar_color=(60,63,60)
        # # definir la position de notre jauge de vie ainsi que la largeur et son epaisseur
        # [self.rect.x + 10,self.rect.y -20,self.health,5]
        # # definir la postion de l'arriere plan de la jauge de vie
        #  [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement se fait s'il ya pas de de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est collision avec le joueur
        else:
            # infliger des degats
            self.game.player.damage(self.attack)


# definir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        # nombre de points lorsquon tue
        self.set_loot_amount(20)


# definir la class alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 140)
        self.health = 250
        self.max_health = 250
        self.attack = 0.5
        self.set_speed(1)
        # nombre de points lorsquon tue
        self.set_loot_amount(80)
