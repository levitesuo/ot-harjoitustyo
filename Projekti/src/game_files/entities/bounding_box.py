from numpy import array as vector


class BoundingBox:
    def __init__(self, pos, bottom_rigth_offset):
        self._pos = vector([pos[0], pos[1]])
        self.__offset = vector([bottom_rigth_offset[0], bottom_rigth_offset[1]])

    def update(self, new_pos):
        self._pos = vector([new_pos[0], new_pos[1]])

    def get_corners(self):
        return list(self._pos) + list(self.__offset + self._pos)

    def get_pos_and_offset(self):
        return list(self._pos) + list(self.__offset)

    def check_for_collision(self, other):
        minx1, miny1, maxx1, maxy1 = self.get_corners()
        minx2, miny2, maxx2, maxy2 = other.get_corners()
        
        if maxx1 >= minx2 and maxx2 >= minx1 and maxy1 >= miny2 and maxy2 >= miny1:
            # Calculate the direction vector from box1 to box2
            dx = min(maxx1, maxx2) - max(minx1, minx2)
            dy = min(maxy1, maxy2) - max(miny1, miny2)
            
            # Check which direction box2 is relative to box1
            if dx < dy:
                if maxx1 < maxx2:
                    return vector([dx, 0])  # box2 is to the right of box1
                else:
                    return vector([-dx, 0])  # box2 is to the left of box1
            else:
                if maxy1 < maxy2:
                    return vector([0, dy])  # box2 is below box1
                else:
                    return vector([0, -dy])  # box2 is above box1
        
        else:
            return vector([0, 0])

    def __str__(self):
        minx, miny, maxx, maxy = self.get_corners()
        return f"[{minx} {miny} {maxx} {maxy}]"
