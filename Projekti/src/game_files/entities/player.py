from .sprited_object import SpritedObject
from .bounding_box import BoundingBox
from numpy import array as vector
import numpy as np
import os


class Player(SpritedObject):
    def __init__(self, pos, sprite=None):
        if not sprite:
            dirname = os.path.dirname(__file__)
            sprite = os.path.join(dirname, "sprites/player.png")
        super().__init__(pos, sprite)
        self.__vel = vector([0, 0])
        self.__acc = vector([0, 0])

        self.__max_speed = 5
        self._floor_box = BoundingBox(
            (self._pos[0], self.sprite.get_height() + self._pos[1]),
            (self.sprite.get_width(), -5),
        )

    def apply_force(self, force):
        force_vector = vector([force[0], force[1]])
        self.__acc += force_vector

    def on_the_floor(self):
        self.__acc[1] = 0
        if self.__vel[1] >= 0:
            self.__vel = vector([self.__vel[0] * 0.5, 0])

    def update(self):
        self.__vel += self.__acc
        self.__acc = vector([0, 0])

        # Speed scaling could use its own method
        speed = np.linalg.norm(self.__vel)
        if speed > self.__max_speed:
            self.__vel = (
                vector([self.__vel[0] / speed, self.__vel[1] / speed])
                * self.__max_speed
            )

        self._pos = vector([self._pos[0] + self.__vel[0], self._pos[1] + self.__vel[1]])
        self._box.update(self._pos)
        self._floor_box.update((self._pos[0], self.sprite.get_height() + self._pos[1]))

    def __str__(self):
        return (
            super().__str__()
            + " "
            + f"[{int(self.__vel[0])} {int(self.__vel[1])}] [{int(self.__acc[0])} {int(self.__acc[1])}] {int(self.__max_speed)}"
        )
