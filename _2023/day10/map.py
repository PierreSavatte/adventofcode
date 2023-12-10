from dataclasses import dataclass

from _2023.day10 import (
    Tile,
    Position,
    TileType,
    Loop,
    NORTH_DIFF,
    SOUTH_DIFF,
    EAST_DIFF,
    WEST_DIFF,
)

from _2023.day10.enclosing import compute_enclosing, EnclosingType


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
                if tile.type == TileType.GROUND:
                    is_enclosed = compute_enclosing(
                        function=EnclosingType.WINDING,
                        position=tile.position,
                        loop=loop,
                        max_x=self.max_x,
                        max_y=self.max_y,
                    )
                    if is_enclosed:
                        tile = Tile(
                            position=tile.position, type=TileType.ENCLOSED
                        )
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
