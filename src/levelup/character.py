from dataclasses import dataclass
from levelup.position import Position

DEFAULT_POSITION = Position(0, 0)

@dataclass
class Character:
    name: str
    current_position: Position
    
    def __init__(self, name):
        self.name = name
        self.current_position = DEFAULT_POSITION

