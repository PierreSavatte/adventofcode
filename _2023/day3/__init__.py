from dataclasses import dataclass


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

    def get_numbers_it_is_close_to(
        self, numbers: list["Number"]
    ) -> list["Number"]:
        numbers_it_is_close_to = []
        for number in numbers:
            if number.is_close_to_a_symbol([self]):
                numbers_it_is_close_to.append(number)
        return numbers_it_is_close_to


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


@dataclass
class Gear:
    position: Position
    numbers: list[Number]

    @property
    def ratio(self) -> int:
        ratio = 1
        for number in self.numbers:
            ratio *= number.value
        return ratio


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

    def get_gears(self):
        gears = []
        for symbol in self.symbols:
            numbers_it_is_closed_to = symbol.get_numbers_it_is_close_to(
                self.numbers
            )
            if len(numbers_it_is_closed_to) == 2:
                gears.append(
                    Gear(
                        position=symbol.position,
                        numbers=numbers_it_is_closed_to,
                    )
                )
        return gears

    def __repr__(self):
        return f"<Schematic cells={self.cells}>"

    def __eq__(self, other):
        return self.cells == other.cells
