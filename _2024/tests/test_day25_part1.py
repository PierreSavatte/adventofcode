from _2024.day25 import LocksAndKeys, Lockset, parse_input
from _2024.day25.part1 import compute_solution

TEST_INPUT = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

LOCKSANDKEYS = LocksAndKeys(
    keys=[
        (5, 0, 2, 1, 3),
        (4, 3, 4, 0, 2),
        (3, 0, 2, 0, 1),
    ],
    locks=[
        (0, 5, 3, 4, 3),
        (1, 2, 0, 5, 3),
    ],
)


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == LOCKSANDKEYS


def test_fitting_locksets_can_be_computed():
    assert LOCKSANDKEYS.compute_fitting() == [
        Lockset(lock=(0, 5, 3, 4, 3), key=(3, 0, 2, 0, 1)),
        Lockset(lock=(1, 2, 0, 5, 3), key=(4, 3, 4, 0, 2)),
        Lockset(lock=(1, 2, 0, 5, 3), key=(3, 0, 2, 0, 1)),
    ]


def test_solution_can_be_computed():
    assert compute_solution(LOCKSANDKEYS) == 3
