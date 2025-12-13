import pytest
from _2025.day9 import compute_area, find_largest_rectangle, parse_input

INPUT = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
TEST_DATA = [
    (7, 1),
    (11, 1),
    (11, 7),
    (9, 7),
    (9, 5),
    (2, 5),
    (2, 3),
    (7, 3),
]


def test_input_can_be_parsed():
    assert parse_input(INPUT) == TEST_DATA


def test_largest_rectangle_can_be_found_in_positions_list():
    assert find_largest_rectangle(TEST_DATA) == ((2, 5), (11, 1))


@pytest.mark.parametrize(
    "a, b, expected_area",
    [
        ((2, 5), (11, 1), 50),
        ((7, 3), (2, 3), 6),
        ((7, 1), (11, 7), 35),
        ((2, 5), (9, 7), 24),
    ],
)
def test_area_can_be_computed(a, b, expected_area):
    assert compute_area(a, b) == expected_area
