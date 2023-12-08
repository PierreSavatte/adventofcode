import pytest

from _2023.day8 import parse_input, Node
from _2023.day8.part1 import compute_solution


def test_input_can_be_parsed_as_tree(get_data):
    map = parse_input(get_data("test_file_day8"))

    assert map.instructions == "RL"
    tree = map.tree
    assert tree == {
        "AAA": Node(L="BBB", R="CCC"),
        "BBB": Node(L="DDD", R="EEE"),
        "CCC": Node(L="ZZZ", R="GGG"),
        "DDD": Node(L="DDD", R="DDD"),
        "EEE": Node(L="EEE", R="EEE"),
        "GGG": Node(L="GGG", R="GGG"),
        "ZZZ": Node(L="ZZZ", R="ZZZ"),
    }


@pytest.mark.parametrize(
    "data, expected_solution",
    [
        (
            """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""",
            2,
        ),
        (
            """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""",
            6,
        ),
    ],
)
def test_solution_can_be_computed(data, expected_solution):
    assert compute_solution(data) == expected_solution
