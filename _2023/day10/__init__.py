from enum import Enum
from dataclasses import dataclass

Position = tuple[int, int]


class TileType(Enum):
    NORTH_SOUTH = "|"
    EAST_WEST = "-"
    NORTH_EAST = "L"
    NORTH_WEST = "J"
    SOUTH_WEST = "7"
    SOUTH_EAST = "F"
    GROUND = "."
    STARTING_POSITION = "S"


NORTH_DIFF = (0, -1)
SOUTH_DIFF = (0, 1)
EAST_DIFF = (1, 0)
WEST_DIFF = (-1, 0)

CONNECTED_POSITION_COMPUTATION_MAPPING = {
    TileType.NORTH_SOUTH: [NORTH_DIFF, SOUTH_DIFF],
    TileType.EAST_WEST: [EAST_DIFF, WEST_DIFF],
    TileType.NORTH_EAST: [NORTH_DIFF, EAST_DIFF],
    TileType.NORTH_WEST: [NORTH_DIFF, WEST_DIFF],
    TileType.SOUTH_WEST: [SOUTH_DIFF, WEST_DIFF],
    TileType.SOUTH_EAST: [SOUTH_DIFF, EAST_DIFF],
    TileType.GROUND: [],
    TileType.STARTING_POSITION: [NORTH_DIFF, SOUTH_DIFF, EAST_DIFF, WEST_DIFF],
}


@dataclass
class Tile:
    position: Position
    type: TileType

    def get_connected_positions(self) -> set[Position]:
        x, y = self.position
        connected_positions = set()
        connected_position_computation = (
            CONNECTED_POSITION_COMPUTATION_MAPPING[self.type]
        )
        for (x_diff, y_diff) in connected_position_computation:
            connected_position = (x + x_diff, y + y_diff)
            connected_positions.add(connected_position)

        return connected_positions

    def is_connected_to(self, other: "Tile") -> bool:
        self_connected_to = self.get_connected_positions()
        if other.position not in self_connected_to:
            return False

        other_connected_to = other.get_connected_positions()
        if self.position not in other_connected_to:
            return False

        return True


@dataclass
class Map:
    tiles: list[list[Tile]]

    def get_tile(self, position: Position) -> Tile:
        return self.tiles[position[1]][position[0]]

    @classmethod
    def from_input(cls, data: str) -> "Map":
        tiles = []
        for y, input_line in enumerate(data.splitlines()):
            tile_line = [
                Tile(position=(x, y), type=TileType(character))
                for x, character in enumerate(input_line)
            ]
            tiles.append(tile_line)
        return Map(tiles=tiles)

    def to_str(self):
        output_lines = []
        for tile_line in self.tiles:
            output_line = "".join([tile.type.value for tile in tile_line])
            output_lines.append(output_line)
        return "\n".join(output_lines)

    def get_starting_position(self) -> Position:
        for y, tile_line in enumerate(self.tiles):
            for x, tile in enumerate(tile_line):
                if tile.type == TileType.STARTING_POSITION:
                    return x, y

    def _compute_loop(
        self, starting_position: Position, next_position: Position
    ) -> list[Position]:
        current_tile = self.get_tile(starting_position)
        next_tile = self.get_tile(next_position)
        positions = [starting_position, next_position]
        while (
            current_tile.is_connected_to(other=next_tile)
            and next_tile.position != starting_position
        ):
            possible_positions = next_tile.get_connected_positions()
            possible_positions.remove(current_tile.position)
            if len(possible_positions) != 1:
                raise RuntimeError(
                    f"Tile {next_tile} has not 2 connected tiles."
                )

            next_position = possible_positions.pop()

            current_tile = next_tile
            next_tile = self.get_tile(next_position)

            positions.append(next_position)
        if (
            next_tile.position != starting_position
            or not current_tile.is_connected_to(other=next_tile)
        ):
            raise RuntimeError("Loop cannot have been computed.")
        return positions

    def compute_loop(self) -> list[Position]:
        # For each cell next to S, try to compute the loop.
        # If it fails, restart trying to compute loop from next
        starting_position = self.get_starting_position()
        for diff in [NORTH_DIFF, SOUTH_DIFF, EAST_DIFF, WEST_DIFF]:

            current_x, current_y = starting_position
            next_x = current_x + diff[0]
            next_y = current_y + diff[1]
            next_position = (next_x, next_y)

            try:
                loop = self._compute_loop(
                    starting_position=starting_position,
                    next_position=next_position,
                )
            except RuntimeError:
                continue
            else:
                return loop

        raise RuntimeError("Couldn't have computed any loops within the map.")
