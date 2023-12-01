import os

from _2021.day3.part2 import keep_only_binaries_by_value_at_index, resolution


def test_list_of_binaries_can_be_filtered_on_bit_value_at_index():
    binaries_filtered = keep_only_binaries_by_value_at_index(
        ["00100", "11110", "10110", "10111", "10101"], value="1", index=3
    )

    assert binaries_filtered == ["11110", "10110", "10111"]


def test_puzzle_is_resolved():
    result = resolution(os.path.join("data", "test_file_day3"))

    assert result == 230
