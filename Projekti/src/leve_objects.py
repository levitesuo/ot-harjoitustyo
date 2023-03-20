import numpy as np
class game_object:
    def __init__(self, pos):
        self.pos = np.array([pos[0], pos[1]])
        
    def __str__(self):
        return f"[{self.pos[0]} {self.pos[1]}]"

class platform(game_object):
    def __init__(self, pos, width):
        super().__init__(pos)
        self.width = width
    
    def __str__(self):
        return super().__str__ ()+ " " + str(self.width)
    

if __name__ == "__main__":
    p = platform((10, 10), 100)
    print(p)