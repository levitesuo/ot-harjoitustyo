from .sprited_object import Sprited_object
from numpy import array as vector
import numpy as np

class Player(Sprited_object):
    def __init__(self, pos, sprite = None):
        super().__init__(pos, sprite)
        self.__vel = vector([0, 0])
        self.__acc = vector([0, 0])

        self.__max_speed = 5

    def apply_force(self, force):
        force_vector = vector([force[0], force[1]])
        self.__acc += force_vector
    
    def update(self):
        self.__vel += self.__acc
        self.__acc = vector([0, 0])

        #Speed scaling could use its own method
        speed = np.linalg.norm(self.__vel) 
        if speed > self.__max_speed: 
            self.__vel = vector([self.__vel[0] / speed, self.__vel[1] / speed]) * self.__max_speed

        self._pos = vector([self._pos[0] + self.__vel[0], self._pos[1] + self.__vel[1]])

    def __str__(self):
        return super().__str__()+ " " + f"[{int(self.__vel[0])} {int(self.__vel[1])}] [{int(self.__acc[0])} {int(self.__acc[1])}] {int(self.__max_speed)}"
        #player = Player((0, 0), "./src/game_files/entitys/sprites/sprite_not_found.png")