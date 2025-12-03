import pytest
from _2025.day3.part2 import LargeBanks


@pytest.mark.parametrize(
    "batteries, expected_result",
    [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ],
)
def test_largest_joltage_can_be_found(batteries, expected_result):
    banks = LargeBanks()
    assert banks.get_bank_max_joltage(batteries) == expected_result
