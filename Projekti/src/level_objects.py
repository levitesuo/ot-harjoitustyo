import pygame
import numpy as np

class platform:
    def __init__(self, pos :tuple, width):
        self.pos = np.asarray(pos)
        self.width = width
    
    def __str__(self):
        return f"{self.pos}, {self.width}"
        
class character:
    def __init__(self, pos: tuple): #ToDo include sprite variation
        self._pos = np.asarray(pos)
        #We use nparrays as vectors to represent positions etc.
    
    def show(sprite, color, luminosity):
        pass
    def __str__(self):
        return f"{self._pos}"

class player(character):
    def __init__(self, pos: tuple):
        super().__init__(pos)
        self.__acc = np.array([0, 0])
        self.__vel = np.array([0, 0])
        #Player has position, velocity, acceleration and max_speed
        self.__max_speed = 1
        
    def __str__(self):
        return f"{self._pos}, {self.__vel}, {self.__acc}"
        
        
if __name__ == "__main__":
    p = platform((1, 2), 3)
    print(p)
    c = character((100, 200))
    print(c)