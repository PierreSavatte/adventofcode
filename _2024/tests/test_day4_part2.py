import pytest
from _2024.day4 import get_windows
from _2024.day4.part2 import compute_solution, is_x_mas


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
        ],
        window_size=3,
    )

    assert next(windows) == [
        "MMM",
        "MSA",
        "AMX",
    ]
    assert next(windows) == [
        "MMS",
        "SAM",
        "MXS",
    ]

    last_window = None
    try:
        while 1:
            last_window = next(windows)
    except StopIteration:
        pass

    assert last_window
    assert last_window == [
        "AAA",
        "MMM",
        "ASX",
    ]


@pytest.mark.parametrize(
    "window",
    [
        [
            "M.S",
            ".A.",
            "M.S",
        ],
        [
            "S.M",
            ".A.",
            "S.M",
        ],
        [
            "S.S",
            ".A.",
            "M.M",
        ],
        [
            "M.M",
            ".A.",
            "S.S",
        ],
        [
            "MAS",
            "AAA",
            "MAS",
        ],
        [
            "M8S",
            "8A8",
            "M8S",
        ],
        [
            "S.M",
            ".A.",
            "S.M",
        ],
    ],
)
def test_x_mas_can_be_verified(window):
    assert is_x_mas(window) is True


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
        == 9
    )
