import pytest
from _2023.day9 import Sequence
from _2023.day9.part1 import compute_solution


@pytest.mark.parametrize(
    "sequence, expected_differences",
    [
        (
            Sequence([0, 3, 6, 9, 12, 15]),
            {
                0: [0, 3, 6, 9, 12, 15],
                1: [3, 3, 3, 3, 3],
                2: [0, 0, 0, 0],
            },
        ),
        (
            Sequence([1, 3, 6, 10, 15, 21]),
            {
                0: [1, 3, 6, 10, 15, 21],
                1: [2, 3, 4, 5, 6],
                2: [1, 1, 1, 1],
                3: [0, 0, 0],
            },
        ),
        (
            Sequence([10, 13, 16, 21, 30, 45]),
            {
                0: [10, 13, 16, 21, 30, 45],
                1: [3, 3, 5, 9, 15],
                2: [0, 2, 4, 6],
                3: [2, 2, 2],
                4: [0, 0],
            },
        ),
    ],
)
def test_differences_can_be_computed(sequence, expected_differences):
    assert sequence.compute_differences() == expected_differences


@pytest.mark.parametrize(
    "sequence, expected_next_value",
    [
        (Sequence([0, 3, 6, 9, 12, 15]), 18),
        (Sequence([1, 3, 6, 10, 15, 21]), 28),
        (Sequence([10, 13, 16, 21, 30, 45]), 68),
    ],
)
def test_next_value_in_sequence_can_be_computed(sequence, expected_next_value):
    assert sequence.get_next_value() == expected_next_value


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day9")) == 114
