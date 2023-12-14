from dataclasses import dataclass
from copy import deepcopy

Position = tuple[int, int]
Tiles = list[list[str]]


def set_tile_at_position(tiles: Tiles, position: Position, new_value: str):
    x, y = position
    tiles[y][x] = new_value


def get_tile_at_position(tiles: Tiles, position: Position) -> str:
    x, y = position
    return tiles[y][x]


def compute_min_y(tiles: Tiles, rounded_rock_position: Position) -> int:
    rock_x, rock_y = rounded_rock_position
    min_y = rock_y
    for y in range(rock_y, -1, -1):
        min_y = y
        if y == 0:
            continue
        tile_above = get_tile_at_position(
            tiles=tiles, position=(rock_x, y - 1)
        )
        if tile_above == "#" or tile_above == "O":
            break
    return min_y


@dataclass
class Platform:
    tiles: Tiles
    rounded_rocks_positions: list[Position]

    @classmethod
    def from_input(cls, data: str) -> "Platform":
        rounded_rocks_positions = []
        tiles = []
        for y, line in enumerate(data.splitlines()):
            tiles_line = []
            for x, cell in enumerate(line):
                if cell == "O":
                    rounded_rocks_positions.append((x, y))
                tiles_line.append(cell)
            tiles.append(tiles_line)

        return Platform(
            tiles=tiles, rounded_rocks_positions=rounded_rocks_positions
        )

    def get_tile_at_position(self, position: Position) -> str:
        return get_tile_at_position(self.tiles, position)

    def as_str(self) -> str:
        return "\n".join("".join(tile) for tile in self.tiles)

    def compute_tiles_with_no_rounded_rocks(self):
        tiles = deepcopy(self.tiles)
        for rounded_rocks_position in self.rounded_rocks_positions:
            x, y = rounded_rocks_position
            tiles[y][x] = "."
        return tiles

    def tilt_north(self) -> "Platform":
        rounded_rocks_positions = []
        new_tiles = self.compute_tiles_with_no_rounded_rocks()

        for rounded_rock_position in self.rounded_rocks_positions:
            rock_x, rock_y = rounded_rock_position

            min_y = compute_min_y(
                tiles=new_tiles, rounded_rock_position=rounded_rock_position
            )

            new_position = (rock_x, min_y)
            new_tiles[min_y][rock_x] = "O"
            rounded_rocks_positions.append(new_position)

        return Platform(
            tiles=new_tiles, rounded_rocks_positions=rounded_rocks_positions
        )

    def compute_load(self) -> int:
        max_y = len(self.tiles)
        load = 0
        for rounded_rock_position in self.rounded_rocks_positions:
            _, y = rounded_rock_position
            load += max_y - y
        return load
