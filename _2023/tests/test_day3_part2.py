import pytest

from _2023.day3 import Schematic, Number, Position, Gear
from _2023.day3.part2 import compute_answer

DATA_FILENAME = "test_file_day3"

GEAR_1 = Gear(
    position=Position(3, 1),
    numbers=[
        Number(
            value=467,
            positions=[Position(0, 0), Position(1, 0), Position(2, 0)],
        ),
        Number(value=35, positions=[Position(2, 2), Position(3, 2)]),
    ],
)

GEAR_2 = Gear(
    position=Position(5, 8),
    numbers=[
        Number(
            value=755,
            positions=[Position(6, 7), Position(7, 7), Position(8, 7)],
        ),
        Number(
            value=598,
            positions=[Position(5, 9), Position(6, 9), Position(7, 9)],
        ),
    ],
)


@pytest.fixture
def schematic(get_data):
    return Schematic.from_data(get_data(DATA_FILENAME))


def test_schematic_can_compute_its_gears(schematic):
    assert schematic.get_gears() == [GEAR_1, GEAR_2]


@pytest.mark.parametrize(
    "gear, expected_ratio", [(GEAR_1, 16345), (GEAR_2, 451490)]
)
def test_gear_can_compute_its_ratio(gear, expected_ratio):
    assert gear.ratio == expected_ratio


def test_solution_can_be_computed(get_data):
    assert compute_answer(get_data(DATA_FILENAME)) == 467835
