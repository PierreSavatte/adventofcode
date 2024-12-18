from _2024.day17 import Computer


def test_my_program_is_equivalent_to_program():
    register_a = 66245665
    computer = Computer(
        register_a=register_a,
        register_b=0,
        register_c=0,
        program=[2, 4, 1, 7, 7, 5, 1, 7, 4, 6, 0, 3, 5, 5, 3, 0],
    )

    other_computer = computer.copy()
    expected_result = other_computer.run()

    assert computer.my_program(register_a) == expected_result
