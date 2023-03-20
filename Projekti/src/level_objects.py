import pygame
import numpy as np
import math

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
        self.__max_speed = 3
        self._sprite = pygame.image.load("Projekti/src/sprites/player.png")
        
    def __str__(self):
        return f"[{int(self._pos[0])} {int(self._pos[1])}], [{int(self.__vel[0])} {int(self.__vel[1])}], [{int(self.__acc[0])} {int(self.__acc[1])}]"
        
    def move(self, force :tuple):
        self.__acc += np.asarray(force)
        
    def get_speed(self):
        return np.linalg.norm(self.__vel)
        
    def updateAndShow(self):
        #xsize and ysize placeholders. To be substituted by the max x and y of the screen
        xsize = 800
        ysize = 400
        #Not sure how to implement gravity. Here is one way
        #Friction also needs to be implemented. Maby in controll / collision dedection methods as those are dependent on if the player is on the ground or not. 
        '''
        gravity = 10
        self.move((0, gravity))      
        '''  
        #Adding acc to vel and setting acc to 0. bcs physics
        self.__vel += self.__acc
        self.__acc = np.array([0, 0])
        
        #Check if speed is greater than max speed. If it is setting it to max
        speed = self.get_speed()
        if speed > self.__max_speed: self.__vel = self.__vel / speed * self.__max_speed
        
        #if the character is trying to go off screen on the x axis. Set the x velocity to -x vel so it bounces of the sides. 
        new_pos = self._pos + self.__vel
        if new_pos[0] >= xsize or new_pos[0] < 0: 
            self.__vel = np.array([self.__vel[0] * -1, self.__vel[1]])
            new_pos = self._pos + self.__vel
            
        self._pos = new_pos
        
        
if __name__ == "__main__":
    p = platform((1, 2), 3)
    print(p)
    c = character((100, 200))
    print(c)