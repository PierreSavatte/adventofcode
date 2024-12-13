import pytest
from _2024.day13 import Machine, Unsolvable, parse_input
from _2024.day13.part1 import compute_solution

TEST_INPUT = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == [
        Machine(prize=(8400, 5400), button_a=(94, 34), button_b=(22, 67)),
        Machine(prize=(12748, 12176), button_a=(26, 66), button_b=(67, 21)),
        Machine(prize=(7870, 6450), button_a=(17, 86), button_b=(84, 37)),
        Machine(prize=(18641, 10279), button_a=(69, 23), button_b=(27, 71)),
    ]


def test_machine_can_compute_button_press_number_to_get_the_prize():
    machine = Machine(prize=(8400, 5400), button_a=(94, 34), button_b=(22, 67))

    assert machine.get_prize() == (80, 40)


def test_unsolvable_machine_raises_an_error_while_trying_to_be_solved():
    machine = Machine(
        prize=(12748, 12176), button_a=(26, 66), button_b=(67, 21)
    )

    with pytest.raises(Unsolvable):
        machine.get_prize()


def test_machine_that_doest_exactly_land_on_prize_is_unsolvable():
    machine = Machine(
        prize=(12198, 17542), button_a=(14, 41), button_b=(70, 38)
    )

    with pytest.raises(Unsolvable):
        machine.get_prize()


def test_solution_can_be_computed():
    machines = [
        Machine(prize=(8400, 5400), button_a=(94, 34), button_b=(22, 67)),
        Machine(prize=(12748, 12176), button_a=(26, 66), button_b=(67, 21)),
        Machine(prize=(7870, 6450), button_a=(17, 86), button_b=(84, 37)),
        Machine(prize=(18641, 10279), button_a=(69, 23), button_b=(27, 71)),
    ]

    assert compute_solution(machines) == 480
