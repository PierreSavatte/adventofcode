import pytest
from _2023.day9 import Sequence
from _2023.day9.part2 import compute_solution


@pytest.mark.parametrize(
    "sequence, expected_previous_value",
    [
        (Sequence([0, 3, 6, 9, 12, 15]), -3),
        (Sequence([1, 3, 6, 10, 15, 21]), 0),
        (Sequence([10, 13, 16, 21, 30, 45]), 5),
    ],
)
def test_next_value_in_sequence_can_be_computed(
    sequence, expected_previous_value
):
    assert sequence.get_previous_value() == expected_previous_value


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day9")) == 2
