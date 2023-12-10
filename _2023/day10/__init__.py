from enum import Enum
from dataclasses import dataclass

Position = tuple[int, int]


class Tile(Enum):
    NORTH_SOUTH = "|"
    EAST_WEST = "-"
    NORTH_EAST = "L"
    NORTH_WEST = "J"
    SOUTH_WEST = "7"
    SOUTH_EAST = "F"
    GROUND = "."
    STARTING_POSITION = "S"

    def get_connected_positions(
        self, tile_position: Position
    ) -> set[Position]:
        x, y = tile_position
        connected_positions = set()
        connected_position_computation = (
            CONNECTED_POSITION_COMPUTATION_MAPPING[self]
        )
        for (x_diff, y_diff) in connected_position_computation:
            connected_position = (x + x_diff, y + y_diff)
            connected_positions.add(connected_position)

        return connected_positions

    def is_connected_to(
        self, position: Position, other: "Tile", other_position: Position
    ) -> bool:
        self_connected_to = self.get_connected_positions(position)
        print(f"{self_connected_to=}", other_position)
        if other_position not in self_connected_to:
            return False

        other_connected_to = other.get_connected_positions(other_position)
        print(f"{other_connected_to=}", position)
        if position not in other_connected_to:
            return False

        return True


NORTH_DIFF = (0, -1)
SOUTH_DIFF = (0, 1)
EAST_DIFF = (1, 0)
WEST_DIFF = (-1, 0)

CONNECTED_POSITION_COMPUTATION_MAPPING = {
    Tile.NORTH_SOUTH: [NORTH_DIFF, SOUTH_DIFF],
    Tile.EAST_WEST: [EAST_DIFF, WEST_DIFF],
    Tile.NORTH_EAST: [NORTH_DIFF, EAST_DIFF],
    Tile.NORTH_WEST: [NORTH_DIFF, WEST_DIFF],
    Tile.SOUTH_WEST: [SOUTH_DIFF, WEST_DIFF],
    Tile.SOUTH_EAST: [SOUTH_DIFF, EAST_DIFF],
    Tile.GROUND: [],
    Tile.STARTING_POSITION: [],
}


@dataclass
class Map:
    tiles: list[list[Tile]]

    @classmethod
    def from_input(cls, data: str) -> "Map":
        tiles = []
        for input_line in data.splitlines():
            tile_line = [Tile(character) for character in input_line]
            tiles.append(tile_line)
        return Map(tiles=tiles)

    def to_str(self):
        output_lines = []
        for tile_line in self.tiles:
            output_line = "".join([tile.value for tile in tile_line])
            output_lines.append(output_line)
        return "\n".join(output_lines)

    def get_starting_position(self) -> Position:
        for y, tile_line in enumerate(self.tiles):
            for x, tile in enumerate(tile_line):
                if tile == Tile.STARTING_POSITION:
                    return x, y
