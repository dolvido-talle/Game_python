import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent
from monster import Mummy
from monster import Alien
from sounds import SoundManager


# classe qui va representer notre jeu

class Game:
  # __init__(self) represente le constructeur
  def __init__(self):

    # definir si notre joueur a commence ou non , mettre True pour desactiver et False pour ...
    self.is_playing = False
    # generer notre joueur
    self.all_players= pygame.sprite.Group()
    self.player= Player(self)
    self.all_players.add(self.player)
    # generer l'evenement
    self.comet_event= CometFallEvent(self)
    # creer groupe de monstre
    self.all_monsters= pygame.sprite.Group()
    # 10 gerer le son
    self.sound_manager = SoundManager()
    # mettre le score a 0
    self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)
    self.score= 0
    # self.max_score = 50
    self.pressed={}

# metode permettant de lancer le jeu
  def start(self):
    self.is_playing= True
    self.spawn_monster(Mummy)
    self.spawn_monster(Mummy)
    self.spawn_monster(Alien)

# metode permettant de'ajouter le score
  def add_score(self,points=10):
        self.max_score=100
        self.score += points
        import json
        # ENREGISTRER LE SCORE
        with open("fichier_scores.json", "w") as f_write:
          json.dump(f"votre ancien score est {self.score}", f_write)
        if self.score >= self.max_score:
              print(f"vous avez gagner et votre score est :  {self.score}")
              self.game_over()
              # self.image = pygame.image.load('assets/win.png')
              # self.rect = self.image.get_rect()
              # self.rect.x = 800
              # self.rect.y = 800
        print(f"votre score est {self.score}")
  def game_over(self):

     self.all_monsters= pygame.sprite.Group()
     self.comet_event.all_comets = pygame.sprite.Group()
     self.player.health= self.player.max_health
     self.comet_event.reset_percent()
     self.is_playing= False
     self.score=0


     # jouer le son
     self.sound_manager.play('game_over')





  # def score_over(self,amount):
  #   if self.score >= max_score:
  #     # si le joueur n'a plus de point de vie
  #     self.game.game_over()
  # while True:
  #  police= pygame.font.SysFont("monospace",15)
  #  image_text= police.render("VOUS AVEZ PERDU",1,(255,0,0))
  #  screen.blit(image_text,(320,400))
  #  pygame.display.flip()


  def update(self,screen):



    # police = pygame.font.SysFont("monospace", 30)
    # image_text= police.render(f"VOTRE ANCIEN SCORE EST {}",1,(0,0,0))
    # screen.blit(image_text,(150,30))

   # afficher le score a l'ecran
    score_text= self.font.render(f"score : {self.score}", 1, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    # appliquer l'image de mon joueur
    screen.blit(self.player.image, self.player.rect)

    # actualiser la barre de vie du joueur
    self.player.update_health_bar(screen)

    # actualiser la barre d'evenement du jeu
    self.comet_event.update_bar(screen)

    # actualiser l'animation du joueur
    self.player.update_animation()
    # recuperer les projectiles du joueur
    for projectile in self.player.all_projectiles:
      projectile.move()

    # recuperer les monstres du jeux
    for monster in self.all_monsters:
      monster.forward()
      monster.update_health_bar(screen)
      monster.update_animation()
     # recuperer les comets de notre jeu
    for comet in self.comet_event.all_comets:
       comet.fall()


    # appliquer l'ensemble des images de mon groupe de projectile et draw permet de dessiner
    self.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des images de mon groupe de monstre
    self.all_monsters.draw(screen)

      # appliquer l'ensemble des images de mon groupe de comettes
    self.comet_event.all_comets.draw(screen)

    # verifier si le joueur souhaite partir a gauche ou droite
    if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
      self.player.move_right()
    elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
      self.player.move_left()

  def check_collision(self, sprite, group):
     return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
   # fonction qui ajoute les monstres
  def spawn_monster(self, monster_class_name):
    self.all_monsters.add(monster_class_name.__call__(self))

