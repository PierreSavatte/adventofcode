from typing import Optional

from _2025.load_input import load_input

MAP = list[list[str]]
NEIGHBOURS_COUNT = list[list[Optional[int]]]


def parse_map(input: str) -> MAP:
    map = []
    for row in input.strip().splitlines():
        map.append(list(row))
    return map


def get_neighbours(map: MAP, x: int, y: int) -> list[str]:
    neighbours = []
    for y_ in range(y - 1, y + 2):
        if y_ < 0 or y_ >= len(map):
            continue

        for x_ in range(x - 1, x + 2):
            if x_ < 0 or x_ >= len(map[0]):
                continue
            if x_ == x and y_ == y:
                continue

            neighbours.append(map[y_][x_])

    return neighbours


def compute_neighbour_count(map: MAP) -> NEIGHBOURS_COUNT:
    new_map = []
    for y in range(len(map)):
        new_row = []
        for x in range(len(map[y])):
            if map[y][x] == ".":
                count = None
            else:
                neighbours = get_neighbours(map, x, y)
                count = sum(neighbour == "@" for neighbour in neighbours)
            new_row.append(count)
        new_map.append(new_row)
    return new_map


def flatten_2d_map(map: NEIGHBOURS_COUNT) -> list[int]:
    flatten = []
    for row in map:
        flatten.extend(row)
    return flatten


def mark(map: MAP) -> list[str]:
    neighbour_count = compute_neighbour_count(map)
    new_map = []
    for y in range(len(map)):
        new_row = []
        for x in range(len(map[y])):
            nb_neighbours = neighbour_count[y][x]
            if nb_neighbours is None:
                cell = "."
            else:
                if nb_neighbours < 4:
                    cell = "x"
                else:
                    cell = "@"

            new_row.append(cell)
        new_map.append("".join(new_row) + "\n")
    return new_map


def compute_solution(map: MAP) -> int:
    neighbours_count = flatten_2d_map(compute_neighbour_count(map))
    return sum(bool(count and count < 4) for count in neighbours_count)


def main():
    map = parse_map(load_input(4))
    print(compute_solution(map))


if __name__ == "__main__":
    # > 1390
    # < 3699
    # != 2311
    # != 3471
    main()
