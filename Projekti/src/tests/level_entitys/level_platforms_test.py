import unittest
from game_files.level_entitys.level_platforms import Level_Platforms

class TestLevel_Platforms(unittest.TestCase):
    def setUp(self):
        self.platforms = Level_Platforms([((10, 10), 30),((20, 20), 40)])
    
    def test_platforms_created(self):
        self.assertEqual(str(self.platforms), "[10 10] 30\n[20 20] 40")
                                         
