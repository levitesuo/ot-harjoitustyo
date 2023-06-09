from .game_object import GameObject
from .bounding_box import BoundingBox
import pygame


class SpritedObject(GameObject):
    def __init__(
        self, pos, sprite="./src/game_files/entities/sprites/sprite_not_found.png"
    ):
        self.__sprite = pygame.image.load(sprite)
        super().__init__(pos, (self.__sprite.get_width(), self.__sprite.get_height()))
        self.__sprite_filelocation = sprite

    @property
    def sprite(self):
        return self.__sprite

    def __str__(self):
        return super().__str__() + " " + str(self.__sprite_filelocation)
