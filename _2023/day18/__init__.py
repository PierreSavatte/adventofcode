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


class Plan:
    def __init__(self, dug_cells: list[Position]):
        self.dug_cells = dug_cells

    @classmethod
    def from_dig_plan(cls, dig_plan: DigPlan) -> "Plan":
        current = Position((0, 0))
        dug_cells = [current]
        for order in dig_plan:
            for i in range(order.length):
                current = current.next(order.direction)
                dug_cells.append(current)
        return Plan(dug_cells=dug_cells)
