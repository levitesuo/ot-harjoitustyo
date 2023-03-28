from .sprited_object import SpritedObject
from .bounding_box import BoundingBox
from numpy import array as vector
import copy
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

        self.__max_speed = 50
        self._floor_box = BoundingBox(
            (self._pos[0], self.sprite.get_height() + self._pos[1]),
            (self.sprite.get_width(), -5),
        )

    def apply_force(self, force):
        force_vector = vector([force[0], force[1]])
        self.__acc += force_vector

    def get_falling_bounding_boxes(self):
        vel = self.__acc + self.__vel

        # Speed scaling could use its own method
        speed = np.linalg.norm(vel)
        if speed > self.__max_speed:
            self.vel = (
                vector([vel[0] / speed, vel[1] / speed])
                * self.__max_speed
            )
            speed = np.linalg.norm(vel)

        falling_boxes = []

        normalised_speed_vector = vel / speed
        iterative_speed_vector = normalised_speed_vector
        i = 1
        while np.linalg.norm(iterative_speed_vector) < speed:
            iterative_speed_vector = normalised_speed_vector * i
            i += 1
            pos = self._pos + iterative_speed_vector
            self._box.update((pos[0], pos[1] + self.sprite.get_height()))
            falling_boxes.append(copy.copy(self._box))
        return falling_boxes
    
    def collision_handler(self, collision):
        self.__vel -= vector([self.__vel[0] * collision[0], self.__vel[1] * collision[1]] )

    def __str__(self):
        return (
            super().__str__()
            + " "
            + f"[{int(self.__vel[0])} {int(self.__vel[1])}] [{int(self.__acc[0])} {int(self.__acc[1])}] {int(self.__max_speed)}"
        )
