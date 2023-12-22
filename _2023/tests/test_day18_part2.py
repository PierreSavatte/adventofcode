import pytest

from _2023.day18 import DigPlan, Order, Direction, Plan, parse_hexadecimal
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


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day18")) == 952408144115
