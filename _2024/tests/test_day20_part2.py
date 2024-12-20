import pytest
from _2024.day20 import Map, compute_shortcuts, get_intermediary_positions
from _2024.day20.part2 import compute_solution

MAP = Map(
    start=(1, 3),
    end=(5, 7),
    cells=[
        "###############",
        "#...#...#.....#",
        "#.#.#.#.#.###.#",
        "#.#...#.#.#...#",
        "#######.#.#.###",
        "#######.#.#...#",
        "#######.#.###.#",
        "###...#...#...#",
        "###.#######.###",
        "#...###...#...#",
        "#.#####.#.###.#",
        "#.#...#.#.#...#",
        "#.#.#.#.#.#.###",
        "#...#...#...###",
        "###############",
    ],
)
PATH = [
    (1, 3),
    (1, 2),
    (1, 1),
    (2, 1),
    (3, 1),
    (3, 2),
    (3, 3),
    (4, 3),
    (5, 3),
    (5, 2),
    (5, 1),
    (6, 1),
    (7, 1),
    (7, 2),
    (7, 3),
    (7, 4),
    (7, 5),
    (7, 6),
    (7, 7),
    (8, 7),
    (9, 7),
    (9, 6),
    (9, 5),
    (9, 4),
    (9, 3),
    (9, 2),
    (9, 1),
    (10, 1),
    (11, 1),
    (12, 1),
    (13, 1),
    (13, 2),
    (13, 3),
    (12, 3),
    (11, 3),
    (11, 4),
    (11, 5),
    (12, 5),
    (13, 5),
    (13, 6),
    (13, 7),
    (12, 7),
    (11, 7),
    (11, 8),
    (11, 9),
    (12, 9),
    (13, 9),
    (13, 10),
    (13, 11),
    (12, 11),
    (11, 11),
    (11, 12),
    (11, 13),
    (10, 13),
    (9, 13),
    (9, 12),
    (9, 11),
    (9, 10),
    (9, 9),
    (8, 9),
    (7, 9),
    (7, 10),
    (7, 11),
    (7, 12),
    (7, 13),
    (6, 13),
    (5, 13),
    (5, 12),
    (5, 11),
    (4, 11),
    (3, 11),
    (3, 12),
    (3, 13),
    (2, 13),
    (1, 13),
    (1, 12),
    (1, 11),
    (1, 10),
    (1, 9),
    (2, 9),
    (3, 9),
    (3, 8),
    (3, 7),
    (4, 7),
    (5, 7),
]


@pytest.mark.parametrize(
    "a, b, intermediary_positions",
    [
        ((0, 0), (0, 0), []),
        ((0, 0), (3, 3), [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]),
        ((3, 3), (0, 0), [(2, 3), (1, 3), (0, 3), (0, 2), (0, 1)]),
        ((3, 0), (0, 3), [(2, 0), (1, 0), (0, 0), (0, 1), (0, 2)]),
        ((1, 3), (3, 3), [(2, 3)]),
    ],
)
def test_intermediary_positions_can_be_computed(a, b, intermediary_positions):
    assert get_intermediary_positions(a, b) == intermediary_positions


def test_shortcuts_can_be_computed():
    shortcuts = compute_shortcuts(
        PATH, min_time_saved=50, max_shortcut_size=20
    )

    expected_over_50_shortcuts = {
        50: 32,
        52: 31,
        54: 29,
        56: 39,
        58: 25,
        60: 23,
        62: 20,
        64: 19,
        66: 12,
        68: 14,
        70: 12,
        72: 22,
        74: 4,
        76: 3,
    }
    assert sum(shortcuts.values()) == sum(expected_over_50_shortcuts.values())
    assert shortcuts == expected_over_50_shortcuts


def test_solution_can_be_computed():
    assert compute_solution(MAP, min_save=70) == 41
