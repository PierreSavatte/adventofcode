from dataclasses import dataclass
from enum import Enum
from tqdm import tqdm


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

    def compute_fully_dug_plan(self) -> "Plan":
        additional_dug_cells = []
        progress_bar = tqdm(total=self.max_x * self.max_y)
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                position = Position((x, y))
                progress_bar.update(1)
                if position in self.dug_cells:
                    continue
                if is_position_enclosed_by_loop_using_ray_casting(
                    position=position,
                    loop_positions=self.dug_cells,
                ):
                    additional_dug_cells.append(position)

        total_dug_cells = list({*self.dug_cells, *additional_dug_cells})
        return Plan(
            dug_cells=total_dug_cells, max_x=self.max_x, max_y=self.max_y
        )


def is_position_enclosed_by_loop_using_ray_casting(
    position: Position, loop_positions: list[Position]
) -> bool:
    # Tracing a ray from position to (+infinity, position[1])
    # and count how many edges it crosses

    x, y = position
    count = 0
    for i in range(len(loop_positions) - 1):
        edge_a = loop_positions[i]
        edge_b = loop_positions[i + 1]

        x_a, y_a = edge_a
        x_b, y_b = edge_b

        if min(y_a, y_b) < y <= max(y_a, y_b):
            # Proceed only if infinite_ray cross the edge

            if x <= max(x_a, x_b):
                # Proceed only if start of infinite ray if before the edge

                x_intersection = (y - y_a) * (x_b - x_a) / (y_b - y_a) + x_a

                if x_a == x_b or x <= x_intersection:
                    count += 1

    return count % 2 != 0
