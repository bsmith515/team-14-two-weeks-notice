from unittest import TestCase
from levelup.character import Character, DEFAULT_POSITION, DEFAULT_CHARACTER_NAME
from levelup.map import GameMap

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
       test_game_map = GameMap()
       test_character.enterMap(test_game_map)

       self.assertIsNotNone(test_character.current_position)

    def test_get_position(self):
        test_character = Character()
        test_game_map = GameMap()
        test_character.enterMap(test_game_map)
        self.assertEqual(test_character.getPostion(), DEFAULT_POSITION)





 
    
        
