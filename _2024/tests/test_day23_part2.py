from _2024.day23 import Computers
from _2024.day23.part2 import compute_solution

COMPUTERS = Computers(
    [
        ("kh", "tc"),
        ("qp", "kh"),
        ("de", "cg"),
        ("ka", "co"),
        ("yn", "aq"),
        ("qp", "ub"),
        ("cg", "tb"),
        ("vc", "aq"),
        ("tb", "ka"),
        ("wh", "tc"),
        ("yn", "cg"),
        ("kh", "ub"),
        ("ta", "co"),
        ("de", "co"),
        ("tc", "td"),
        ("tb", "wq"),
        ("wh", "td"),
        ("ta", "ka"),
        ("td", "qp"),
        ("aq", "cg"),
        ("wq", "ub"),
        ("ub", "vc"),
        ("de", "ta"),
        ("wq", "aq"),
        ("wq", "vc"),
        ("wh", "yn"),
        ("ka", "de"),
        ("kh", "ta"),
        ("co", "tc"),
        ("wh", "qp"),
        ("tb", "vc"),
        ("td", "yn"),
    ]
)


def test_largest_of_interconnected_computers_can_be_computed():
    assert COMPUTERS.get_largest_interconnected_set() == (
        "co",
        "de",
        "ka",
        "ta",
    )


def test_solution_can_be_computed():
    assert compute_solution(COMPUTERS) == "co,de,ka,ta"
