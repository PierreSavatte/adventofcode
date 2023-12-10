import math
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


@dataclass
class Map:
    tiles: list[list[Tile]]

    def get_tile(self, position: Position) -> Tile:
        return self.tiles[position[1]][position[0]]

    @property
    def max_x(self) -> int:
        return len(self.tiles[0]) - 1

    @property
    def max_y(self) -> int:
        return len(self.tiles[1]) - 1

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
    ) -> Loop:
        current_tile = self.get_tile(starting_position)
        next_tile = self.get_tile(next_position)
        loop = Loop()
        loop.add_tile(tile=current_tile, distance_from_start=0)
        loop.add_tile(tile=next_tile, distance_from_start=1)
        distance = 2
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
            loop.add_tile(tile=next_tile, distance_from_start=distance)
            distance += 1

        if (
            next_tile.position != starting_position
            or not current_tile.is_connected_to(other=next_tile)
        ):
            raise RuntimeError("Loop cannot have been computed.")
        return loop

    def compute_loop(self, validate_distances: bool = True) -> Loop:
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
                if validate_distances:
                    loop.validate_distances()
                return loop

        raise RuntimeError("Couldn't have computed any loops within the map.")

    def compute_loop_map(self) -> "Map":
        loop = self.compute_loop()
        loop_positions = loop.positions

        new_tiles = []
        for tile_line in self.tiles:
            new_tiles_line = []
            for tile in tile_line:
                if tile.position not in loop_positions:
                    tile = Tile(position=tile.position, type=TileType.GROUND)
                new_tiles_line.append(tile)
            new_tiles.append(new_tiles_line)

        return Map(tiles=new_tiles)

    def compute_enclosed_map(self) -> "Map":
        loop = self.compute_loop(validate_distances=False)

        new_tiles = []
        for tile_line in self.tiles:
            new_tiles_line = []
            for tile in tile_line:
                if (
                    tile.type == TileType.GROUND
                    and is_position_enclosed_by_loop_using_winding_number(
                        position=tile.position,
                        loop=loop,
                        max_x=self.max_x,
                        max_y=self.max_y,
                    )
                ):
                    tile = Tile(position=tile.position, type=TileType.ENCLOSED)
                new_tiles_line.append(tile)
            new_tiles.append(new_tiles_line)

        return Map(tiles=new_tiles)

    def compute_enclosed_tiles(self):
        map = self.compute_enclosed_map()
        enclosed_tiles = 0
        for tile_line in map.tiles:
            for tile in tile_line:
                if tile.type == TileType.ENCLOSED:
                    enclosed_tiles += 1
        return enclosed_tiles


def is_position_enclosed_by_loop_using_ray_casting(
    position: Position, loop: Loop, max_x: int, max_y: int
) -> bool:
    starting_x = position[0]
    ending_x = max_x
    loop_positions = loop.positions

    y = position[1]
    count = 0
    for x in range(starting_x, ending_x + 1):
        if (x, y) in loop_positions:
            count += 1
    # If the point is on the inside of the polygon then it will intersect
    # the edge an odd number of times.
    return count % 2 != 0


def edge_function(p: Position, vertices: tuple[Position, Position]) -> float:
    a, b = vertices
    return (p[0] - a[0]) * (b[1] - a[1]) - (p[1] - a[1]) * (b[0] - a[0])


def _winding_number_x_range(
    position: Position, loop: Loop, max_x: int
) -> bool:
    loop_positions = loop.positions

    y = position[1]
    winding_number = 0
    for x in range(-1, max_x + 2):
        current_position = (x, y)
        if current_position in loop_positions:
            i = loop.get_position_index(current_position)
            vertices = loop[i].position, loop[i + 1].position
            edge = edge_function(position, vertices)
            if edge == 0:
                pass
            elif edge > 0:
                winding_number += 1
            else:
                winding_number -= 1

    return winding_number != 0


def _winding_number_y_range(
    position: Position, loop: Loop, max_y: int
) -> bool:
    loop_positions = loop.positions

    x = position[0]
    winding_number = 0
    for y in range(-1, max_y + 2):
        current_position = (x, y)
        if current_position in loop_positions:
            i = loop.get_position_index(current_position)
            vertices = loop[i].position, loop[i + 1].position
            edge = edge_function(position, vertices)
            if edge == 0:
                pass
            elif edge > 0:
                winding_number += 1
            else:
                winding_number -= 1

    return winding_number != 0


def is_position_enclosed_by_loop_using_winding_number(
    position: Position, loop: Loop, max_x: int, max_y: int
) -> bool:
    enclosed_winding_x = _winding_number_x_range(position, loop, max_x)
    enclosed_winding_y = _winding_number_y_range(position, loop, max_y)
    return enclosed_winding_x and enclosed_winding_y
