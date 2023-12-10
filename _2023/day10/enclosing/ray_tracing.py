from _2023.day10 import Position, Loop


def is_position_enclosed_by_loop_using_ray_casting(
    position: Position, loop: Loop, max_x: int, max_y: int
) -> bool:
    starting_x = position[0]
    ending_x = max_x
    loop_positions = loop.positions

    y = position[1]
    count = 0
    for x in range(starting_x, ending_x + 1):
        if (x, y) in loop_positions:
            count += 1
    # If the point is on the inside of the polygon then it will intersect
    # the edge an odd number of times.
    return count % 2 != 0
