from typing import Generator, Optional

PARSED_MAP = list[list[str]]
POSITION = tuple[int, int]


class Map:
    def __init__(self, input: str):
        rows = input.strip().splitlines()
        self.width = len(rows[0])
        self.height = len(rows)
        self.cells = []
        for y, row in enumerate(rows):
            new_row = []
            for x, cell_value in enumerate(row):
                is_roll = cell_value == "@"
                cell = Cell(map=self, is_roll=is_roll, x=x, y=y)
                new_row.append(cell)
            self.cells.append(new_row)

    def get_neighbour_positions(self, x: int, y: int) -> list[POSITION]:
        neighbours = []
        for y_ in range(y - 1, y + 2):
            if y_ < 0 or y_ >= self.height:
                continue

            for x_ in range(x - 1, x + 2):
                if x_ < 0 or x_ >= self.width:
                    continue
                if x_ == x and y_ == y:
                    continue

                neighbours.append((x_, y_))

        return neighbours

    def get_cell(self, position: POSITION) -> "Cell":
        x, y = position
        return self.cells[y][x]

    def iterate_over_cells(self) -> Generator["Cell", None, None]:
        for row in self.cells:
            for cell in row:
                yield cell


class Cell:
    def __init__(self, map: Map, is_roll: bool, x: int, y: int):
        self.is_roll = is_roll

        self.x = x
        self.y = y
        self.position = (x, y)
        self.map = map

        self.neighbour_positions = map.get_neighbour_positions(x, y)

    def compute_nb_roll_neighbours(self) -> Optional[int]:
        if not self.is_roll:
            return None
        return sum(
            self.map.get_cell(neighbour_position).is_roll
            for neighbour_position in self.neighbour_positions
        )
