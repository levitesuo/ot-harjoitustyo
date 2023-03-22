from .game_object import Game_object
from .bounding_box import Bounding_Box
        
class Platform(Game_object):
    def __init__(self, pos, width):
        super().__init__(pos)
        self._width = width
        self._height = 10
        self._box = Bounding_Box(self._pos, (self._width, self._height))

    def __str__(self):
        return super().__str__ ()+ " " + str(self._box)