from dataclasses import dataclass
from enum import Enum


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
    ENCLOSED = "I"


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
    TileType.ENCLOSED: [],
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
class LoopTile(Tile):
    distance_from_start: int

    @classmethod
    def from_tile(cls, tile: Tile, distance_from_start: int) -> "LoopTile":
        return LoopTile(
            position=tile.position,
            type=tile.type,
            distance_from_start=distance_from_start,
        )


class Loop(list):
    def add_tile(self, tile: Tile, distance_from_start: int):
        self.append(
            LoopTile.from_tile(
                tile=tile, distance_from_start=distance_from_start
            )
        )

    def get_position_index(self, position: Position) -> int:
        for i, tile in enumerate(self):
            if tile.position == position:
                return i

        raise ValueError(f"{position} is not in list")

    @property
    def positions(self) -> list[Position]:
        return [tile.position for tile in self]

    @property
    def distances(self) -> dict[Position, int]:
        return {tile.position: tile.distance_from_start for tile in self}

    def validate_distances(self):
        new_distance = 0
        for tile_index in range(len(self) - 1, -1, -1):
            tile = self[tile_index]

            if tile.distance_from_start <= new_distance:
                break
            else:
                tile.distance_from_start = new_distance
            new_distance += 1
