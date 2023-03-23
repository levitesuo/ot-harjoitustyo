import unittest
from game_files.entities.game_object import GameObject


class TestGameObject(unittest.TestCase):
    def setUp(self):
        self.obj = GameObject((100, 100))

    def test_object_created(self):
        self.assertEqual(str(self.obj), "[100 100]")
