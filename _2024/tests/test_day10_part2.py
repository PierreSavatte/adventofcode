import pytest
from _2024.day10.part2 import (
    HikingTrail,
    compute_all_hiking_trails,
    compute_solution,
    get_trailhead_rating,
)

MAP_1 = [
    # single trailhead with rating 3
    # .....0.
    # ..4321.
    # ..5..2.
    # ..6543.
    # ..7..4.
    # ..8765.
    # ..9....
    [2, 2, 2, 2, 2, 0, 2],
    [2, 2, 4, 3, 2, 1, 2],
    [2, 2, 5, 2, 2, 2, 2],
    [2, 2, 6, 5, 4, 3, 2],
    [2, 2, 7, 2, 2, 4, 2],
    [2, 2, 8, 7, 6, 5, 2],
    [2, 2, 9, 2, 2, 2, 2],
]

MAP_2 = [
    # single trailhead with rating 13
    # ..90..9
    # ...1.98
    # ...2..7
    # 6543456
    # 765.987
    # 876....
    # 987....
    [1, 1, 9, 0, 1, 1, 9],
    [1, 1, 1, 1, 1, 9, 8],
    [1, 1, 1, 2, 1, 1, 7],
    [6, 5, 4, 3, 4, 5, 6],
    [7, 6, 5, 1, 9, 8, 7],
    [8, 7, 6, 1, 1, 1, 1],
    [9, 8, 7, 1, 1, 1, 1],
]

MAP_3 = [
    # single trailhead with rating 227 :
    #   - 121 distinct hiking trails that lead to the 9 on the right edge
    #   - 106 that lead to the 9 on the bottom edge
    # 012345
    # 123456
    # 234567
    # 345678
    # 4.6789
    # 56789.
    [0, 1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8],
    [4, 1, 6, 7, 8, 9],
    [5, 6, 7, 8, 9, 1],
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


def test_all_hiking_trail_can_be_computed():
    assert compute_all_hiking_trails(MAP_1) == [
        HikingTrail(
            positions=[
                (5, 0),
                (5, 1),
                (4, 1),
                (3, 1),
                (2, 1),
                (2, 2),
                (2, 3),
                (2, 4),
                (2, 5),
                (2, 6),
            ]
        ),
        HikingTrail(
            positions=[
                (5, 0),
                (5, 1),
                (5, 2),
                (5, 3),
                (4, 3),
                (3, 3),
                (2, 3),
                (2, 4),
                (2, 5),
                (2, 6),
            ]
        ),
        HikingTrail(
            positions=[
                (5, 0),
                (5, 1),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 5),
                (4, 5),
                (3, 5),
                (2, 5),
                (2, 6),
            ]
        ),
    ]


@pytest.mark.parametrize(
    "map, trailheads_with_their_rating",
    [
        (MAP_1, {(5, 0): 3}),
        (MAP_2, {(3, 0): 13}),
        (MAP_3, {(0, 0): 227}),
        (
            MAP_4,
            {
                (2, 0): 20,
                (4, 0): 24,
                (4, 2): 10,
                (6, 4): 4,
                (2, 5): 1,
                (5, 5): 4,
                (0, 6): 5,
                (6, 6): 8,
                (1, 7): 5,
            },
        ),
    ],
)
def test_trailhead_rating_can_be_computed(map, trailheads_with_their_rating):
    total_expected_hiking_trails = sum(trailheads_with_their_rating.values())

    hiking_trails = compute_all_hiking_trails(map)

    actuals = {}
    for trailhead, rating in trailheads_with_their_rating.items():
        actuals[trailhead] = get_trailhead_rating(trailhead, hiking_trails)

    assert actuals == trailheads_with_their_rating
    assert len(hiking_trails) == total_expected_hiking_trails


def test_solution_can_be_computed():
    assert compute_solution(MAP_4) == 81
