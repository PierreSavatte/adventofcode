from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    RIGHT = "R"
    LEFT = "L"
    DOWN = "D"
    UP = "U"


class Position(tuple[int, int]):
    def next(self, direction: Direction) -> "Position":
        x, y = self
        if direction == Direction.RIGHT:
            x += 1
        elif direction == Direction.LEFT:
            x -= 1
        elif direction == Direction.DOWN:
            y += 1
        elif direction == Direction.UP:
            y -= 1
        return Position((x, y))

    @property
    def x(self) -> int:
        return self[0]

    @property
    def y(self) -> int:
        return self[1]


@dataclass
class Order:
    direction: Direction
    length: int
    color: str


class DigPlan(list[Order]):
    @classmethod
    def from_data(cls, data: str) -> "DigPlan":
        orders = []
        for line in data.splitlines():
            direction_raw, length_raw, color_raw = line.split(" ")

            color = color_raw.strip("()")

            orders.append(
                Order(
                    direction=Direction(direction_raw),
                    length=int(length_raw),
                    color=color,
                )
            )
        return DigPlan(orders)


class Tiles(list[list[str]]):
    ...


@dataclass
class Plan:
    dug_cells: list[Position]
    max_x: int
    max_y: int

    @property
    def tiles(self) -> Tiles:
        tiles = []
        for y in range(self.max_y + 1):
            tiles_line = []
            for x in range(self.max_x + 1):
                tiles_line.append(".")
            tiles.append(tiles_line)

        for dug_cell in self.dug_cells:
            tiles[dug_cell.y][dug_cell.x] = "#"

        return Tiles(tiles)

    def as_string(self) -> str:
        return "\n".join("".join(line) for line in self.tiles)

    @classmethod
    def from_dig_plan(cls, dig_plan: DigPlan) -> "Plan":
        current = Position((0, 0))
        dug_cells = [current]
        max_x = 0
        max_y = 0
        for order in dig_plan:
            for i in range(order.length):
                current = current.next(order.direction)
                dug_cells.append(current)

                if current.x > max_x:
                    max_x = current.x

                if current.y > max_y:
                    max_y = current.y

        return Plan(dug_cells=dug_cells, max_x=max_x, max_y=max_y)
