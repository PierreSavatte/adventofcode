import pytest
from _2024.day10 import (
    HikingTrail,
    get_neighbors,
    get_trail_destinations,
    get_trailheads,
    parse_input,
)
from _2024.day10.part1 import (
    compute_hiking_trails,
    compute_solution,
    get_trailhead_score,
)

MAP_1 = [
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1],
    [6, 5, 4, 3, 4, 5, 6],
    [7, 1, 1, 1, 1, 1, 7],
    [8, 1, 1, 1, 1, 1, 8],
    [9, 1, 1, 1, 1, 1, 9],
]

MAP_2 = [
    [1, 1, 9, 0, 1, 1, 9],
    [1, 1, 1, 1, 1, 9, 8],
    [1, 1, 1, 2, 1, 1, 7],
    [6, 5, 4, 3, 4, 5, 6],
    [7, 6, 5, 1, 9, 8, 7],
    [8, 7, 6, 1, 1, 1, 1],
    [9, 8, 7, 1, 1, 1, 1],
]

MAP_3 = [
    [1, 0, 1, 1, 9, 1, 1],
    [2, 1, 1, 1, 8, 1, 1],
    [3, 1, 1, 1, 7, 1, 1],
    [4, 5, 6, 7, 6, 5, 4],
    [1, 1, 1, 8, 1, 1, 3],
    [1, 1, 1, 9, 1, 1, 2],
    [1, 1, 1, 1, 1, 0, 1],
]

MAP_4 = [
    [8, 9, 0, 1, 0, 1, 2, 3],
    [7, 8, 1, 2, 1, 8, 7, 4],
    [8, 7, 4, 3, 0, 9, 6, 5],
    [9, 6, 5, 4, 9, 8, 7, 4],
    [4, 5, 6, 7, 8, 9, 0, 3],
    [3, 2, 0, 1, 9, 0, 1, 2],
    [0, 1, 3, 2, 9, 8, 0, 1],
    [1, 0, 4, 5, 6, 7, 3, 2],
]


def test_input_can_be_parsed():
    data = """0123
1234
8765
9876
"""
    assert parse_input(data) == [
        [0, 1, 2, 3],
        [1, 2, 3, 4],
        [8, 7, 6, 5],
        [9, 8, 7, 6],
    ]


@pytest.mark.parametrize(
    "map, trailheads",
    [
        (MAP_1, [(3, 0)]),
        (MAP_2, [(3, 0)]),
        (MAP_3, [(1, 0), (5, 6)]),
        (
            MAP_4,
            [
                (2, 0),
                (4, 0),
                (4, 2),
                (6, 4),
                (2, 5),
                (5, 5),
                (0, 6),
                (6, 6),
                (1, 7),
            ],
        ),
    ],
)
def test_trailhead_can_be_detected(map, trailheads):
    assert get_trailheads(map) == trailheads


@pytest.mark.parametrize(
    "map, trail_destinations",
    [
        (MAP_1, [(0, 6), (6, 6)]),
        (MAP_2, [(2, 0), (6, 0), (5, 1), (4, 4), (0, 6)]),
        (MAP_3, [(4, 0), (3, 5)]),
        (
            MAP_4,
            [
                (1, 0),
                (5, 2),
                (0, 3),
                (4, 3),
                (5, 4),
                (4, 5),
                (4, 6),
            ],
        ),
    ],
)
def test_trail_destinations_can_be_detected(map, trail_destinations):
    assert get_trail_destinations(map) == trail_destinations


@pytest.mark.parametrize(
    "map, neighbors",
    [
        (
            [
                [1, 2, 3],
                [1, 2, 3],
                [1, 4, 3],
            ],
            [(2, 1)],
        ),
        (
            [
                [1, 2, 1],
                [4, 3, 4],
                [5, 1, 9],
            ],
            [(2, 1), (0, 1)],
        ),
    ],
)
def test_neighbors_can_be_computed_for_a_position(map, neighbors):
    position = (1, 1)
    assert get_neighbors(map, position) == neighbors


@pytest.mark.parametrize(
    "map, hiking_trails",
    [
        (
            MAP_1,
            [
                HikingTrail(
                    positions=[
                        (3, 0),
                        (3, 1),
                        (3, 2),
                        (3, 3),
                        (2, 3),
                        (1, 3),
                        (0, 3),
                        (0, 4),
                        (0, 5),
                        (0, 6),
                    ]
                ),
                HikingTrail(
                    positions=[
                        (3, 0),
                        (3, 1),
                        (3, 2),
                        (3, 3),
                        (4, 3),
                        (5, 3),
                        (6, 3),
                        (6, 4),
                        (6, 5),
                        (6, 6),
                    ]
                ),
            ],
        ),
        (
            MAP_2,
            [
                HikingTrail(
                    positions=[
                        (3, 0),
                        (3, 1),
                        (3, 2),
                        (3, 3),
                        (4, 3),
                        (5, 3),
                        (6, 3),
                        (6, 2),
                        (6, 1),
                        (6, 0),
                    ]
                ),
                HikingTrail(
                    positions=[
                        (3, 0),
                        (3, 1),
                        (3, 2),
                        (3, 3),
                        (4, 3),
                        (5, 3),
                        (6, 3),
                        (6, 2),
                        (6, 1),
                        (5, 1),
                    ]
                ),
                HikingTrail(
                    positions=[
                        (3, 0),
                        (3, 1),
                        (3, 2),
                        (3, 3),
                        (4, 3),
                        (5, 3),
                        (6, 3),
                        (6, 4),
                        (5, 4),
                        (4, 4),
                    ]
                ),
                HikingTrail(
                    positions=[
                        (3, 0),
                        (3, 1),
                        (3, 2),
                        (3, 3),
                        (2, 3),
                        (2, 4),
                        (2, 5),
                        (1, 5),
                        (0, 5),
                        (0, 6),
                    ]
                ),
            ],
        ),
    ],
)
def test_hiking_trail_can_be_computed(map, hiking_trails):
    assert compute_hiking_trails(map) == hiking_trails


def test_trailhead_score_can_be_computed():
    trailhead = (3, 0)
    hiking_trails = [
        HikingTrail(
            positions=[
                (3, 0),
                (3, 1),
                (3, 2),
                (3, 3),
                (4, 3),
                (5, 3),
                (6, 3),
                (6, 2),
                (6, 1),
                (6, 0),
            ]
        ),
        HikingTrail(
            positions=[
                (3, 0),
                (3, 1),
                (3, 2),
                (3, 3),
                (4, 3),
                (5, 3),
                (6, 3),
                (6, 2),
                (6, 1),
                (5, 1),
            ]
        ),
        HikingTrail(
            positions=[
                (3, 0),
                (3, 1),
                (3, 2),
                (3, 3),
                (4, 3),
                (5, 3),
                (6, 3),
                (6, 4),
                (5, 4),
                (4, 4),
            ]
        ),
        HikingTrail(
            positions=[
                (3, 0),
                (3, 1),
                (3, 2),
                (3, 3),
                (2, 3),
                (2, 4),
                (2, 5),
                (1, 5),
                (0, 5),
                (0, 6),
            ]
        ),
    ]

    assert get_trailhead_score(trailhead, hiking_trails) == 4


def test_solution_can_be_computed():
    assert compute_solution(MAP_4) == 36
