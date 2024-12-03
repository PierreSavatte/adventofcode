from _2024.day3.part2 import remove_ignored_part_of_input

TEST_INPUT = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def test_part_of_input_can_be_removed():
    assert (
        remove_ignored_part_of_input(TEST_INPUT)
        == "xmul(2,4)&mul[3,7]!^?mul(8,5))"  # noqa: E501
    )
