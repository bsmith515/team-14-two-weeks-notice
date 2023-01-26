from enum import Enum

class direction(Enum):
    EAST = "e"
    WEST = "w"
    NORTH = "n"
    SOUTH = "s"

class GameMap:
    def get_total_positions(self):
        return 100

