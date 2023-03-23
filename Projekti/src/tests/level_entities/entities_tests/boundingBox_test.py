import unittest
from game_files.entities.bounding_box import Bounding_Box

class TestBounding_Box(unittest.TestCase):
    def setUp(self):
        self.box = Bounding_Box((10, 40), (100, 100))

    def test_box_creation(self):
        self.assertEqual(str(self.box), "[10 40 110 140]")

    def test_box_update(self):
        self.box.update((0, 0))
        self.assertEqual(str(self.box), "[0 0 100 100]")

    def test_box_collision_true(self):
        other_box = Bounding_Box((20, 0), (10, 400))
        collision = self.box.check_for_collision(other_box)
        self.assertEqual(str(collision), "True")
    
    def test_box_collision_false(self):
        other_box = Bounding_Box((2000, 10000), (10, 400))
        collision = self.box.check_for_collision(other_box)
        self.assertEqual(str(collision), "False")