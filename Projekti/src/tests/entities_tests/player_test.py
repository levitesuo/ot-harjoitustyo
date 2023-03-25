import unittest
from game_files.entities.player import Player

<<<<<<< HEAD
=======

>>>>>>> ce519ab322ba6a6a628bbe3fb19ee525116e4964
class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player((10, 40), "./src/game_files/entities/sprites/player.png")

    def test_player_creation(self):
<<<<<<< HEAD
        self.assertEqual(str(self.player), "[10 40] ./src/game_files/entities/sprites/player.png [0 0] [0 0] 5")

    def test_force_applied_to_player(self):
        self.player.apply_force((10, 0))
        self.assertEqual(str(self.player), "[10 40] ./src/game_files/entities/sprites/player.png [0 0] [10 0] 5")
=======
        self.assertEqual(
            str(self.player),
            "[10 40] ./src/game_files/entities/sprites/player.png [0 0] [0 0] 5",
        )

    def test_force_applied_to_player(self):
        self.player.apply_force((10, 0))
        self.assertEqual(
            str(self.player),
            "[10 40] ./src/game_files/entities/sprites/player.png [0 0] [10 0] 5",
        )
>>>>>>> ce519ab322ba6a6a628bbe3fb19ee525116e4964

    def test_force_to_vel_not_exeeding_maxSpeed(self):
        self.player.apply_force((1, -1))
        self.player.update()
<<<<<<< HEAD
        self.assertEqual(str(self.player), "[11 39] ./src/game_files/entities/sprites/player.png [1 -1] [0 0] 5")
=======
        self.assertEqual(
            str(self.player),
            "[11 39] ./src/game_files/entities/sprites/player.png [1 -1] [0 0] 5",
        )
>>>>>>> ce519ab322ba6a6a628bbe3fb19ee525116e4964

    def test_force_to_vel_exeeding_maxSpeed(self):
        self.player.apply_force((300, 400))
        self.player.update()
<<<<<<< HEAD
        self.assertEqual(str(self.player), "[13 44] ./src/game_files/entities/sprites/player.png [3 4] [0 0] 5")
=======
        self.assertEqual(
            str(self.player),
            "[13 44] ./src/game_files/entities/sprites/player.png [3 4] [0 0] 5",
        )
>>>>>>> ce519ab322ba6a6a628bbe3fb19ee525116e4964
