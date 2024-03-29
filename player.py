import pygame

from projectile import Projectile
import animation


# creons une classe qui va representer notre joueur
# sprite est la methode pour deplacement du joueur et Sprite est la classe des elemts visibles du jeux


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        # self.image=pygame.image.load('assets/player.png')
        # creation d'un recctangle pour contenir le joueur
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

    def damage(self, amount):
        self.health -= amount
        if self.health - amount < amount:
            # si le joueur n'a plus de point de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        # dessiner la bar de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):
        # definir object projectile
        # projectile=  Projectile()
        self.all_projectiles.add(Projectile(self))
        # demarrer l'animation du lancer
        self.start_animation()
        # jouer le son
        self.game.sound_manager.play('tir')

    # deplacemnt du joueur
    def move_right(self):
        # si le joueur n'est pas en collision avec le monstre alors il se deplace
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
