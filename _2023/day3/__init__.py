from dataclasses import dataclass
from _2023.load_input import load_input


@dataclass
class Position:
    x: int
    y: int

    def is_close(self, other):
        x_is_close = self.x in [other.x + 1, other.x - 1, other.x]
        y_is_close = self.y in [other.y + 1, other.y - 1, other.y]
        return x_is_close and y_is_close


@dataclass
class Symbol:
    value: str
    position: Position


@dataclass
class Number:
    value: int
    positions: list[Position]

    @classmethod
    def create_from_schematic(
        cls, value_str: str, positions_tuple: list[tuple[int, int]]
    ):
        return Number(
            value=int(value_str),
            positions=[
                Position(x=position[0], y=position[1])
                for position in positions_tuple
            ],
        )

    def is_close_to_a_symbol(self, symbols: list[Symbol]) -> bool:
        return any(
            own_position.is_close(symbol.position)
            for symbol in symbols
            for own_position in self.positions
        )


class Schematic:
    def __init__(self, cells: list[list[str]]):
        self.cells = cells
        self._init_numbers_and_symbols()

    @classmethod
    def from_data(cls, data: str) -> "Schematic":
        cells = []
        for line in data.split("\n"):
            cells_line = [character for character in line]
            cells.append(cells_line)
        return Schematic(cells)

    def _init_numbers_and_symbols(self):
        numbers = []
        symbols = []
        for y in range(len(self.cells)):
            is_in_number = False
            current_number = ""
            current_number_positions = []
            for x in range(len(self.cells[y])):
                cell = self.cells[y][x]
                if cell.isdecimal():
                    is_in_number = True
                    current_number = f"{current_number}{cell}"
                    current_number_positions.append((x, y))
                else:
                    if is_in_number:
                        numbers.append(
                            Number.create_from_schematic(
                                value_str=current_number,
                                positions_tuple=current_number_positions,
                            )
                        )
                        is_in_number = False
                        current_number = ""
                        current_number_positions = []
                    if cell != ".":
                        symbols.append(
                            Symbol(value=cell, position=Position(x=x, y=y))
                        )

            if is_in_number:
                numbers.append(
                    Number.create_from_schematic(
                        value_str=current_number,
                        positions_tuple=current_number_positions,
                    )
                )

        self.numbers = numbers
        self.symbols = symbols

    def __repr__(self):
        return f"<Schematic cells={self.cells}>"

    def __eq__(self, other):
        return self.cells == other.cells


def compute_answer(data: str) -> int:
    schematic = Schematic.from_data(data)

    part_numbers = []
    for number in schematic.numbers:
        if number.is_close_to_a_symbol(schematic.symbols):
            part_numbers.append(number)

    return sum(part_number.value for part_number in part_numbers)


if __name__ == "__main__":
    print(compute_answer(load_input(3)))
