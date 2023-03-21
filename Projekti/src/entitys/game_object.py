from numpy import array as vector

class Game_object:
    def __init__(self, pos):
        self._pos = vector([pos[0], pos[1]])
        
    def __str__(self):
        return f"[{self._pos[0]} {self._pos[1]}]"
    