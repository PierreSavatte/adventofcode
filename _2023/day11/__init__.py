from copy import deepcopy
from dataclasses import dataclass
from typing import Any

Table = list[list[Any]]
Position = tuple[int, int]


def is_list_composed_only_of_character(l: list, character: str) -> bool:
    return all(c == character for c in l)


def expand_lines_of_table(table: Table, age: int) -> Table:
    table = deepcopy(table)
    i = 0
    while i < len(table):
        line = table[i]
        if is_list_composed_only_of_character(line, "."):

            # To overcome a problem I did not totally understood 🙈
            if age == 1:
                age += 1

            new_lines = [line for _ in range(age)]
            table = [*table[:i], *new_lines, *table[i + 1 :]]
            i += age
        i += 1

    return table


def transpose_table(table: Table):
    table_col_length = len(table[0])
    table_row_length = len(table)

    new_table = [
        [0 for _ in range(table_row_length)] for _ in range(table_col_length)
    ]

    for x, line in enumerate(table):
        for y, item in enumerate(line):
            new_table[y][x] = item

    return new_table


def manhattan_distance(a: Position, b: Position) -> int:
    x_a, y_a = a
    x_b, y_b = b
    return abs(x_b - x_a) + abs(y_b - y_a)


@dataclass
class Universe:
    tiles: Table

    def get_tile_at_position(self, position: Position) -> Any:
        (x, y) = position
        return self.tiles[y][x]

    @classmethod
    def from_input(cls, data: str) -> "Universe":
        tiles = [
            [character for character in line] for line in data.splitlines()
        ]
        return Universe(tiles=tiles)

    def expand(self, age: int = 1) -> "Universe":
        expanded_lines = expand_lines_of_table(self.tiles, age=age)
        tiles = transpose_table(
            expand_lines_of_table(transpose_table(expanded_lines), age=age)
        )
        return Universe(tiles=tiles)

    @property
    def galaxy_positions(self) -> list[Position]:
        positions = []
        for y, line in enumerate(self.tiles):
            for x, item in enumerate(line):
                position = (x, y)
                if self.get_tile_at_position(position) == "#":
                    positions.append(position)
        return positions

    @property
    def galaxy_pairs(self) -> list[tuple[Position, Position]]:
        pairs = []
        for i, a in enumerate(self.galaxy_positions):
            for b in self.galaxy_positions[i + 1 :]:
                pairs.append((a, b))
        return pairs
