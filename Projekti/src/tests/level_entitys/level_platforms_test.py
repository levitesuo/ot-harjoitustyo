import unittest
from game_files.level_entitys.level_platforms import Level_Platforms
from game_files.entitys.player import Player

class TestLevel_Platforms(unittest.TestCase):
    def setUp(self):
        self.platforms = Level_Platforms([((10, 10), 30),((20, 20), 40)])
    
    def test_platforms_created(self):
        self.assertEqual(str(self.platforms), "[10 10] [10 10 40 20]\n[20 20] [20 20 60 30]")
                                         
    def test_platform_collision(self):
        player = Player((10, 10), "./src/game_files/entitys/sprites/player.png")
        collision = self.platforms.check_for_collisions(player)
        self.assertEqual(str(collision), "True")

    def test_platform_collision_false(self):
        player = Player((100, 100), "./src/game_files/entitys/sprites/player.png")
        collision = self.platforms.check_for_collisions(player)
        self.assertEqual(str(collision), "False")