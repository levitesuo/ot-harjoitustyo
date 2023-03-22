from ..entitys.platform import Platform

class Level_Platforms:
    def __init__(self, list_of_platforms):
        #list_of_platforms contains a list of platforms
        #Where one platform is in the format ((x, y), width)
        self.__platforms = []
        list_of_platforms.sort(key = lambda plat: plat[0][1])
        for plat in list_of_platforms: 
            if __name__ == "__main__": print(plat)
            self.__platforms.append(Platform(plat[0], plat[1]))

    def __str__(self):
        s = ""
        for i in range(len(self.__platforms)):
            s += str(self.__platforms[i])
            if i != len(self.__platforms) - 1: s += "\n"
        return s
    
    def check_for_collisions(self, other):
        other_Box = other._box
        for plat in self.__platforms:
            if other_Box.check_for_collision(plat._box): return True
        return False
