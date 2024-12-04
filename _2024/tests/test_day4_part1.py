import pytest
from _2024.day4 import get_windows, parse_input
from _2024.day4.part1 import (
    compute_solution,
    compute_xmax_number_in_diagonals,
    compute_xmax_number_in_rows,
    transpose,
)

TEST_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]


def test_grid_can_be_transposed():
    grid = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    transposed_grid = [
        "MMAMXXSSMM",
        "MSMSMXMAAX",
        "MAXAAASXMM",
        "SMSMSMMAMX",
        "XXXAAMSMMA",
        "XMMSMXAAXX",
        "MSAMXXSSMM",
        "AMASAAXAMA",
        "SSMMMMSAMS",
        "MAMXMASAMX",
    ]

    assert transpose(grid) == transposed_grid


def test_search_windows_can_be_computed():
    windows = get_windows(
        [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
    )

    assert next(windows) == [
        "MMMS",
        "MSAM",
        "AMXS",
        "MSAM",
    ]
    assert next(windows) == [
        "MMSX",
        "SAMX",
        "MXSX",
        "SAMA",
    ]
    assert next(windows) == [
        "MSXX",
        "AMXM",
        "XSXM",
        "AMAS",
    ]
    assert next(windows) == [
        "SXXM",
        "MXMS",
        "SXMA",
        "MASM",
    ]
    next(windows)
    next(windows)
    next(windows)
    assert next(windows) == [
        "MSAM",
        "AMXS",
        "MSAM",
        "XMAS",
    ]

    last_window = None
    try:
        while 1:
            last_window = next(windows)
    except StopIteration:
        pass

    assert last_window
    assert last_window == [
        "SXSS",
        "SAAA",
        "MMMM",
        "MASX",
    ]


@pytest.mark.parametrize(
    "window",
    [
        [
            "X...",
            ".M..",
            "..A.",
            "...S",
        ],
        [
            "...X",
            "..M.",
            ".A..",
            "S...",
        ],
        [
            "S...",
            ".A..",
            "..M.",
            "...X",
        ],
        [
            "...S",
            "..A.",
            ".M..",
            "X...",
        ],
        # Only counting diagonals
        [
            "S..S",
            "AA.A",
            "M.MM",
            "X..X",
        ],
    ],
)
def test_number_of_xmas_can_be_counted_in_diagonals(window):
    assert compute_xmax_number_in_diagonals(window) == 1


@pytest.mark.parametrize(
    "window, expected_number",
    [
        (
            [
                "S..S",
                "AA.A",
                "M.MM",
                "X..X",
            ],
            1,
        ),
        (
            [
                "S..S",
                "AAAA",
                "MMMM",
                "X..X",
            ],
            2,
        ),
    ],
)
def test_multiple_diagonal_xmas_can_be_counted_in_the_same_window(
    window, expected_number
):
    assert compute_xmax_number_in_diagonals(window) == expected_number


@pytest.mark.parametrize(
    "window",
    [
        [
            "XMAS",
            "....",
            "....",
            "....",
        ],
        [
            "....",
            "XMAS",
            "....",
            "....",
        ],
        [
            "....",
            "....",
            "XMAS",
            "....",
        ],
        [
            "....",
            "....",
            "....",
            "XMAS",
        ],
        [
            "SAMX",
            "....",
            "....",
            "....",
        ],
        [
            "....",
            "SAMX",
            "....",
            "....",
        ],
        [
            "....",
            "....",
            "SAMX",
            "....",
        ],
        [
            "....",
            "....",
            "....",
            "SAMX",
        ],
    ],
)
def test_xmas_can_be_counted_in_rows(window):
    assert compute_xmax_number_in_rows(window) == 1


def test_solution_can_be_computed():
    assert (
        compute_solution(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )
        == 18
    )
