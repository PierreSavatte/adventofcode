import pytest
from _2024.day12 import Region, RegionList, compute_regions, parse_input
from _2024.day12.part1 import compute_solution

TEST_INPUT = """AAAA
BBCD
BBCC
EEEC
"""

MAP = [
    ["A", "A", "A", "A"],
    ["B", "B", "C", "D"],
    ["B", "B", "C", "C"],
    ["E", "E", "E", "C"],
]

MAP_2 = [
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O"],
    ["O", "O", "O", "O", "O"],
]


MAP_3 = [
    ["R", "R", "R", "R", "I", "I", "C", "C", "F", "F"],
    ["R", "R", "R", "R", "I", "I", "C", "C", "C", "F"],
    ["V", "V", "R", "R", "R", "C", "C", "F", "F", "F"],
    ["V", "V", "R", "C", "C", "C", "J", "F", "F", "F"],
    ["V", "V", "V", "V", "C", "J", "J", "C", "F", "E"],
    ["V", "V", "I", "V", "C", "C", "J", "J", "E", "E"],
    ["V", "V", "I", "I", "I", "C", "J", "J", "E", "E"],
    ["M", "I", "I", "I", "I", "I", "J", "J", "E", "E"],
    ["M", "I", "I", "I", "S", "I", "J", "E", "E", "E"],
    ["M", "M", "M", "I", "S", "S", "J", "E", "E", "E"],
]


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == MAP


def test_regions_can_know_if_new_cell_is_linked_to_same_region():
    regions = RegionList(map=MAP)
    expected_region = Region(
        map=MAP,
        character="A",
        positions=[(0, 0)],
        area=1,
        perimeter=3,
    )
    regions.append(expected_region)
    regions.append(
        Region(
            map=MAP,
            character="C",
            positions=[(3, 3)],
            area=1,
            perimeter=2,
        )
    )

    assert (
        regions.get_region_with(
            character="A", cell_left=(0, 0), cell_up=(0, -1)
        )
        == expected_region
    )


def test_new_position_can_be_added_to_region():
    region = Region(
        map=MAP,
        character="A",
        positions=[(0, 0)],
        area=1,
        perimeter=3,
    )

    region.add_new_position((1, 0))

    assert region == Region(
        map=MAP,
        character="A",
        positions=[(0, 0), (1, 0)],
        area=2,
        perimeter=5,
    )


@pytest.mark.parametrize(
    "map, regions",
    [
        (
            MAP,
            [
                Region(
                    character="A",
                    positions=[(0, 0), (1, 0), (2, 0), (3, 0)],
                    area=4,
                    perimeter=10,
                    map=MAP,
                ),
                Region(
                    character="B",
                    positions=[(0, 1), (1, 1), (0, 2), (1, 2)],
                    area=4,
                    perimeter=8,
                    map=MAP,
                ),
                Region(
                    character="C",
                    positions=[(2, 1), (2, 2), (3, 2), (3, 3)],
                    area=4,
                    perimeter=10,
                    map=MAP,
                ),
                Region(
                    character="D",
                    positions=[(3, 1)],
                    area=1,
                    perimeter=4,
                    map=MAP,
                ),
                Region(
                    character="E",
                    positions=[(0, 3), (1, 3), (2, 3)],
                    area=3,
                    perimeter=8,
                    map=MAP,
                ),
            ],
        ),
        (
            MAP_2,
            [
                Region(
                    character="O",
                    area=21,
                    perimeter=36,
                    map=MAP_2,
                    positions=[
                        (0, 0),
                        (1, 0),
                        (2, 0),
                        (3, 0),
                        (4, 0),
                        (0, 1),
                        (2, 1),
                        (4, 1),
                        (0, 2),
                        (1, 2),
                        (2, 2),
                        (3, 2),
                        (4, 2),
                        (0, 3),
                        (2, 3),
                        (4, 3),
                        (0, 4),
                        (1, 4),
                        (2, 4),
                        (3, 4),
                        (4, 4),
                    ],
                ),
                Region(
                    character="X",
                    area=1,
                    perimeter=4,
                    map=MAP_2,
                    positions=[(1, 1)],
                ),
                Region(
                    character="X",
                    area=1,
                    perimeter=4,
                    map=MAP_2,
                    positions=[(3, 1)],
                ),
                Region(
                    character="X",
                    area=1,
                    perimeter=4,
                    map=MAP_2,
                    positions=[(1, 3)],
                ),
                Region(
                    character="X",
                    area=1,
                    perimeter=4,
                    map=MAP_2,
                    positions=[(3, 3)],
                ),
            ],
        ),
        (
            MAP_3,
            [
                Region(
                    character="C",
                    area=14,
                    perimeter=28,
                    positions=[
                        (6, 0),
                        (7, 0),
                        (6, 1),
                        (7, 1),
                        (8, 1),
                        (5, 2),
                        (6, 2),
                        (3, 3),
                        (4, 3),
                        (5, 3),
                        (4, 4),
                        (4, 5),
                        (5, 5),
                        (5, 6),
                    ],
                    map=MAP_3,
                ),
                Region(
                    character="C",
                    area=1,
                    perimeter=4,
                    positions=[(7, 4)],
                    map=MAP_3,
                ),
                Region(
                    character="E",
                    area=13,
                    perimeter=18,
                    positions=[
                        (9, 4),
                        (8, 5),
                        (9, 5),
                        (8, 6),
                        (9, 6),
                        (8, 7),
                        (9, 7),
                        (7, 8),
                        (8, 8),
                        (9, 8),
                        (7, 9),
                        (8, 9),
                        (9, 9),
                    ],
                    map=MAP_3,
                ),
                Region(
                    character="F",
                    area=10,
                    perimeter=18,
                    positions=[
                        (8, 0),
                        (9, 0),
                        (9, 1),
                        (7, 2),
                        (8, 2),
                        (9, 2),
                        (7, 3),
                        (8, 3),
                        (9, 3),
                        (8, 4),
                    ],
                    map=MAP_3,
                ),
                Region(
                    character="I",
                    area=4,
                    perimeter=8,
                    positions=[(4, 0), (5, 0), (4, 1), (5, 1)],
                    map=MAP_3,
                ),
                Region(
                    character="I",
                    area=14,
                    perimeter=22,
                    positions=[
                        (2, 5),
                        (2, 6),
                        (3, 6),
                        (4, 6),
                        (1, 7),
                        (2, 7),
                        (3, 7),
                        (4, 7),
                        (5, 7),
                        (1, 8),
                        (2, 8),
                        (3, 8),
                        (5, 8),
                        (3, 9),
                    ],
                    map=MAP_3,
                ),
                Region(
                    character="J",
                    area=11,
                    perimeter=20,
                    positions=[
                        (6, 3),
                        (5, 4),
                        (6, 4),
                        (6, 5),
                        (7, 5),
                        (6, 6),
                        (7, 6),
                        (6, 7),
                        (7, 7),
                        (6, 8),
                        (6, 9),
                    ],
                    map=MAP_3,
                ),
                Region(
                    character="M",
                    area=5,
                    perimeter=12,
                    positions=[(0, 7), (0, 8), (0, 9), (1, 9), (2, 9)],
                    map=MAP_3,
                ),
                Region(
                    character="R",
                    area=12,
                    perimeter=18,
                    positions=[
                        (0, 0),
                        (1, 0),
                        (2, 0),
                        (3, 0),
                        (0, 1),
                        (1, 1),
                        (2, 1),
                        (3, 1),
                        (2, 2),
                        (3, 2),
                        (4, 2),
                        (2, 3),
                    ],
                    map=MAP_3,
                ),
                Region(
                    character="S",
                    area=3,
                    perimeter=8,
                    positions=[(4, 8), (4, 9), (5, 9)],
                    map=MAP_3,
                ),
                Region(
                    character="V",
                    area=13,
                    perimeter=20,
                    positions=[
                        (0, 2),
                        (1, 2),
                        (0, 3),
                        (1, 3),
                        (0, 4),
                        (1, 4),
                        (2, 4),
                        (3, 4),
                        (0, 5),
                        (1, 5),
                        (3, 5),
                        (0, 6),
                        (1, 6),
                    ],
                    map=MAP_3,
                ),
            ],
        ),
    ],
)
def test_regions_can_be_computed(map, regions):
    assert compute_regions(map) == regions


def test_fence_price_can_be_computed():
    region = Region(
        character="S",
        area=3,
        perimeter=8,
        positions=[(4, 8), (4, 9), (5, 9)],
        map=MAP_3,
    )

    assert region.fence_price == 24


def test_solution_can_be_computed():
    assert compute_solution(MAP_3) == 1930
