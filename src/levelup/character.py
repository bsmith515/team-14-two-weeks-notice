from dataclasses import dataclass
from position import Position

DEFAULT_POSITION = Position(0, 0)

@dataclass
class Character:
    name: str
