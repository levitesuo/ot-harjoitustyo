from numpy import array as vector
from .bounding_box import BoundingBox


class GameObject:
    def __init__(self, pos, bounding_box_offset=None):
        if not bounding_box_offset:
            bounding_box_offset = pos
        self._pos = vector([pos[0], pos[1]])
        self._box = BoundingBox(self._pos, bounding_box_offset)

    def __str__(self):
        return f"[{int(self._pos[0])} {int(self._pos[1])}]"
