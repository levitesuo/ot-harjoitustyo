from numpy import array as vector


class Bounding_Box:
    def __init__(self, pos, bottom_rigth_offset):
        self.__pos = vector([pos[0], pos[1]])
        self.__offset = vector([bottom_rigth_offset[0], bottom_rigth_offset[1]])

    def update(self, new_pos):
        self.__pos = vector([new_pos[0], new_pos[1]])

    def get_corners(self):
        return list(self.__pos) + list(self.__offset + self.__pos)

    def get_pos_and_offset(self):
        return list(self.__pos) + list(self.__offset)

    def check_for_collision(self, other):
        minx1, miny1, maxx1, maxy1 = self.get_corners()
        minx2, miny2, maxx2, maxy2 = other.get_corners()
        if maxx1 >= minx2 and maxx2 >= minx1 and maxy1 >= miny2 and maxy2 >= miny1:
            return True
        else:
            return False

    def __str__(self):
        minx, miny, maxx, maxy = self.get_corners()
        return f"[{minx} {miny} {maxx} {maxy}]"
