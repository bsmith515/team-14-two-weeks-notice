from dataclasses import dataclass
from levelup.position import Position
from levelup.map import GameMap

DEFAULT_POSITION = Position(0, 0)
DEFAULT_CHARACTER_NAME = "Bubba"

@dataclass
class Character:
    name: str
    current_position: Position()
    testmap: GameMap()
    
    def __init__(self, name=DEFAULT_CHARACTER_NAME):
        self.name = name
        

    def getName(self):
        return self.name

    def enterMap(self, map):
        self.testmap = map
        self.current_position = DEFAULT_POSITION



        


