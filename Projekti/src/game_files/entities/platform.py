from .game_object import GameObject
from .bounding_box import Bounding_Box


class Platform(GameObject):
    def __init__(self, pos, width):
        self._width = width
        self._height = 10
        super().__init__(pos, (self._width, self._height))

    def __str__(self):
        return super().__str__() + " " + str(self._box)
