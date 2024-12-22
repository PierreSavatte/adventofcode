import pytest
from _2024.day22 import (
    generate_next_secret_number,
    get_nth_secret_number,
    mix,
    prune,
)
from _2024.day22.part1 import compute_solution


def test_values_can_be_mixed():
    assert mix(42, 15) == 37


def test_values_can_be_pruned():
    assert prune(100000000) == 16113920


@pytest.mark.parametrize(
    "previous, next",
    [
        (123, 15887950),
        (15887950, 16495136),
        (16495136, 527345),
        (527345, 704524),
        (704524, 1553684),
        (1553684, 12683156),
        (12683156, 11100544),
        (11100544, 12249484),
        (12249484, 7753432),
        (7753432, 5908254),
    ],
)
def test_next_secret_number_can_be_generated(previous, next):
    assert generate_next_secret_number(previous) == next


@pytest.mark.parametrize(
    "secret_number, result",
    [
        (1, 8685429),
        (10, 4700978),
        (100, 15273692),
        (2024, 8667524),
    ],
)
def test_get_nth_secret_number(secret_number, result):
    assert get_nth_secret_number(secret_number=secret_number, n=2000) == result


def test_solution_can_be_computed():
    assert compute_solution([1, 10, 100, 2024]) == 37327623
