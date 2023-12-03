import pytest

from _2023.day3 import Schematic, Number, Position, Symbol, compute_answer

DATA_FILENAME = "test_file_day3"


@pytest.fixture
def schematic(get_data):
    return Schematic.from_data(get_data(DATA_FILENAME))


@pytest.fixture
def expected_symbols():
    return [
        Symbol(value="*", position=Position(3, 1)),
        Symbol(value="#", position=Position(6, 3)),
        Symbol(value="*", position=Position(3, 4)),
        Symbol(value="+", position=Position(5, 5)),
        Symbol(value="$", position=Position(3, 8)),
        Symbol(value="*", position=Position(5, 8)),
    ]


def test_schematic_can_be_computed(get_data):
    data = get_data(DATA_FILENAME)
    assert Schematic.from_data(data) == Schematic(
        cells=[
            ["4", "6", "7", ".", ".", "1", "1", "4", ".", "."],
            [".", ".", ".", "*", ".", ".", ".", ".", ".", "."],
            [".", ".", "3", "5", ".", ".", "6", "3", "3", "."],
            [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
            ["6", "1", "7", "*", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "+", ".", "5", "8", "."],
            [".", ".", "5", "9", "2", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "7", "5", "5", "."],
            [".", ".", ".", "$", ".", "*", ".", ".", ".", "."],
            [".", "6", "6", "4", ".", "5", "9", "8", ".", "."],
        ]
    )


def test_schematic_can_compute_its_numbers(schematic):
    assert schematic.numbers == [
        Number(
            value=467,
            positions=[Position(0, 0), Position(1, 0), Position(2, 0)],
        ),
        Number(
            value=114,
            positions=[Position(5, 0), Position(6, 0), Position(7, 0)],
        ),
        Number(
            value=35,
            positions=[Position(2, 2), Position(3, 2)],
        ),
        Number(
            value=633,
            positions=[Position(6, 2), Position(7, 2), Position(8, 2)],
        ),
        Number(
            value=617,
            positions=[Position(0, 4), Position(1, 4), Position(2, 4)],
        ),
        Number(
            value=58,
            positions=[Position(7, 5), Position(8, 5)],
        ),
        Number(
            value=592,
            positions=[Position(2, 6), Position(3, 6), Position(4, 6)],
        ),
        Number(
            value=755,
            positions=[Position(6, 7), Position(7, 7), Position(8, 7)],
        ),
        Number(
            value=664,
            positions=[Position(1, 9), Position(2, 9), Position(3, 9)],
        ),
        Number(
            value=598,
            positions=[Position(5, 9), Position(6, 9), Position(7, 9)],
        ),
    ]


def test_schematic_can_compute_its_symbols(schematic, expected_symbols):
    assert schematic.symbols == expected_symbols


@pytest.mark.parametrize(
    "is_close, number",
    [
        (
            True,
            Number(
                value=467,
                positions=[Position(0, 0), Position(1, 0), Position(2, 0)],
            ),
        ),
        (
            False,
            Number(
                value=114,
                positions=[Position(5, 0), Position(6, 0), Position(7, 0)],
            ),
        ),
        (
            True,
            Number(
                value=35,
                positions=[Position(2, 2), Position(3, 2)],
            ),
        ),
        (
            True,
            Number(
                value=633,
                positions=[Position(6, 2), Position(7, 2), Position(8, 2)],
            ),
        ),
        (
            True,
            Number(
                value=617,
                positions=[Position(0, 4), Position(1, 4), Position(2, 4)],
            ),
        ),
        (
            False,
            Number(
                value=58,
                positions=[Position(7, 5), Position(8, 5)],
            ),
        ),
        (
            True,
            Number(
                value=592,
                positions=[Position(2, 6), Position(3, 6), Position(4, 6)],
            ),
        ),
        (
            True,
            Number(
                value=755,
                positions=[Position(6, 7), Position(7, 7), Position(8, 7)],
            ),
        ),
        (
            True,
            Number(
                value=664,
                positions=[Position(1, 9), Position(2, 9), Position(3, 9)],
            ),
        ),
        (
            True,
            Number(
                value=598,
                positions=[Position(5, 9), Position(6, 9), Position(7, 9)],
            ),
        ),
    ],
)
def test_number_can_say_if_close_to_any_symbols(
    is_close, number, expected_symbols
):
    assert number.is_close_to_a_symbol(symbols=expected_symbols) is is_close


def test_solution_can_be_computed(get_data):
    assert compute_answer(get_data(DATA_FILENAME)) == 4361
