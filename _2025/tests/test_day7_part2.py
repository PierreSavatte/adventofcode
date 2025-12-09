import pytest
from _2025.day7 import Beam, Diagram, Position, parse_diagram

TEST_INPUT = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

TEST_DIAGRAM = Diagram(
    width=15,
    height=16,
    spawn=Position((7, 0)),
    splitters=[
        Position((7, 2)),
        Position((6, 4)),
        Position((8, 4)),
        Position((5, 6)),
        Position((7, 6)),
        Position((9, 6)),
        Position((4, 8)),
        Position((6, 8)),
        Position((10, 8)),
        Position((3, 10)),
        Position((5, 10)),
        Position((9, 10)),
        Position((11, 10)),
        Position((2, 12)),
        Position((6, 12)),
        Position((12, 12)),
        Position((1, 14)),
        Position((3, 14)),
        Position((5, 14)),
        Position((7, 14)),
        Position((9, 14)),
        Position((13, 14)),
    ],
)


def test_total_beam_count_can_be_performed():
    assert TEST_DIAGRAM.count_total_beams_that_reached_the_bottom() == 40
