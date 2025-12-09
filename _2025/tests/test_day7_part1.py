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

EXPECTED_OUTPUT_MAP = """.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|
"""


def test_diagram_can_be_parsed():
    assert parse_diagram(TEST_INPUT) == TEST_DIAGRAM


@pytest.mark.parametrize(
    "diagram, expected_beam",
    [
        # .S.
        # .|.
        # .^.
        # ...
        # ...
        (
            Diagram(
                width=3,
                height=5,
                spawn=Position((1, 0)),
                splitters=[Position((1, 2))],
            ),
            Beam(
                positions=[Position((1, 0)), Position((1, 1))],
                splitter_hit=Position((1, 2)),
            ),
        ),
        # .S.
        # .|.
        # .|.
        # .|.
        # .|.
        (
            Diagram(
                width=3,
                height=5,
                spawn=Position((1, 0)),
                splitters=[],
            ),
            Beam(
                positions=[
                    Position((1, 0)),
                    Position((1, 1)),
                    Position((1, 2)),
                    Position((1, 3)),
                    Position((1, 4)),
                ],
                splitter_hit=None,
            ),
        ),
    ],
)
def test_beam_can_be_generated(diagram, expected_beam):
    assert diagram.generate_beam(diagram.spawn) == expected_beam


def test_position_can_be_split():
    position = Position((2, 0))
    assert position.split() == [Position((1, 0)), Position((3, 0))]


@pytest.mark.parametrize(
    "a, b, expected_equality",
    [
        (
            # ..S..
            # .|^|.
            # .|.|.
            Beam(
                positions=[
                    Position((1, 1)),
                    Position((1, 2)),
                ],
                splitter_hit=None,
            ),
            Beam(
                positions=[
                    Position((3, 1)),
                    Position((3, 2)),
                ],
                splitter_hit=None,
            ),
            False,
        ),
        (
            # .S.
            # .^A
            # ..|
            # .S|
            # .^B
            # ..|
            Beam(
                positions=[
                    Position((2, 1)),
                    Position((2, 2)),
                    Position((2, 3)),
                    Position((2, 4)),
                    Position((2, 5)),
                ],
                splitter_hit=None,
            ),
            Beam(
                positions=[
                    Position((2, 4)),
                    Position((2, 5)),
                ],
                splitter_hit=None,
            ),
            True,
        ),
    ],
)
def test_beams_equality_can_be_checked(a, b, expected_equality):
    assert (a == b) is expected_equality


def test_beam_map_can_be_exported():
    assert TEST_DIAGRAM.export_output_map() == EXPECTED_OUTPUT_MAP


def test_total_beam_count_can_be_performed():
    assert TEST_DIAGRAM.count_beams_that_has_split() == 21
