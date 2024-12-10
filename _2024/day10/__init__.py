from dataclasses import dataclass

MAP = list[list[int]]
POSITION = tuple[int, int]


def parse_input(data: str) -> MAP:
    data = data.strip("\n")

    map = [[int(char) for char in line] for line in data.split("\n")]

    return map


def _get_positions(map: MAP, lookup_value: int) -> list[POSITION]:
    trailheads = []
    for y, line in enumerate(map):
        for x, cell in enumerate(line):
            if cell == lookup_value:
                trailheads.append((x, y))
    return trailheads


def get_trailheads(map: MAP) -> list[POSITION]:
    return _get_positions(map, lookup_value=0)


def get_trail_destinations(map: MAP) -> list[POSITION]:
    return _get_positions(map, lookup_value=9)


def get_value(map: MAP, position: POSITION) -> int:
    x, y = position
    return map[y][x]


def get_neighbors(map: MAP, position: POSITION) -> list[POSITION]:
    map_size = len(map)
    x, y = position

    neighbors = []
    for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = position
        new_x = x + delta_x
        new_y = y + delta_y
        if not (0 <= new_x < map_size and 0 <= new_y < map_size):
            # Not in the map
            continue

        new_position = (new_x, new_y)
        if get_value(map, new_position) == get_value(map, position) + 1:
            neighbors.append(new_position)
    return neighbors


@dataclass
class HikingTrail:
    positions: list[POSITION]

