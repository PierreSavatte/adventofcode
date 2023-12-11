from _2023.day10 import Position, Loop


def is_position_enclosed_by_loop_using_ray_casting(
    position: Position, loop: Loop, max_x: int, max_y: int
) -> bool:
    # Tracing a ray from position to (+infinity, position[1])
    # and count how many edges it crosses

    x, y = position
    loop_positions = loop.shape
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
