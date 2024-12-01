import pytest

from _2024.day1.part2 import (
    get_similarity_increase,
    compute_similarity_score,
)

LIST_A = [3, 4, 2, 1, 3, 3]
LIST_B = [4, 3, 5, 3, 9, 3]


@pytest.mark.parametrize(
    "a, expected_value",
    [
        (3, 9),
        (4, 4),
        (2, 0),
        (1, 0),
    ],
)
def test_number_of_appearance_can_be_computed(a, expected_value):
    assert get_similarity_increase(a, LIST_B) == expected_value


def test_total_distance_can_be_computed():
    assert (
        compute_similarity_score([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 31
    )
