from _2025.day4 import Map
from _2025.day4.part2 import compute_solution

INPUT = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_solution_can_be_computed():
    assert compute_solution(Map(INPUT)) == 43
