from numpy import array as vector
from .bounding_box import Bounding_Box


class Game_object:
    def __init__(self, pos, Bounding_Box_offset=None):
        if not Bounding_Box_offset:
            Bounding_Box_offset = pos
        self._pos = vector([pos[0], pos[1]])
        self._box = Bounding_Box(self._pos, Bounding_Box_offset)

    def __str__(self):
        return f"[{int(self._pos[0])} {int(self._pos[1])}]"
