import unittest
from game_files.entities.bounding_box import BoundingBox


class TestBoundingBox(unittest.TestCase):
    def setUp(self):
        self.box = BoundingBox((10, 40), (100, 100))

    def test_box_creation(self):
        self.assertEqual(str(self.box), "[10 40 110 140]")

    def test_box_update(self):
        self.box.update((0, 0))
        self.assertEqual(str(self.box), "[0 0 100 100]")

    def test_box_collision_true(self):
        box1 = BoundingBox((0, 0), (2, 1))
        box2 = BoundingBox((1, 0), (2, 1))
        collision = box1.check_for_collision(box2)
        self.assertEqual(str(collision), "[ 0 -1]")

    def test_box_collision_false(self):
        other_box = BoundingBox((2000, 10000), (10, 400))
        collision = self.box.check_for_collision(other_box)
        self.assertEqual(str(collision), "[0 0]")
