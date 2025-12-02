import pytest
from _2025.day2 import compute_invalid_ids_sum, is_invalid_id, parse_id_ranges

TEST_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""


def test_id_ranges_can_be_parsed():
    assert parse_id_ranges(TEST_INPUT) == [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]


@pytest.mark.parametrize(
    "id, expected_result",
    [
        (11, True),
        (15, False),
        (22, True),
        (1010, True),
        (1188511885, True),
        (222222, True),
        (446446, True),
        (38593859, True),
    ],
)
def test_invalid_id_can_be_detected(id, expected_result):
    assert is_invalid_id(id) == expected_result


def test_invalid_ids_sum_can_be_computed():
    assert (
        compute_invalid_ids_sum(
            [
                (11, 22),
                (95, 115),
                (998, 1012),
                (1188511880, 1188511890),
                (222220, 222224),
                (1698522, 1698528),
                (446443, 446449),
                (38593856, 38593862),
                (565653, 565659),
                (824824821, 824824827),
                (2121212118, 2121212124),
            ]
        )
        == 1227775554
    )
