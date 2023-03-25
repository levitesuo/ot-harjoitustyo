import unittest
from game_files.entities.sprited_object import SpritedObject


class TestSritedObject(unittest.TestCase):
    def setUp(self):
        self.obj = SpritedObject(
            (100, 100), "./src/game_files/entities/sprites/player.png"
        )

    def test_object_created(self):
        self.assertEqual(
            str(self.obj), "[100 100] ./src/game_files/entities/sprites/player.png"
        )

    def test_object_created_if_path_to_file_was_null(self):
        obj = SpritedObject((100, 100))
        self.assertEqual(
            str(obj), "[100 100] ./src/game_files/entities/sprites/sprite_not_found.png"
        )

    def test_object_get_sprite(self):
        self.assertEqual(str(self.obj.sprite), "<Surface(32x40x8 SW)>")

    def test_object_get_sprite_when_sprite_is_null(self):
        obj = SpritedObject((100, 100))
        self.assertEqual(str(obj.sprite), "<Surface(80x80x32 SW)>")
