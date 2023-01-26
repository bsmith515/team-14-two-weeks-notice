from unittest import TestCase
from levelup.character import Character, DEFAULT_POSITION

class TestCharacter(TestCase):
    def test_init(self):
        fake_name = "Balthazar"
        test_character = Character(fake_name)
        self.assertEqual(test_character.name, fake_name)
        self.assertEqual(test_character.current_position, DEFAULT_POSITION)



 
    
        
