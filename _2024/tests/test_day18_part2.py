from _2024.day18 import Map
from _2024.day18.part2 import compute_solution

MAP = Map(
    map_size=6,
    obstacles=[
        (5, 4),
        (4, 2),
        (4, 5),
        (3, 0),
        (2, 1),
        (6, 3),
        (2, 4),
        (1, 5),
        (0, 6),
        (3, 3),
        (2, 6),
        (5, 1),
        (1, 2),
        (5, 5),
        (2, 5),
        (6, 5),
        (1, 4),
        (0, 4),
        (6, 4),
        (1, 1),
        (6, 1),
        (1, 0),
        (0, 5),
        (1, 6),
        (2, 0),
    ],
)


def test_first_byte_that_block_the_path_can_be_computed():
    assert compute_solution(MAP) == (6, 1)
