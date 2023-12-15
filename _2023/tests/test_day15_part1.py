import pytest
from _2023.day15 import compute_hash
from _2023.day15.part1 import compute_solution


@pytest.mark.parametrize(
    "string, expected_hash",
    [
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47),
        ("qp-", 14),
        ("pc=4", 180),
        ("ot=9", 9),
        ("ab=5", 197),
        ("pc-", 48),
        ("pc=6", 214),
        ("ot=7", 231),
    ],
)
def test_hash_can_be_parsed_from_string(string, expected_hash):
    assert compute_hash(string) == expected_hash


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day15")) == 1320
