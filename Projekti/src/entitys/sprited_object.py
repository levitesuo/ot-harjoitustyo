from .game_object import Game_object
import pygame

class Sprited_object(Game_object):
    def __init__(self, pos, sprite = None):
       super().__init__(pos) 
       self.__sprite_filelocation = sprite
       if sprite: self.__sprite = pygame.image.load(sprite)
       else: self.__sprite = None
       
    @property
    def sprite(self):
        if self.__sprite: return self.__sprite
        else: return pygame.image.load("./src/entitys/sprites/sprite_not_found.png")
        
    def __str__(self): 
        return super().__str__() + " " + str(self.__sprite_filelocation)