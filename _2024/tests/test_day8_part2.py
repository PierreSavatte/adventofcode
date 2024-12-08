from _2024.day8 import Map, Point
from _2024.day8.part2 import compute_solution


def test_antinodes_can_be_computed_with_resonance():
    """
    T....#....
    ...T......
    .T....#...
    .........#
    ..#.......
    ..........
    ...#......
    ..........
    ....#.....
    ..........
    """

    map = Map(
        size=10,
        antennas={"T": [Point(0, 0), Point(3, 1), Point(1, 2)]},
    )

    assert map.compute_antinodes_with_resonance() == {
        "T": {
            # antennas
            Point(0, 0),
            Point(3, 1),
            Point(1, 2),
            # antinodes
            Point(5, 0),
            Point(6, 2),
            Point(9, 3),
            Point(2, 4),
            Point(3, 6),
            Point(4, 8),
        }
    }


def test_antinodes_can_be_computed_for_multiple_antenna_types():
    map = Map(
        size=12,
        antennas={
            "A": [Point(6, 5), Point(8, 8), Point(9, 9)],
            "0": [Point(8, 1), Point(5, 2), Point(7, 3), Point(4, 4)],
        },
    )

    assert map.compute_antinodes_with_resonance() == {
        "A": {
            # Antennas
            Point(6, 5),
            Point(8, 8),
            Point(9, 9),
            # Antinodes
            Point(4, 2),
            Point(3, 1),
            Point(10, 11),
            Point(0, 0),
            Point(1, 1),
            Point(2, 2),
            Point(3, 3),
            Point(4, 4),
            Point(5, 5),
            Point(6, 6),
            Point(7, 7),
            Point(10, 10),
            Point(11, 11),
        },
        "0": {
            # Antennas
            Point(8, 1),
            Point(5, 2),
            Point(7, 3),
            Point(4, 4),
            # Antinodes
            Point(1, 0),
            Point(6, 0),
            Point(11, 0),
            Point(3, 1),
            Point(10, 2),
            Point(2, 3),
            Point(9, 4),
            Point(1, 5),
            Point(6, 5),
            Point(11, 5),
            Point(3, 6),
            Point(0, 7),
            Point(5, 7),
            Point(2, 8),
            Point(4, 9),
            Point(1, 10),
            Point(3, 11),
        },
    }


def test_solution_can_be_computed():
    map = Map(
        size=12,
        antennas={
            "A": [Point(6, 5), Point(8, 8), Point(9, 9)],
            "0": [Point(8, 1), Point(5, 2), Point(7, 3), Point(4, 4)],
        },
    )

    assert compute_solution(map) == 34
