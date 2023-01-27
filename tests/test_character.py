from unittest import TestCase
from levelup.character import Character, DEFAULT_POSITION, DEFAULT_CHARACTER_NAME
from levelup.map import GameMap, Direction
from levelup.position import Position

class TestGameMap(GameMap):
    def __init__(self):
        GameMap.__init__(self)
    def get_starting_position(self):
        return Position(0,0)

class TestCharacter(TestCase):
    def test_init_given_name(self):
        fake_name = "Balthazar"
        test_character = Character(fake_name)
        self.assertEqual(test_character.name, fake_name)
 
    def test_init_given_no_name(self):
        test_character = Character()
        self.assertEqual(test_character.name, DEFAULT_CHARACTER_NAME)
 
    def test_get_name(self):
        fake_name = "Tiny"
        test_character = Character(fake_name)
        test_name = test_character.getName()
        self.assertEqual(test_name, fake_name)

    def test_enter_map(self):
       test_character = Character()
       test_game_map = TestGameMap()
       test_character.enterMap(test_game_map)

       self.assertIsNotNone(test_character.current_position)

    def test_get_position(self):
        test_character = Character()
        test_game_map = TestGameMap()
        test_character.enterMap(test_game_map)
        self.assertEqual(test_character.getPosition(), DEFAULT_POSITION)

    def test_move(self):
        test_character = Character()
        test_game_map = TestGameMap()
        test_character.enterMap(test_game_map)
        cPos = test_character.getPosition()
        test_character.move(Direction.EAST)
        nPos = test_character.getPosition()       
        self.assertNotEqual(cPos, nPos)

