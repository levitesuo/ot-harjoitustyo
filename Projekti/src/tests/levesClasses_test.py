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
    
    def test_move_method(self):
        self.play.move((20, 10))
        self.assertEqual(str(self.play), "[100 200], [0 0], [20 10]")
        
    def test_updateAndShow_method_with_no_special_case(self):
        self.play.move((20, 10))
        self.play.updateAndShow()
        self.assertEqual(str(self.play), "[120 210], [20 10], [0 0]")
        
    def test_updateAndShow_method_with_x_out_of_bounds_neg(self):
        play = level_objects.player((0, 0))
        play.move((-10, 10))
        play.updateAndShow()
        self.assertEqual(str(play), "[10 10], [10 10], [0 0]")
        
    def test_updateAndShow_method_with_x_out_of_bounds_pos(self):
        #max x size = 400
        play = level_objects.player((399, 0))
        play.move((10, 10))
        play.updateAndShow()
        self.assertEqual(str(play), "[389 10], [-10 10], [0 0]")
        
    def test_updateAndShow_method_maxspeed_exeeded(self):
        self.play.move((1000, 1000))
        self.play.updateAndShow()
        self.assertEqual(str(self.play), "[170 270], [70 70], [0 0]")