import pytest
from _2024.day3.part2 import remove_ignored_part_of_input


@pytest.mark.parametrize(
    "data, expected_output",
    [
        (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
            "xmul(2,4)&mul[3,7]!^?mul(8,5))",
        ),
        (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)do()+mul(32,64](mul(11,8)don't()undo()?mul(8,5))",
            "xmul(2,4)&mul[3,7]!^+mul(32,64](mul(11,8)?mul(8,5))",
        ),
        (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)do()+mul(32,64](mul(11,8)don't()mul(32,64)undo()?don't()mul(8,5))",
            "xmul(2,4)&mul[3,7]!^+mul(32,64](mul(11,8)?",
        ),
        (
            "xmul(2,4)&mul[3,7]!^_don't()mul(5,5)do()+mul(32,64](mul(11,8)un?mul(8,5)don't())",
            "xmul(2,4)&mul[3,7]!^_+mul(32,64](mul(11,8)un?mul(8,5)",
        ),
        (
            "mul(1,1)don't()mul(2,2)do()mul(3,3)do()don't()mul(4,4)don't()mul(5,5)do()mul(6,6)don't()mul(7,7)",
            "mul(1,1)mul(3,3)do()mul(6,6)",
        ),
    ],
)
def test_part_of_input_can_be_removed(data, expected_output):
    assert remove_ignored_part_of_input(data) == expected_output  # noqa: E501
