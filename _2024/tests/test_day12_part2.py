import pytest
from _2024.day12 import Region, compute_regions
from _2024.day12.part2 import compute_solution

MAP = [
    ["A", "A", "A", "A"],
    ["B", "B", "C", "D"],
    ["B", "B", "C", "C"],
    ["E", "E", "E", "C"],
]

MAP_2 = [
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "B", "B", "A"],
    ["A", "A", "A", "B", "B", "A"],
    ["A", "B", "B", "A", "A", "A"],
    ["A", "B", "B", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
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

MAP_4 = [
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O"],
    ["O", "O", "O", "O", "O"],
]


def test_region_can_have_its_sides_computed():
    region = Region(
        character="A",
        positions=[],
        area=0,
        perimeter=0,
        map=MAP,
    )

    region.add_new_position((0, 0))
    region.add_new_position((1, 0))
    region.add_new_position((2, 0))
    region.add_new_position((3, 0))

    assert region.sides == 4


@pytest.mark.parametrize(
    "map, character_sides",
    [
        (MAP_2, [("A", 12), ("B", 4), ("B", 4)]),
        (
            MAP_3,
            [
                ("C", 22),
                ("C", 4),
                ("E", 8),
                ("F", 12),
                ("I", 4),
                ("I", 16),
                ("J", 12),
                ("M", 6),
                ("R", 10),
                ("S", 6),
                ("V", 10),
            ],
        ),
    ],
)
def test_sides_can_be_computed_for_a_whole_map(map, character_sides):
    regions = compute_regions(map)

    assert [
        (region.character, region.sides) for region in regions
    ] == character_sides


@pytest.mark.parametrize(
    "map, solution",
    [
        (MAP, 80),
        (
            [
                ["E", "E", "E", "E", "E"],
                ["E", "X", "X", "X", "X"],
                ["E", "E", "E", "E", "E"],
                ["E", "X", "X", "X", "X"],
                ["E", "E", "E", "E", "E"],
            ],
            236,
        ),
        (
            [
                ["E", "E", "E", "E", "E"],
                ["E", "X", "X", "X", "X"],
                ["E", "E", "E", "E", "E"],
                ["E", "X", "X", "X", "X"],
                ["E", "E", "E", "E", "E"],
            ],
            236,
        ),
        (MAP_2, 368),
        (MAP_3, 1206),
        (MAP_4, 436),
    ],
)
def test_solution_can_be_computed(map, solution):
    assert compute_solution(map) == solution
