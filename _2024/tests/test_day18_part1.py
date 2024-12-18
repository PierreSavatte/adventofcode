from _2024.day18 import Map, parse_input
from _2024.day18.part1 import compute_solution

TEST_INPUT = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

MAP = Map(
    map_size=6,
    current_fallen_bytes_number=12,
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


def test_input_can_be_parsed():
    assert (
        parse_input(TEST_INPUT, map_size=6, current_fallen_bytes_number=12)
        == MAP
    )


def test_map_can_be_plotted():
    assert (
        MAP.plot()
        == """...#...
..#..#.
....#..
...#..#
..#..#.
.#..#..
#.#...."""
    )


def test_path_can_be_computed():
    assert MAP.get_path() == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (3, 1),
        (4, 1),
        (4, 0),
        (5, 0),
        (6, 0),
        (6, 1),
        (6, 2),
        (5, 2),
        (5, 3),
        (4, 3),
        (4, 4),
        (3, 4),
        (3, 5),
        (3, 6),
        (4, 6),
        (5, 6),
        (6, 6),
    ]


def test_solution_can_be_computed():
    assert compute_solution(MAP) == 22
