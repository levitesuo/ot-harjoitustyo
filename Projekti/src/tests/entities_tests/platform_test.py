import unittest
from game_files.entities.platform import Platform


class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = Platform((100, 100), 50)

    def test_Platform_creation(self):
        self.assertEqual(str(self.platform), "[100 100] [100 100 150 110]")
