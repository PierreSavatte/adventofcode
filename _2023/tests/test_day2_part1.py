import pytest
from _2023.day2 import parse_line, Game, filter_games, compute_answer


@pytest.mark.parametrize(
    "line, expected_value",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            Game(id=1, max_blue=6, max_red=4, max_green=2),
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            Game(id=2, max_blue=4, max_red=1, max_green=3),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",  # noqa: E501
            Game(id=3, max_blue=6, max_red=20, max_green=13),
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",  # noqa: E501
            Game(id=4, max_blue=15, max_red=14, max_green=3),
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            Game(id=5, max_blue=2, max_red=6, max_green=3),
        ),
    ],
)
def test_line_is_properly_parsed(line, expected_value):
    assert parse_line(line) == expected_value


def test_games_can_be_filtered():
    assert (
        filter_games(
            [
                Game(id=1, max_blue=6, max_red=4, max_green=2),
                Game(id=2, max_blue=4, max_red=1, max_green=3),
                Game(id=3, max_blue=6, max_red=20, max_green=13),
                Game(id=4, max_blue=15, max_red=14, max_green=3),
                Game(id=5, max_blue=2, max_red=6, max_green=3),
            ]
        )
        == [1, 2, 5]
    )


def test_answer_can_be_computed(get_data):
    assert compute_answer(get_data("test_file_day2_part1")) == 8
