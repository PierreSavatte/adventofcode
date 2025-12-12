import pytest
from _2025.day8 import Playground, Position, compute_distance


@pytest.fixture
def input() -> str:
    return """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


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


def test_input_can_be_parsed(input, playground):
    assert Playground.from_input(input) == playground


def test_distance_can_be_computed():
    assert (
        compute_distance(Position(52, 470, 668), Position(739, 650, 466))
        == 738.3583140995976
    )


def test_connections_can_be_made(playground):
    playground.make_next_connection()
    assert playground.groups == [
        {Position(162, 817, 812), Position(425, 690, 689)},
        {Position(57, 618, 57)},
        {Position(906, 360, 560)},
        {Position(592, 479, 940)},
        {Position(352, 342, 300)},
        {Position(466, 668, 158)},
        {Position(542, 29, 236)},
        {Position(431, 825, 988)},
        {Position(739, 650, 466)},
        {Position(52, 470, 668)},
        {Position(216, 146, 977)},
        {Position(819, 987, 18)},
        {Position(117, 168, 530)},
        {Position(805, 96, 715)},
        {Position(346, 949, 466)},
        {Position(970, 615, 88)},
        {Position(941, 993, 340)},
        {Position(862, 61, 35)},
        {Position(984, 92, 344)},
    ]

    playground.make_next_connection()
    assert playground.groups == [
        {
            Position(162, 817, 812),
            Position(425, 690, 689),
            Position(431, 825, 988),
        },
        {Position(57, 618, 57)},
        {Position(906, 360, 560)},
        {Position(592, 479, 940)},
        {Position(352, 342, 300)},
        {Position(466, 668, 158)},
        {Position(542, 29, 236)},
        {Position(739, 650, 466)},
        {Position(52, 470, 668)},
        {Position(216, 146, 977)},
        {Position(819, 987, 18)},
        {Position(117, 168, 530)},
        {Position(805, 96, 715)},
        {Position(346, 949, 466)},
        {Position(970, 615, 88)},
        {Position(941, 993, 340)},
        {Position(862, 61, 35)},
        {Position(984, 92, 344)},
    ]

    playground.make_next_connection()
    assert playground.groups == [
        {
            Position(162, 817, 812),
            Position(425, 690, 689),
            Position(431, 825, 988),
        },
        {Position(57, 618, 57)},
        {Position(906, 360, 560), Position(805, 96, 715)},
        {Position(592, 479, 940)},
        {Position(352, 342, 300)},
        {Position(466, 668, 158)},
        {Position(542, 29, 236)},
        {Position(739, 650, 466)},
        {Position(52, 470, 668)},
        {Position(216, 146, 977)},
        {Position(819, 987, 18)},
        {Position(117, 168, 530)},
        {Position(346, 949, 466)},
        {Position(970, 615, 88)},
        {Position(941, 993, 340)},
        {Position(862, 61, 35)},
        {Position(984, 92, 344)},
    ]

    for i in range(7):
        playground.make_next_connection()

    expected_group_sizes = [5, 4, 2, 2, 1, 1, 1, 1, 1, 1, 1]
    assert playground.get_group_sizes() == expected_group_sizes


def test_solution_can_be_computed(playground):
    assert playground.compute_solution(nb_connections=10) == 40
