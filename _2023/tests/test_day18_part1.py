import pytest

from _2023.day18 import DigPlan, Order, Direction, Plan
from _2023.day18.part1 import compute_solution


@pytest.fixture
def dig_plan(get_data) -> DigPlan:
    data = get_data("test_file_day18")
    return DigPlan.from_data(data)


@pytest.fixture
def plan(dig_plan) -> Plan:
    return Plan.from_dig_plan(dig_plan)


def test_input_can_be_parsed(dig_plan):
    assert dig_plan[:3] == [
        Order(direction=Direction.RIGHT, length=6),
        Order(direction=Direction.DOWN, length=5),
        Order(direction=Direction.LEFT, length=2),
    ]


def test_plan_can_be_computed(plan):
    assert plan.loop_positions == [
        (0, 0),
        (6, 0),
        (6, 5),
        (4, 5),
        (4, 7),
        (6, 7),
        (6, 9),
        (1, 9),
        (1, 7),
        (0, 7),
        (0, 5),
        (2, 5),
        (2, 2),
        (0, 2),
        (0, 0),
    ]


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day18")) == 62
