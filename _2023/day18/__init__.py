import math
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from tqdm import tqdm


class Direction(Enum):
    RIGHT = "R"
    LEFT = "L"
    DOWN = "D"
    UP = "U"


HEXA_DIRECTION_MAPPING = {
    0: Direction.RIGHT,
    1: Direction.DOWN,
    2: Direction.LEFT,
    3: Direction.UP,
}


def parse_hexadecimal(hexadecimal: str) -> tuple[Direction, int]:
    hexa_direction = hexadecimal[-1]
    hexa_length = hexadecimal[:6]

    direction = HEXA_DIRECTION_MAPPING[int(hexa_direction)]
    length = int(hexa_length.strip("#"), 16)
    return direction, length


class Position(tuple[int, int]):
    def next(self, direction: Direction, amount: int = 1) -> "Position":
        x, y = self
        if direction == Direction.RIGHT:
            x += amount
        elif direction == Direction.LEFT:
            x -= amount
        elif direction == Direction.DOWN:
            y += amount
        elif direction == Direction.UP:
            y -= amount
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


class DigPlan(list[Order]):
    @classmethod
    def from_data(cls, data: str, large_lagoon: bool = False) -> "DigPlan":
        orders = []
        for line in data.splitlines():
            direction_raw, length_raw, color_raw = line.split(" ")

            color_raw = color_raw.strip("()")

            if large_lagoon:
                direction, length = parse_hexadecimal(color_raw)
            else:
                direction = Direction(direction_raw)
                length = int(length_raw)

            orders.append(Order(direction=direction, length=length))
        return DigPlan(orders)


@dataclass
class Rectangle:
    top_left: Position
    bottom_right: Position


@dataclass
class Plan:
    loop_positions: list[Position]
    max_x: int
    max_y: int
    min_x: int
    min_y: int

    @classmethod
    def from_dig_plan(
        cls, dig_plan: DigPlan, starting_position: Optional[Position] = None
    ) -> "Plan":
        if starting_position:
            current = starting_position
        else:
            current = Position((0, 0))
        loop_positions = [current]
        max_x = 0
        max_y = 0
        min_x = math.inf
        min_y = math.inf
        progress_bar = tqdm(desc="Loading dig plan", total=len(dig_plan))
        for order in dig_plan:
            current = current.next(order.direction, amount=order.length)
            if current.x < min_x:
                min_x = current.x

            if current.x > max_x:
                max_x = current.x

            if current.y < min_y:
                min_y = current.y

            if current.y > max_y:
                max_y = current.y

            loop_positions.append(current)
            progress_bar.update(1)

        progress_bar.close()

        if min_x < 0 or min_y < 0:
            x: int = max(-min_x, 0)  # type: ignore
            y: int = max(-min_y, 0)  # type: ignore
            return Plan.from_dig_plan(
                dig_plan, starting_position=Position((x, y))
            )
        else:
            return Plan(
                loop_positions=loop_positions,
                min_x=min_x,
                max_x=max_x,
                min_y=min_y,
                max_y=max_y,
            )

    def compute_min_rectangles(self):
        ...

    def compute_area(self) -> int:
        # TODO: from loop points, compute the min rectangles
        #  https://www.reddit.com/r/GraphicsProgramming/comments/nwtw4j/comment/h1cj4ee/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
        #  Then compute area of minimal rectangles
        raise RuntimeError()
