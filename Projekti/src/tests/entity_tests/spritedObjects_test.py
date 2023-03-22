import unittest
from entitys import Sprited_object

class TestSrited_boject(unittest.TestCase):
    def setUp(self):
        self.obj = Sprited_object((100, 100), "./src/entitys/sprites/player.png")
    
    def test_object_created(self):
        self.assertEqual(str(self.obj), "[100 100] ./src/entitys/sprites/player.png")

    def test_object_created_if_path_to_file_was_null(self):
        obj = Sprited_object((100, 100))
        self.assertEqual(str(obj), "[100 100] None")

    def test_object_get_sprite(self):
        self.assertEqual(str(self.obj.sprite),"<Surface(32x40x8 SW)>")

    def test_object_get_sprite_when_sprite_is_null(self):
        obj = Sprited_object((100, 100))
        self.assertEqual(str(obj.sprite),"<Surface(80x80x32 SW)>")