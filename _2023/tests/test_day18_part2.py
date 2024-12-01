import pytest

from _2023.day18 import (
    DigPlan,
    Order,
    Direction,
    Plan,
    parse_hexadecimal,
    Rectangle,
    Position,
)
from _2023.day18.part2 import compute_solution


@pytest.fixture
def dig_plan(get_data) -> DigPlan:
    data = get_data("test_file_day18")
    return DigPlan.from_data(data, large_lagoon=True)


@pytest.fixture
def plan(dig_plan) -> Plan:
    return Plan.from_dig_plan(dig_plan)


@pytest.mark.parametrize(
    "hexadecimal, expected_direction, expected_length",
    [
        ("#70c710", Direction.RIGHT, 461937),
        ("#0dc571", Direction.DOWN, 56407),
        ("#5713f0", Direction.RIGHT, 356671),
        ("#d2c081", Direction.DOWN, 863240),
        ("#59c680", Direction.RIGHT, 367720),
        ("#411b91", Direction.DOWN, 266681),
        ("#8ceee2", Direction.LEFT, 577262),
        ("#caa173", Direction.UP, 829975),
        ("#1b58a2", Direction.LEFT, 112010),
        ("#caa171", Direction.DOWN, 829975),
        ("#7807d2", Direction.LEFT, 491645),
        ("#a77fa3", Direction.UP, 686074),
        ("#015232", Direction.LEFT, 5411),
        ("#7a21e3", Direction.UP, 500254),
    ],
)
def test_hexadecimal_can_be_parsed(
    hexadecimal, expected_direction, expected_length
):
    assert parse_hexadecimal(hexadecimal) == (
        expected_direction,
        expected_length,
    )


def test_input_can_be_parsed(dig_plan):
    assert dig_plan[:3] == [
        Order(direction=Direction.RIGHT, length=461937),
        Order(direction=Direction.DOWN, length=56407),
        Order(direction=Direction.RIGHT, length=356671),
    ]


def test_minimal_rectangles_can_be_computed():
    """
    .#...#.
    .......
    ##...##
    .......
    #.#....
    ..#...#

    Rectangles:

    - [(1, 0), (5, 1)]
    - [(0, 2), (6, 4)]
    - [(2, 5), (6, 5)]
    """
    dig_plan = DigPlan(
        [
            Order(direction=Direction.RIGHT, length=4),
            Order(direction=Direction.DOWN, length=2),
            Order(direction=Direction.RIGHT, length=1),
            Order(direction=Direction.DOWN, length=3),
            Order(direction=Direction.LEFT, length=4),
            Order(direction=Direction.UP, length=1),
            Order(direction=Direction.LEFT, length=2),
            Order(direction=Direction.UP, length=2),
            Order(direction=Direction.RIGHT, length=1),
            Order(direction=Direction.UP, length=2),
        ]
    )

    plan = Plan.from_dig_plan(dig_plan)

    assert plan.compute_min_rectangles() == [
        Rectangle(top_left=Position((1, 0)), bottom_right=Position((5, 1))),
        Rectangle(top_left=Position((0, 2)), bottom_right=Position((6, 4))),
        Rectangle(top_left=Position((2, 5)), bottom_right=Position((6, 5))),
    ]


def test_dug_area_can_be_computed(plan):
    assert plan.compute_area() == 952408144115


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day18")) == 952408144115
