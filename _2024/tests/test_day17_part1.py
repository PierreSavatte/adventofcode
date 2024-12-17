import pytest
from _2024.day17 import Computer, ReservedValue, parse_input

TEST_INPUT = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == Computer(
        register_a=729, register_b=0, register_c=0, program=[0, 1, 5, 4, 3, 0]
    )


@pytest.mark.parametrize(
    "literal_operand, expected_value",
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 123), (5, 456), (6, 789)],
)
def test_computer_can_read_operand(literal_operand, expected_value):
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[0, 1, 5, 4, 3, 0],
    )
    assert computer.to_combo_operand(literal_operand) == expected_value


def test_computer_raises_error_when_reading_reserved_operand():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[0, 1, 5, 4, 3, 0],
    )
    with pytest.raises(ReservedValue):
        computer.to_combo_operand(7)


def test_computer_can_execute_adv():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[0, 5],
    )

    assert computer.read() == 0  # We need to execute adv

    computer.adv()

    assert computer.instruction_pointer == 2
    assert computer.register_a == int(123 / (2 ** 456))

    # No other side effects
    assert computer.register_b == 456
    assert computer.register_c == 789


def test_computer_can_execute_bxl():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[1, 5],
    )

    assert computer.read() == 1  # We need to execute bxl

    computer.bxl()

    assert computer.instruction_pointer == 2
    assert computer.register_b == 456 ^ 5

    # No other side effects
    assert computer.register_a == 123
    assert computer.register_c == 789


def test_computer_can_execute_bst():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[2, 5],
    )

    assert computer.read() == 2  # We need to execute bst

    computer.bst()

    assert computer.instruction_pointer == 2
    assert computer.register_b == 456 % 8

    # No other side effects
    assert computer.register_a == 123
    assert computer.register_c == 789


def test_computer_can_execute_jnz_with_register_a_equals_0():
    computer = Computer(
        register_a=0,
        register_b=456,
        register_c=789,
        program=[3, 5],
    )

    assert computer.read() == 3  # We need to execute jnz

    computer.jnz()

    # Still increase pointer by 1
    assert computer.instruction_pointer == 2

    # No other side effects
    assert computer.register_a == 0
    assert computer.register_b == 456
    assert computer.register_c == 789


def test_computer_can_execute_jnz_with_register_a_not_equal_to_0():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[3, 5],
    )

    assert computer.read() == 3  # We need to execute jnz

    computer.jnz()

    assert computer.instruction_pointer == 5

    # No other side effects
    assert computer.register_a == 123
    assert computer.register_b == 456
    assert computer.register_c == 789


def test_computer_can_execute_bxc():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[4, 5],
    )

    assert computer.read() == 4  # We need to execute bxc

    computer.bxc()

    assert computer.instruction_pointer == 2
    assert computer.register_b == 456 ^ 789

    # No other side effects
    assert computer.register_a == 123
    assert computer.register_c == 789


def test_computer_can_execute_out():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[5, 5],
    )

    assert computer.read() == 5  # We need to execute out

    output = computer.out()

    assert computer.instruction_pointer == 2
    assert output == 456 % 8

    # No other side effects
    assert computer.register_a == 123
    assert computer.register_b == 456
    assert computer.register_c == 789


def test_computer_can_execute_bdv():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[6, 5],
    )

    assert computer.read() == 6  # We need to execute bdv

    computer.bdv()

    assert computer.instruction_pointer == 2
    assert computer.register_b == int(123 / (2 ** 456))

    # No other side effects
    assert computer.register_a == 123
    assert computer.register_c == 789


def test_computer_can_execute_cdv():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[7, 5],
    )

    assert computer.read() == 7  # We need to execute cdv

    computer.cdv()

    assert computer.instruction_pointer == 2
    assert computer.register_c == int(123 / (2 ** 456))

    # No other side effects
    assert computer.register_a == 123
    assert computer.register_b == 456


@pytest.mark.parametrize(
    "opcode, expected_method_name",
    [
        (0, "adv"),
        (1, "bxl"),
        (2, "bst"),
        (3, "jnz"),
        (4, "bxc"),
        (5, "out"),
        (6, "bdv"),
        (7, "cdv"),
    ],
)
def test_computer_can_read_instruction(opcode, expected_method_name):
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[opcode, 1, 5, 4, 3, 0],
    )
    computer.instruction_pointer = 0
    assert computer.to_instruction(opcode) == getattr(
        computer, expected_method_name
    )


def test_computer_can_execute_a_step():
    computer = Computer(
        register_a=123,
        register_b=456,
        register_c=789,
        program=[5, 1, 5, 4, 3, 0],
    )

    output = computer.step()

    assert output == 1
    assert computer.instruction_pointer == 2


def test_computer_can_run_program_1():
    computer = Computer(
        register_a=0,
        register_b=0,
        register_c=9,
        program=[2, 6],
    )

    output = computer.run()

    assert output == []
    assert computer.register_b == 1


def test_computer_can_run_program_2():
    computer = Computer(
        register_a=10,
        register_b=0,
        register_c=0,
        program=[5, 0, 5, 1, 5, 4],
    )

    output = computer.run()

    assert output == [0, 1, 2]


def test_computer_can_run_program_3():
    computer = Computer(
        register_a=2024,
        register_b=0,
        register_c=0,
        program=[0, 1, 5, 4, 3, 0],
    )

    output = computer.run()

    assert output == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert computer.register_a == 0


def test_computer_can_run_program_4():
    computer = Computer(
        register_a=0,
        register_b=29,
        register_c=0,
        program=[1, 7],
    )

    output = computer.run()

    assert output == []
    assert computer.register_b == 26


def test_computer_can_run_program_5():
    computer = Computer(
        register_a=0,
        register_b=2024,
        register_c=43690,
        program=[4, 0],
    )

    output = computer.run()

    assert output == []
    assert computer.register_b == 44354


def test_computer_can_run_example_program():
    computer = Computer(
        register_a=729,
        register_b=0,
        register_c=0,
        program=[0, 1, 5, 4, 3, 0],
    )

    output = computer.run()

    assert output == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]
