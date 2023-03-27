import unittest
from game_files.entities.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player((10, 40), "./src/game_files/entities/sprites/player.png")
        self.max_speed = 50

    def test_player_creation(self):
        self.assertEqual(
            str(self.player),
            f"[10 40] ./src/game_files/entities/sprites/player.png [0 0] [0 0] {self.max_speed}",
        )

    def test_force_applied_to_player(self):
        self.player.apply_force((10, 0))
        self.assertEqual(
            str(self.player),
            f"[10 40] ./src/game_files/entities/sprites/player.png [0 0] [10 0] {self.max_speed}",
        )

    def test_falling_bounding_boxes_correct(self):
        self.player.apply_force((5, 0))
        boxes = self.player.get_falling_bounding_boxes()
        s = ""
        for i in range(len(boxes)):
            s += str(boxes[i])
            if i != len(boxes) - 1:
                s += "\n"
        self.assertEqual(
            s,
            "[11.0 80.0 43.0 120.0]\n[12.0 80.0 44.0 120.0]\n[13.0 80.0 45.0 120.0]\n[14.0 80.0 46.0 120.0]\n[15.0 80.0 47.0 120.0]",
        )
