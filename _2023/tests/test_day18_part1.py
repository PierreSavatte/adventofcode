import pytest

from _2023.day18 import DigPlan, Order, Direction, Plan

EXPECTED_PLAN = """#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######"""


EXPECTED_FULLY_DUG_PLAN = """#######
#######
#######
..#####
..#####
#######
#####..
#######
.######
.######"""


@pytest.fixture
def dig_plan(get_data) -> DigPlan:
    data = get_data("test_file_day18")
    return DigPlan.from_data(data)


@pytest.fixture
def plan(dig_plan) -> Plan:
    return Plan.from_dig_plan(dig_plan)


def test_input_can_be_parsed(dig_plan):
    assert dig_plan[:3] == [
        Order(direction=Direction.RIGHT, length=6, color="#70c710"),
        Order(direction=Direction.DOWN, length=5, color="#0dc571"),
        Order(direction=Direction.LEFT, length=2, color="#5713f0"),
    ]


def test_plan_can_be_computed(plan):
    assert plan.dug_cells[:8] == [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (6, 1),
    ]


def test_plan_can_be_output_as_string(plan):
    assert plan.as_string() == EXPECTED_PLAN


def test_enclosing_plan_can_be_computed(plan):
    fully_dug_plan = plan.compute_fully_dug_plan()
    assert fully_dug_plan.as_string() == EXPECTED_FULLY_DUG_PLAN
