from copy import deepcopy
from dataclasses import dataclass
from typing import Callable


Position = tuple[int, int]
Tiles = list[list[str]]


def set_tile_at_position(tiles: Tiles, position: Position, new_value: str):
    x, y = position
    tiles[y][x] = new_value


def get_tile_at_position(tiles: Tiles, position: Position) -> str:
    x, y = position
    return tiles[y][x]


def compute_most_north_position(
    tiles: Tiles, rounded_rock_position: Position
) -> Position:
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
    return rock_x, min_y


def compute_most_south_position(
    tiles: Tiles, rounded_rock_position: Position
) -> Position:
    tiles_max_y = len(tiles) - 1
    rock_x, rock_y = rounded_rock_position
    max_y = rock_y
    for y in range(rock_y, tiles_max_y + 1):
        max_y = y
        if y == tiles_max_y:
            continue
        tile_below = get_tile_at_position(
            tiles=tiles, position=(rock_x, y + 1)
        )
        if tile_below == "#" or tile_below == "O":
            break
    return rock_x, max_y


def compute_most_west_position(
    tiles: Tiles, rounded_rock_position: Position
) -> Position:
    rock_x, rock_y = rounded_rock_position
    min_x = rock_y
    for x in range(rock_x, -1, -1):
        min_x = x
        if x == 0:
            continue
        tile_on_left = get_tile_at_position(
            tiles=tiles, position=(x - 1, rock_y)
        )
        if tile_on_left == "#" or tile_on_left == "O":
            break
    return min_x, rock_y


def compute_most_east_position(
    tiles: Tiles, rounded_rock_position: Position
) -> Position:
    tiles_max_x = len(tiles[0]) - 1
    rock_x, rock_y = rounded_rock_position
    max_x = rock_x
    for x in range(rock_x, tiles_max_x + 1):
        max_x = x
        if x == tiles_max_x:
            continue
        tile_on_right = get_tile_at_position(
            tiles=tiles, position=(x + 1, rock_y)
        )
        if tile_on_right == "#" or tile_on_right == "O":
            break
    return max_x, rock_y


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

    def _tilt(
        self,
        compute_new_position: Callable,
        sorted_rounded_rocks_positions: list[Position],
    ) -> "Platform":
        rounded_rocks_positions = []
        new_tiles = self.compute_tiles_with_no_rounded_rocks()

        for rounded_rock_position in sorted_rounded_rocks_positions:
            new_position = compute_new_position(
                tiles=new_tiles, rounded_rock_position=rounded_rock_position
            )

            x, y = new_position
            new_tiles[y][x] = "O"
            rounded_rocks_positions.append(new_position)

        return Platform(
            tiles=new_tiles, rounded_rocks_positions=rounded_rocks_positions
        )

    def tilt_north(self) -> "Platform":
        sorted_rounded_rocks_positions = sorted(
            self.rounded_rocks_positions, key=lambda x: x[1]
        )
        return self._tilt(
            compute_new_position=compute_most_north_position,
            sorted_rounded_rocks_positions=sorted_rounded_rocks_positions,
        )

    def tilt_south(self) -> "Platform":
        sorted_rounded_rocks_positions = sorted(
            self.rounded_rocks_positions, key=lambda x: x[1], reverse=True
        )
        return self._tilt(
            compute_new_position=compute_most_south_position,
            sorted_rounded_rocks_positions=sorted_rounded_rocks_positions,
        )

    def tilt_east(self) -> "Platform":
        sorted_rounded_rocks_positions = sorted(
            self.rounded_rocks_positions, key=lambda x: x[0], reverse=True
        )
        return self._tilt(
            compute_new_position=compute_most_east_position,
            sorted_rounded_rocks_positions=sorted_rounded_rocks_positions,
        )

    def tilt_west(self) -> "Platform":
        sorted_rounded_rocks_positions = sorted(
            self.rounded_rocks_positions, key=lambda x: x[0]
        )
        return self._tilt(
            compute_new_position=compute_most_west_position,
            sorted_rounded_rocks_positions=sorted_rounded_rocks_positions,
        )

    def _compute_circle(self, n: int) -> "CircleData":
        platform = self
        cache = {}
        circle = []
        first_tilted_platforms = None
        last_tilted_platforms = None
        circle_started_at = None
        for i in range(n):

            platforms = []
            for step_name in [
                "tilt_north",
                "tilt_west",
                "tilt_south",
                "tilt_east",
            ]:
                step = getattr(platform, step_name)
                platform = step()
                platforms.append(platform)

            tilted_platforms = TiltedPlatforms(
                north=platforms[0],
                west=platforms[1],
                south=platforms[2],
                east=platforms[3],
            )
            if tilted_platforms in cache.values():
                if first_tilted_platforms is None:
                    circle_started_at = i
                    first_tilted_platforms = tilted_platforms
                else:
                    if tilted_platforms == first_tilted_platforms:
                        return CircleData(
                            circle_started_at=circle_started_at,  # noqa: E501
                            platform_at_end_of_circle=last_tilted_platforms.east,  # noqa: E501
                            circle=circle,
                        )
                circle.append(i)
            cache[i] = tilted_platforms
            last_tilted_platforms = tilted_platforms

    def _compute_next_cycle(self) -> "Platform":
        platform = self
        for step_name in [
            "tilt_north",
            "tilt_west",
            "tilt_south",
            "tilt_east",
        ]:
            step = getattr(platform, step_name)
            platform = step()
        return platform

    def spin_cycle(self, n: int = 1) -> "Platform":
        circle_data = self._compute_circle(n)

        rest_of_iterations_after_first_cycle = (
            n - circle_data.circle_started_at
        )
        rest_of_iterations = rest_of_iterations_after_first_cycle % (
            len(circle_data.circle)
        )

        platform = circle_data.platform_at_end_of_circle
        for i in range(rest_of_iterations):
            platform = platform._compute_next_cycle()

        return platform

    def compute_load(self) -> int:
        max_y = len(self.tiles)
        load = 0
        for rounded_rock_position in self.rounded_rocks_positions:
            _, y = rounded_rock_position
            load += max_y - y
        return load


@dataclass
class TiltedPlatforms:
    north: Platform
    south: Platform
    east: Platform
    west: Platform

    def __eq__(self, other):
        equal = True
        for attr in ["north", "south", "east", "west"]:
            self_platform = getattr(self, attr)
            other_platform = getattr(other, attr)
            equal = equal and (self_platform.tiles == other_platform.tiles)
        return equal


@dataclass
class CircleData:
    circle_started_at: int
    platform_at_end_of_circle: Platform
    circle: list[int]
