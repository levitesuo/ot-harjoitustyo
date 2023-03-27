import unittest
from game_files.level_entities.level_platforms import LevelPlatforms
from game_files.entities.player import Player


class TestLevelPlatforms(unittest.TestCase):
    def setUp(self):
        self.platforms = LevelPlatforms([((10, 10), 30), ((20, 20), 40)])

    def test_platforms_created(self):
        self.assertEqual(
            str(self.platforms), "[10 10] [10 10 40 20]\n[20 20] [20 20 60 30]"
        )

    def test_platform_collision(self):
        player = Player((10, 10), "./src/game_files/entities/sprites/player.png")
        collision = self.platforms.check_for_collisions(player._box)
        self.assertEqual(str(collision), "[  0 -20]")

    def test_platform_collision_false(self):
        player = Player((100, 100), "./src/game_files/entities/sprites/player.png")
        collision = self.platforms.check_for_collisions(player._box)
        self.assertEqual(str(collision), "[0 0]")
