import pytest
from _2024.day16 import Map
from _2024.day16.part2 import compute_solution

MAP = Map(
    map=[
        "###############",
        "#.......#.....#",
        "#.#.###.#.###.#",
        "#.....#.#...#.#",
        "#.###.#####.#.#",
        "#.#.#.......#.#",
        "#.#.#####.###.#",
        "#...........#.#",
        "###.#.#####.#.#",
        "#...#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.....#...#.#.#",
        "#.###.#.#.#.#.#",
        "#...#.....#...#",
        "###############",
    ],
    start=(1, 13),
    end=(13, 1),
)
SECOND_MAP = Map(
    map=[
        "#################",
        "#...#...#...#...#",
        "#.#.#.#.#.#.#.#.#",
        "#.#.#.#...#...#.#",
        "#.#.#.#.###.#.#.#",
        "#...#.#.#.....#.#",
        "#.#.#.#.#.#####.#",
        "#.#...#.#.#.....#",
        "#.#.#####.#.###.#",
        "#.#.#.......#...#",
        "#.#.###.#####.###",
        "#.#.#...#.....#.#",
        "#.#.#.#####.###.#",
        "#.#.#.........#.#",
        "#.#.#.#########.#",
        "#.#.............#",
        "#################",
    ],
    start=(1, 15),
    end=(15, 1),
)


@pytest.mark.parametrize(
    "map, nb_cells_in_path",
    [
        (MAP, 45),
        (SECOND_MAP, 64),
    ],
)
def test_total_distance_can_be_computed(map, nb_cells_in_path):
    assert compute_solution(map) == nb_cells_in_path