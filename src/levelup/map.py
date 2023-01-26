from enum import Enum
from levelup.position import Position
from levelup.controller import Direction

class direction(Enum):
    EAST = "e"
    WEST = "w"
    NORTH = "n"
    SOUTH = "s"

class GameMap:

    position_list: list 
    num_positions: int

    def __init__(self):
        self.position_list = []
        for x in range(0, 10):
            for y in range(0, 10):
                self.position_list.append(Position(x, y))
        self.num_positions = len(self.position_list)
                    
    def get_total_positions(self):
        return self.num_positions

    def get_positions(self):
        return self.position_list         

    def calculate_position(self, starting_position: Position, direction: Direction):
        print(starting_position)
        return Position(5,6)

    def is_position_valid(self, pos_to_validate: Position):
        return pos_to_validate in self.position_list
