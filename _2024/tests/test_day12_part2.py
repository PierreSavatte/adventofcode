import pytest
from _2024.day12 import Region, Side, compute_regions, merge_sides
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


def test_horizontal_sides_can_be_merged():
    """
    - -
    A A A A

    B B C D

    B B C C
    """
    side_a = Side(x_range=[0, 1], y_range=[0])
    side_b = Side(x_range=[1, 2], y_range=[0])

    assert merge_sides(side_a, side_b) == Side(x_range=[0, 2], y_range=[0])


def test_different_horizontal_sides_cannot_be_merged():
    """
    -
    A A A A
    -
    B B C D

    B B C C
    """
    side_a = Side(x_range=[0, 1], y_range=[0])
    side_b = Side(x_range=[0, 1], y_range=[1])

    assert merge_sides(side_a, side_b) is None


def test_vertical_sides_can_be_merged():
    """

     A A A A

    |B B C D

    |B B C C
    """
    side_a = Side(x_range=[0], y_range=[1, 2])
    side_b = Side(x_range=[0], y_range=[2, 3])

    assert merge_sides(side_a, side_b) == Side(x_range=[0], y_range=[1, 3])


def test_different_vertical_sides_cannot_be_merged():
    """

     A A A A

    |B B C D

     B B|C C
    """
    side_a = Side(x_range=[0], y_range=[0, 1])
    side_b = Side(x_range=[2], y_range=[1, 2])

    assert merge_sides(side_a, side_b) is None


def test_vertical_and_horizontal_sides_are_not_merged():
    """
     -
    |A A A A

     B B C D

     B B C C
    """
    side_a = Side(x_range=[0, 1], y_range=[0])
    side_b = Side(x_range=[0], y_range=[0, 1])

    assert merge_sides(side_a, side_b) is None


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

    assert region.sides == [
        Side(x_range=[0], y_range=[0, 1]),
        Side(x_range=[0, 4], y_range=[0]),
        Side(x_range=[0, 4], y_range=[1]),
        Side(x_range=[4], y_range=[0, 1]),
    ]


@pytest.mark.parametrize(
    "map, character_sides",
    [
        (
            MAP_2,
            [
                (
                    "A",
                    [
                        Side(x_range=[3, 5], y_range=[1]),
                        Side(x_range=[0, 6], y_range=[0]),
                        Side(x_range=[1, 3], y_range=[3]),
                        Side(x_range=[3], y_range=[1, 3]),
                        Side(x_range=[5], y_range=[1, 3]),
                        Side(x_range=[1, 5], y_range=[3]),
                        Side(x_range=[1], y_range=[3, 5]),
                        Side(x_range=[3], y_range=[1, 5]),
                        Side(x_range=[0], y_range=[0, 6]),
                        Side(x_range=[1, 3], y_range=[5]),
                        Side(x_range=[0, 6], y_range=[6]),
                        Side(x_range=[6], y_range=[0, 6]),
                    ],
                ),
                (
                    "B",
                    [
                        Side(x_range=[3, 5], y_range=[1]),
                        Side(x_range=[3], y_range=[1, 3]),
                        Side(x_range=[3, 5], y_range=[3]),
                        Side(x_range=[5], y_range=[1, 3]),
                    ],
                ),
                (
                    "B",
                    [
                        Side(x_range=[1, 3], y_range=[3]),
                        Side(x_range=[1], y_range=[3, 5]),
                        Side(x_range=[1, 3], y_range=[5]),
                        Side(x_range=[3], y_range=[3, 5]),
                    ],
                ),
            ],
        ),
        (
            MAP_3,
            [
                (
                    "C",
                    [
                        Side(x_range=[6, 8], y_range=[0]),
                        Side(x_range=[8], y_range=[0, 1]),
                        Side(x_range=[6], y_range=[0, 2]),
                        Side(x_range=[8, 9], y_range=[1]),
                        Side(x_range=[7, 9], y_range=[2]),
                        Side(x_range=[9], y_range=[1, 2]),
                        Side(x_range=[5, 6], y_range=[2]),
                        Side(x_range=[5], y_range=[2, 3]),
                        Side(x_range=[6, 7], y_range=[3]),
                        Side(x_range=[7], y_range=[2, 3]),
                        Side(x_range=[3], y_range=[3, 4]),
                        Side(x_range=[3, 4], y_range=[4]),
                        Side(x_range=[3, 5], y_range=[3]),
                        Side(x_range=[5, 6], y_range=[4]),
                        Side(x_range=[6], y_range=[3, 4]),
                        Side(x_range=[5], y_range=[4, 5]),
                        Side(x_range=[4], y_range=[4, 6]),
                        Side(x_range=[4, 5], y_range=[6]),
                        Side(x_range=[5, 6], y_range=[5]),
                        Side(x_range=[5], y_range=[6, 7]),
                        Side(x_range=[5, 6], y_range=[7]),
                        Side(x_range=[6], y_range=[5, 7]),
                    ],
                ),
                (
                    "C",
                    [
                        Side(x_range=[7, 8], y_range=[4]),
                        Side(x_range=[7], y_range=[4, 5]),
                        Side(x_range=[7, 8], y_range=[5]),
                        Side(x_range=[8], y_range=[4, 5]),
                    ],
                ),
                (
                    "E",
                    [
                        Side(x_range=[9, 10], y_range=[4]),
                        Side(x_range=[9], y_range=[4, 5]),
                        Side(x_range=[8, 9], y_range=[5]),
                        Side(x_range=[8], y_range=[5, 8]),
                        Side(x_range=[7, 8], y_range=[8]),
                        Side(x_range=[7], y_range=[8, 10]),
                        Side(x_range=[7, 10], y_range=[10]),
                        Side(x_range=[10], y_range=[4, 10]),
                    ],
                ),
                (
                    "F",
                    [
                        Side(x_range=[8], y_range=[0, 1]),
                        Side(x_range=[8, 9], y_range=[1]),
                        Side(x_range=[8, 10], y_range=[0]),
                        Side(x_range=[9], y_range=[1, 2]),
                        Side(x_range=[7, 9], y_range=[2]),
                        Side(x_range=[7], y_range=[2, 4]),
                        Side(x_range=[7, 8], y_range=[4]),
                        Side(x_range=[9, 10], y_range=[4]),
                        Side(x_range=[10], y_range=[0, 4]),
                        Side(x_range=[8], y_range=[4, 5]),
                        Side(x_range=[8, 9], y_range=[5]),
                        Side(x_range=[9], y_range=[4, 5]),
                    ],
                ),
                (
                    "I",
                    [
                        Side(x_range=[4, 6], y_range=[0]),
                        Side(x_range=[4], y_range=[0, 2]),
                        Side(x_range=[4, 6], y_range=[2]),
                        Side(x_range=[6], y_range=[0, 2]),
                    ],
                ),
                (
                    "I",
                    [
                        Side(x_range=[2, 3], y_range=[5]),
                        Side(x_range=[3], y_range=[5, 6]),
                        Side(x_range=[2], y_range=[5, 7]),
                        Side(x_range=[3, 5], y_range=[6]),
                        Side(x_range=[5], y_range=[6, 7]),
                        Side(x_range=[1, 2], y_range=[7]),
                        Side(x_range=[4, 5], y_range=[8]),
                        Side(x_range=[5, 6], y_range=[7]),
                        Side(x_range=[1], y_range=[7, 9]),
                        Side(x_range=[1, 3], y_range=[9]),
                        Side(x_range=[5], y_range=[8, 9]),
                        Side(x_range=[5, 6], y_range=[9]),
                        Side(x_range=[6], y_range=[7, 9]),
                        Side(x_range=[3], y_range=[9, 10]),
                        Side(x_range=[3, 4], y_range=[10]),
                        Side(x_range=[4], y_range=[8, 10]),
                    ],
                ),
                (
                    "J",
                    [
                        Side(x_range=[6, 7], y_range=[3]),
                        Side(x_range=[6], y_range=[3, 4]),
                        Side(x_range=[5, 6], y_range=[4]),
                        Side(x_range=[5], y_range=[4, 5]),
                        Side(x_range=[5, 6], y_range=[5]),
                        Side(x_range=[7], y_range=[3, 5]),
                        Side(x_range=[7, 8], y_range=[5]),
                        Side(x_range=[7, 8], y_range=[8]),
                        Side(x_range=[8], y_range=[5, 8]),
                        Side(x_range=[6], y_range=[5, 10]),
                        Side(x_range=[6, 7], y_range=[10]),
                        Side(x_range=[7], y_range=[8, 10]),
                    ],
                ),
                (
                    "M",
                    [
                        Side(x_range=[0, 1], y_range=[7]),
                        Side(x_range=[1], y_range=[7, 9]),
                        Side(x_range=[0], y_range=[7, 10]),
                        Side(x_range=[1, 3], y_range=[9]),
                        Side(x_range=[0, 3], y_range=[10]),
                        Side(x_range=[3], y_range=[9, 10]),
                    ],
                ),
                (
                    "R",
                    [
                        Side(x_range=[0, 4], y_range=[0]),
                        Side(x_range=[0], y_range=[0, 2]),
                        Side(x_range=[0, 2], y_range=[2]),
                        Side(x_range=[4], y_range=[0, 2]),
                        Side(x_range=[4, 5], y_range=[2]),
                        Side(x_range=[3, 5], y_range=[3]),
                        Side(x_range=[5], y_range=[2, 3]),
                        Side(x_range=[2], y_range=[2, 4]),
                        Side(x_range=[2, 3], y_range=[4]),
                        Side(x_range=[3], y_range=[3, 4]),
                    ],
                ),
                (
                    "S",
                    [
                        Side(x_range=[4, 5], y_range=[8]),
                        Side(x_range=[5], y_range=[8, 9]),
                        Side(x_range=[4], y_range=[8, 10]),
                        Side(x_range=[5, 6], y_range=[9]),
                        Side(x_range=[4, 6], y_range=[10]),
                        Side(x_range=[6], y_range=[9, 10]),
                    ],
                ),
                (
                    "V",
                    [
                        Side(x_range=[0, 2], y_range=[2]),
                        Side(x_range=[2], y_range=[2, 4]),
                        Side(x_range=[2, 3], y_range=[5]),
                        Side(x_range=[2, 4], y_range=[4]),
                        Side(x_range=[3], y_range=[5, 6]),
                        Side(x_range=[3, 4], y_range=[6]),
                        Side(x_range=[4], y_range=[4, 6]),
                        Side(x_range=[0], y_range=[2, 7]),
                        Side(x_range=[0, 2], y_range=[7]),
                        Side(x_range=[2], y_range=[5, 7]),
                    ],
                ),
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
