import unittest
from game_files.entities.game_object import Game_object

class TestGame_object(unittest.TestCase):
    def setUp(self):
        self.obj = Game_object((100, 100))
        
    def test_object_created(self):
        self.assertEqual(str(self.obj), "[100 100]")