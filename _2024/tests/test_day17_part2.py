from _2024.day17 import Computer
from _2024.day17.part2 import get_min_register_a_for_auto_replication


def test_computer_can_evaluate_the_min_value_of_a_that_replicates_the_program():
    computer = Computer(
        register_a=0,
        register_b=0,
        register_c=0,
        program=[0, 3, 5, 4, 3, 0],
    )
    min_register_a = get_min_register_a_for_auto_replication(computer)

    assert min_register_a == 117440
