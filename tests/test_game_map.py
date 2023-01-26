from unittest import TestCase
from levelup.map import GameMap

class TestGameMap(TestCase):
    def test_get_total_positions(self):
        test_gamemap = GameMap()
        self.assertEqual(100, test_gamemap.get_total_positions())