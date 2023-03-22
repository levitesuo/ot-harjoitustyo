from numpy import array as vector

class Game_object:
    def __init__(self, pos):
        self._pos = vector([pos[0], pos[1]])
        
    def __str__(self):
        return f"[{int(self._pos[0])} {int(self._pos[1])}]"
    