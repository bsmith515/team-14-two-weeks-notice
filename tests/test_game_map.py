from unittest import TestCase
from levelup.map import GameMap
from levelup.map import Direction
from levelup.position import Position

class TestGameMap(TestCase):
    def test_get_total_positions(self):
        test_gamemap = GameMap()
        self.assertEqual(100, test_gamemap.get_total_positions())

    def test_get_positions(self):
        test_gamemap = GameMap()
        self.assertEqual(100, len(test_gamemap.get_positions()))

    def test_calculate_position_mid_go_north(self):
        test_gamemap = GameMap()
        starting_position = Position(5,5)
        expected_position = Position(5,6)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.NORTH))

    def test_calculate_position_mid_go_south(self):
        test_gamemap = GameMap()
        starting_position = Position(5,5)
        expected_position = Position(5,4)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.SOUTH))

    def test_calculate_position_mid_go_east(self):
        test_gamemap = GameMap()
        starting_position = Position(5,5)
        expected_position = Position(6,5)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.EAST))

    def test_calculate_position_mid_go_west(self):
        test_gamemap = GameMap()
        starting_position = Position(5,5)
        expected_position = Position(4,5)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.WEST))

    def test_calculate_position_lower_left_go_west(self):
        test_gamemap = GameMap()
        starting_position = Position(0,0)
        expected_position = Position(0,0)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.WEST))

    def test_calculate_position_lower_left_go_south(self):
        test_gamemap = GameMap()
        starting_position = Position(0,0)
        expected_position = Position(0,0)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.SOUTH))

    def test_calculate_position_upper_right_go_north(self):
        test_gamemap = GameMap()
        starting_position = Position(9,9)
        expected_position = Position(9,9)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.NORTH))

    def test_calculate_position_upper_right_go_east(self):
        test_gamemap = GameMap()
        starting_position = Position(9,9)
        expected_position = Position(9,9)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.EAST))

    def test_calculate_position_upper_mid_go_north(self):
        test_gamemap = GameMap()
        starting_position = Position(5,9)
        expected_position = Position(5,9)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.NORTH))

    def test_calculate_position_lower_mid_go_south(self):
        test_gamemap = GameMap()
        starting_position = Position(5,0)
        expected_position = Position(5,0)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.SOUTH))

    def test_calculate_position_left_mid_go_west(self):
        test_gamemap = GameMap()
        starting_position = Position(0,5)
        expected_position = Position(0,5)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.WEST))

    def test_calculate_position_right_mid_go_east(self):
        test_gamemap = GameMap()
        starting_position = Position(9,5)
        expected_position = Position(9,5)
        self.assertEqual(expected_position, test_gamemap.calculate_position(starting_position, Direction.EAST))

    def test_is_position_valid(self):
        test_gamemap = GameMap()
        valid_position = Position(5,5)
        self.assertTrue(test_gamemap.is_position_valid(valid_position))

    def test_get_starting_position(self):
        test_gamemap = GameMap()
        expected_starting_position = Position(0,0)
        self.assertEqual(expected_starting_position, test_gamemap.get_starting_position())