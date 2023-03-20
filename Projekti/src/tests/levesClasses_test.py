import unittest
import level_objects

class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = level_objects.platform((100, 200), 10)
    
    def test_platform_init(self):
        self.assertEqual(str(self.platform), "[100 200], 10")
        
class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.char = level_objects.character((100, 200))
    
    def test_character_init(self):
        self.assertEqual(str(self.char), "[100 200]")
        
class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.play = level_objects.player((100, 200))
    
    def test_character_init(self):
        self.assertEqual(str(self.play), "[100 200], [0 0], [0 0]")