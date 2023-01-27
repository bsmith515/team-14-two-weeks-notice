from enum import Enum
from levelup.position import Position

class Direction(Enum):
    EAST = "e"
    WEST = "w"
    NORTH = "n"
    SOUTH = "s"

class GameMap:

    position_list: list 
    num_positions: int
    starting_position: int

    def __init__(self):
        self.position_list = []
        for x in range(0, 10):
            for y in range(0, 10):
                self.position_list.append(Position(x, y))
        self.num_positions = len(self.position_list)
        self.starting_position = Position(0,0)
                    
    def get_total_positions(self) -> int:
        return self.num_positions

    def get_positions(self):
        return self.position_list         

    def calculate_position(self, starting_position: Position, direction: Direction) -> Position:
        x_starting_pos = starting_position.coordinates[0]    
        y_starting_pos = starting_position.coordinates[1]

        if(direction == Direction.NORTH):
            return_position = Position(x_starting_pos, y_starting_pos+1)
        elif(direction == Direction.SOUTH):
            return_position = Position(x_starting_pos, y_starting_pos-1)
        elif(direction == Direction.EAST):
            return_position = Position(x_starting_pos+1, y_starting_pos)
        elif(direction == Direction.WEST):
            return_position = Position(x_starting_pos-1, y_starting_pos)         

        return return_position

    def is_position_valid(self, pos_to_validate: Position) -> bool:
        return pos_to_validate in self.position_list
