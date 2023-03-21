import unittest
import entitys

class TestGame_object(unittest.TestCase):
    def setUp(self):
        self.obj = game_object((100, 100))
        
    def test_object_created(self):
        self.assertEqual(str(self.obj), "[100 100]")