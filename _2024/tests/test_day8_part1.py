from _2024.day8 import Map, Point, parse_input
from _2024.day8.part1 import compute_solution

TEST_INPUT = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

MAP = Map(
    size=12,
    antennas={
        "A": [Point(6, 5), Point(8, 8), Point(9, 9)],
        "0": [Point(8, 1), Point(5, 2), Point(7, 3), Point(4, 4)],
    },
)


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == MAP


def test_point_reflection_can_be_computed():
    """
    ..........
    ...i......
    ..........
    ....a.....
    ..........
    .....b....
    ..........
    ......j...
    ..........
    ..........
    """
    a = Point(4, 3)
    b = Point(5, 5)

    i = Point(3, 1)
    j = Point(6, 7)

    assert a.reflection_from(b) == j
    assert b.reflection_from(a) == i


def test_antinodes_can_be_computed():
    """
    ..........
    ...#......
    #.........
    ....a.....
    ........a.
    .....a....
    ..#.......
    ......#...
    ..........
    ..........
    """
    map = Map(size=10, antennas={"a": [Point(4, 3), Point(8, 4), Point(5, 5)]})

    assert map.compute_antinodes() == {
        "a": sorted([Point(3, 1), Point(0, 2), Point(2, 6), Point(6, 7)])
    }


def test_antinodes_can_be_computed_for_multiple_antenna_types():
    """
    ......#....#
    ...#....0...
    ....#O....#.
    ..#....0....
    ....0....#..
    .#....A.....
    ...#........
    #......#....
    ........A...
    .........A..
    ..........#.
    ..........#.

    (Plus the topmost A-frequency antenna overlaps with a 0-frequency antinode)
    (3, 1) is an antinode for both for A and 0
    """
    assert MAP.compute_antinodes() == {
        "A": sorted(
            [
                Point(3, 1),
                Point(4, 2),
                Point(7, 7),
                Point(10, 10),
                Point(10, 11),
            ]
        ),
        "0": sorted(
            [
                Point(6, 0),
                Point(11, 0),
                Point(3, 1),
                Point(10, 2),
                Point(2, 3),
                Point(9, 4),
                Point(1, 5),
                Point(6, 5),
                Point(3, 6),
                Point(0, 7),
            ]
        ),
    }


def test_solution_can_be_computed():
    assert compute_solution(MAP) == 14
