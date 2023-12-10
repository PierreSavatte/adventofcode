from _2023.day10 import Position, Loop


def edge_function(p: Position, vertices: tuple[Position, Position]) -> float:
    a, b = vertices
    return (p[0] - a[0]) * (b[1] - a[1]) - (p[1] - a[1]) * (b[0] - a[0])


def _winding_number_x_range(
    position: Position, loop: Loop, max_x: int
) -> bool:
    loop_positions = loop.positions

    y = position[1]
    winding_number = 0
    for x in range(-1, max_x + 2):
        current_position = (x, y)
        if current_position in loop_positions:
            i = loop.get_position_index(current_position)
            vertices = loop[i].position, loop[i + 1].position
            edge = edge_function(position, vertices)
            if edge == 0:
                pass
            elif edge > 0:
                winding_number += 1
            else:
                winding_number -= 1

    return winding_number != 0


def _winding_number_y_range(
    position: Position, loop: Loop, max_y: int
) -> bool:
    loop_positions = loop.positions

    x = position[0]
    winding_number = 0
    for y in range(-1, max_y + 2):
        current_position = (x, y)
        if current_position in loop_positions:
            i = loop.get_position_index(current_position)
            vertices = loop[i].position, loop[i + 1].position
            edge = edge_function(position, vertices)
            if edge == 0:
                pass
            elif edge > 0:
                winding_number += 1
            else:
                winding_number -= 1

    return winding_number != 0


def is_position_enclosed_by_loop_using_winding_number(
    position: Position, loop: Loop, max_x: int, max_y: int
) -> bool:
    enclosed_winding_x = _winding_number_x_range(position, loop, max_x)
    enclosed_winding_y = _winding_number_y_range(position, loop, max_y)
    return enclosed_winding_x and enclosed_winding_y
