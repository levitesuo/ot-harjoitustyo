from game_object import Game_object
        
class platform(Game_object):
    def __init__(self, pos, width):
        super().__init__(pos)
        self._width = width
        self._height = 10
        
    def __str__(self):
        return super().__str__ ()+ " " + str(self.width)
    
if __name__ == "__main__":
    p = platform((10, 10), 100)
    print(p)