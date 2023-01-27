from enum import Enum
from dataclasses import dataclass
from levelup.character import Character
from levelup.map import GameMap

DEFAULT_CHARACTER_NAME = "Character"
ARBITRARY_INVALID_INITIALIZED_POSITION = (-1,-1,0)

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


# @dataclass
class GameStatus:
    running: bool = False
    current_position: tuple = ARBITRARY_INVALID_INITIALIZED_POSITION


class GameController:
    status: GameStatus
    character: Character = Character(DEFAULT_CHARACTER_NAME)
    game_map: GameMap

    def __init__(self):
        self.status = GameStatus()
        self.game_map = GameMap()

    def create_character(self, character_name: str) -> None:
        if not character_name:
            character_name = DEFAULT_CHARACTER_NAME
        self.character = Character(character_name)

    def move(self, direction: Direction) -> None:
        print(f"Moved {direction.name}")

    def set_character_position(self,xycoordinates: tuple) -> None:
        print(f"Set Character position state for testing")
        self.character(xycoordinates)        

