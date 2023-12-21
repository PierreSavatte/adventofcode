import pytest

from _2023.day17 import Map, build_solution_tiles, CrucibleType
from _2023.day17.part2 import compute_solution
from _2023.day17.pathfinding import a_star

EXPECTED_SHORTEST_PATH_FOR_PART1 = """2>>>>>>>>1323
32154535v5623
32552456v4254
34465858v5452
45466578v>>>>
143859879845v
445787698776v
363787797965v
465496798688v
456467998645v
122468686556v
254654888773v
432267465553v"""

EXPECTED_SHORTEST_PATH_FOR_PART2 = """1>>>>>>>>>11
999999999v91
999999999v91
999999999v91
999999999v>>"""


@pytest.mark.parametrize(
    "data_filename, expected_path",
    [
        ("test_file_day17_part1", EXPECTED_SHORTEST_PATH_FOR_PART1),
        ("test_file_day17_part2", EXPECTED_SHORTEST_PATH_FOR_PART2),
    ],
)
def test_shortest_path_can_be_computed(get_data, data_filename, expected_path):
    map = Map.from_data(
        get_data(data_filename), crucible_type=CrucibleType.ULTRA
    )
    shortest_route = a_star(map=map)

    assert build_solution_tiles(map, shortest_route) == expected_path


@pytest.mark.parametrize(
    "data_filename, expected_result",
    [
        ("test_file_day17_part1", 94),
        ("test_file_day17_part2", 55),
    ],
)
def test_solution_can_be_computed(get_data, data_filename, expected_result):
    assert compute_solution(get_data(data_filename)) == expected_result
