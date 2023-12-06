import pytest

from _2023.day6 import Race, Option
from _2023.day6.part1 import compute_solution, parse_input


def test_input_can_be_parsed(get_data):
    races = parse_input(data=get_data("test_file_day6"))
    assert races == [
        Race(time=7, min_distance=9),
        Race(time=15, min_distance=40),
        Race(time=30, min_distance=200),
    ]


@pytest.mark.parametrize(
    "race, expected_options",
    [
        [
            Race(time=7, min_distance=9),
            [Option(holding_for=option) for option in range(2, 5 + 1)],
        ],
        [
            Race(time=15, min_distance=40),
            [Option(holding_for=option) for option in range(4, 11 + 1)],
        ],
        [
            Race(time=30, min_distance=200),
            [Option(holding_for=option) for option in range(11, 19 + 1)],
        ],
    ],
)
def test_winning_options_can_be_computed(race, expected_options):
    assert race.compute_winning_options() == expected_options


def test_solution_can_be_computed(get_data):
    assert compute_solution(data=get_data("test_file_day6")) == 288
