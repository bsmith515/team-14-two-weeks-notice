from dataclasses import dataclass
from levelup.position import Position
from levelup.map import GameMap

DEFAULT_POSITION = Position(0, 0)
DEFAULT_CHARACTER_NAME = "Bubba"

@dataclass
class Character:
    name: str
    current_position: Position
    gameMap: GameMap
    
    def __init__(self, name=DEFAULT_CHARACTER_NAME):
        self.name = name
        

    def getName(self):
        return self.name

    def getPosition(self):
        return self.current_position
        
    def enterMap(self, map):
        self.gameMap = map
        self.current_position = self.gameMap.get_starting_position()

