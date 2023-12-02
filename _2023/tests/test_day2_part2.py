import pytest
from _2023.day2.part2 import Game, compute_power_of_game, compute_answer


@pytest.mark.parametrize(
    "game, power",
    [
        (Game(id=1, max_blue=6, max_red=4, max_green=2), 48),
        (Game(id=2, max_blue=4, max_red=1, max_green=3), 12),
        (Game(id=3, max_blue=6, max_red=20, max_green=13), 1560),
        (Game(id=4, max_blue=15, max_red=14, max_green=3), 630),
        (Game(id=5, max_blue=2, max_red=6, max_green=3), 36),
    ],
)
def test_power_of_a_set_can_be_computed(game, power):
    assert compute_power_of_game(game) == power


def test_answer_can_be_computed(get_data):
    assert compute_answer(get_data("test_file_day2")) == 2286
