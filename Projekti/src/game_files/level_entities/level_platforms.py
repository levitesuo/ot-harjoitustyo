from ..entities.platform import Platform
import pygame


class LevelPlatforms:
    def __init__(self, list_of_platforms):
        # list_of_platforms contains a list of platforms
        # Where one platform is in the format ((x, y), width)
        self.__platforms = []
        list_of_platforms.sort(key=lambda plat: plat[0][1])
        for plat in list_of_platforms:
            if __name__ == "__main__":
                print(plat)
            self.__platforms.append(Platform(plat[0], plat[1]))

    def __str__(self):
        s = ""
        for i in range(len(self.__platforms)):
            s += str(self.__platforms[i])
            if i != len(self.__platforms) - 1:
                s += "\n"
        return s

    def check_for_collisions(self, other_box):
        hights_collision = None
        for plat in self.__platforms:
            if other_box.check_for_collision(plat._box):
                if hights_collision == None or hights_collision < plat._pos[1]:
                    hights_collision = plat._pos[1]
        if hights_collision: return hights_collision
        else: return False

    def draw(self, surface):
        for plat in self.__platforms:
            rect = plat._box.get_pos_and_offset()
            plat_middle_height = rect[1] + rect[3] / 2
            radius = rect[3] / 2
            color = (0, 0, 0)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.circle(surface, color, (rect[0], plat_middle_height), radius)
            pygame.draw.circle(
                surface, color, (rect[0] + rect[2], plat_middle_height), radius
            )
