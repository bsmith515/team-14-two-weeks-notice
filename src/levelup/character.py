from dataclasses import dataclass
from levelup.position import Position

DEFAULT_POSITION = Position(0, 0)
DEFAULT_CHARACTER_NAME = "Bubba"

@dataclass
class Character:
    name: str
    current_position: Position
    
    def __init__(self, name=DEFAULT_CHARACTER_NAME):
        self.name = name
        self.current_position = DEFAULT_POSITION

    def getName(self):
        return self.name


