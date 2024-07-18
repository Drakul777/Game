import pygame.sprite
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        #generer le joueur
        self.player = Player(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self. all_monsters.add(monster)
