from enum import Enum

from _2023.day10 import Position, Loop
from _2023.day10.enclosing.ray_tracing import (
    is_position_enclosed_by_loop_using_ray_casting,
)
from _2023.day10.enclosing.winding import (
    is_position_enclosed_by_loop_using_winding_number,
)


class EnclosingType(Enum):
    WINDING = is_position_enclosed_by_loop_using_winding_number
    RAY_TRACING = is_position_enclosed_by_loop_using_ray_casting


def compute_enclosing(
    function: callable, position: Position, loop: Loop, max_x: int, max_y: int
):
    return function(position=position, loop=loop, max_x=max_x, max_y=max_y)
