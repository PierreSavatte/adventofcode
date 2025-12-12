import pytest
from _2025.day8 import Position
from _2025.day8.part2 import Playground


@pytest.fixture
def playground() -> Playground:
    return Playground(
        positions=[
            Position(162, 817, 812),
            Position(57, 618, 57),
            Position(906, 360, 560),
            Position(592, 479, 940),
            Position(352, 342, 300),
            Position(466, 668, 158),
            Position(542, 29, 236),
            Position(431, 825, 988),
            Position(739, 650, 466),
            Position(52, 470, 668),
            Position(216, 146, 977),
            Position(819, 987, 18),
            Position(117, 168, 530),
            Position(805, 96, 715),
            Position(346, 949, 466),
            Position(970, 615, 88),
            Position(941, 993, 340),
            Position(862, 61, 35),
            Position(984, 92, 344),
            Position(425, 690, 689),
        ]
    )


def test_last_connection_pair_can_be_computed(playground):
    assert playground.get_last_connection_pair() == (
        Position(216, 146, 977),
        Position(117, 168, 530),
    )


def test_solution_can_be_computed(playground):
    assert playground.compute_solution() == 25272
