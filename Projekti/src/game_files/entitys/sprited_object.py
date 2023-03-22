from .game_object import Game_object
from .bounding_box import Bounding_Box
import pygame

class Sprited_object(Game_object):
    def __init__(self, pos, sprite = "./src/game_files/entitys/sprites/sprite_not_found.png"):
        super().__init__(pos) 
        self.__sprite_filelocation = sprite
        self.__sprite = pygame.image.load(sprite)
        self._box = Bounding_Box(self._pos, (self.__sprite.get_width(), self.__sprite.get_height()))

       
    @property
    def sprite(self):
        return self.__sprite
        
    def __str__(self): 
        return super().__str__() + " " + str(self.__sprite_filelocation)