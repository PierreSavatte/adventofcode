from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    RIGHT = "R"
    LEFT = "L"
    DOWN = "D"
    UP = "U"


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
