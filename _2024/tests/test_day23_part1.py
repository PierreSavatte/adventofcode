from _2024.day23 import Computers, one_computer_starts_with_t
from _2024.day23.part1 import compute_solution

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


def test_connected_computer_sets_can_be_computed():
    connected_computer_sets = COMPUTERS.compute_connected_sets()
    assert connected_computer_sets == {
        ("aq", "cg", "yn"),
        ("aq", "vc", "wq"),
        ("co", "de", "ka"),
        ("co", "de", "ta"),
        ("co", "ka", "ta"),
        ("de", "ka", "ta"),
        ("kh", "qp", "ub"),
        ("qp", "td", "wh"),
        ("tb", "vc", "wq"),
        ("tc", "td", "wh"),
        ("td", "wh", "yn"),
        ("ub", "vc", "wq"),
    }


def test_filtered_connected_computer_sets_can_be_computed():
    connected_computer_sets = COMPUTERS.compute_connected_sets(
        filter=one_computer_starts_with_t
    )
    assert connected_computer_sets == {
        ("co", "de", "ta"),
        ("co", "ka", "ta"),
        ("de", "ka", "ta"),
        ("qp", "td", "wh"),
        ("tb", "vc", "wq"),
        ("tc", "td", "wh"),
        ("td", "wh", "yn"),
    }


def test_solution_can_be_computed():
    assert compute_solution(COMPUTERS) == 7
