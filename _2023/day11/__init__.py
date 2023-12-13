from dataclasses import dataclass
from typing import Any

from _2023.utils import transpose_table

Table = list[list[Any]]
Position = tuple[int, int]


def is_list_composed_only_of_character(l: list, character: str) -> bool:
    return all(c == character for c in l)


def _compute_expanded_lines(table: Table):
    expanded_lines = []
    for i, line in enumerate(table):
        if is_list_composed_only_of_character(line, "."):
            expanded_lines.append(i)
    return expanded_lines


def manhattan_distance(a: Position, b: Position) -> int:
    x_a, y_a = a
    x_b, y_b = b
    return abs(x_b - x_a) + abs(y_b - y_a)


@dataclass
class Universe:
    age: int

    tiles: Table

    expanded_columns: list[int]
    expanded_rows: list[int]

    def get_tile_at_position(self, position: Position) -> Any:
        (x, y) = position
        return self.tiles[y][x]

    @classmethod
    def from_input(cls, data: str, age: int = 1) -> "Universe":
        tiles = [
            [character for character in line] for line in data.splitlines()
        ]

        expanded_rows = _compute_expanded_lines(tiles)

        transposed_tiles = transpose_table(tiles)

        expanded_columns = _compute_expanded_lines(transposed_tiles)

        return Universe(
            age=age,
            tiles=tiles,
            expanded_rows=expanded_rows,
            expanded_columns=expanded_columns,
        )

    def compute_expanded_distance_between_points(
        self, a: Position, b: Position
    ) -> int:
        distance = manhattan_distance(a, b)

        # To overcome a problem I did not totally understood 🙈
        age = self.age
        if age == 1:
            age += 1

        x_a, y_a = a
        x_b, y_b = b

        min_x = min(x_a, x_b)
        max_x = max(x_a, x_b)
        for x in range(min_x, max_x):
            if x in self.expanded_columns:
                distance += age - 1

        min_y = min(y_a, y_b)
        max_y = max(y_a, y_b)
        for y in range(min_y, max_y):
            if y in self.expanded_rows:
                distance += age - 1

        return distance

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
