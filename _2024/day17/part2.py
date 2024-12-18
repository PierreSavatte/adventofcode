from _2024.day17 import Computer, parse_input
from _2024.load_input import load_input


def get_min_register_a_for_auto_replication(computer: Computer):
    register = 0
    for i in range(1, len(computer.program) + 1):
        expected_program_result = computer.program[-i:]
        expected_result = computer.get_program_to_string(
            expected_program_result
        )
        register *= 8
        for j in range(8):
            result = computer.my_program(register + j)
            if result == expected_result:
                register += j
                break
    return register


def compute_solution(computer: Computer) -> int:
    return get_min_register_a_for_auto_replication(computer)


def main():
    input_data = load_input(17)
    computer = parse_input(input_data)
    print(compute_solution(computer))


if __name__ == "__main__":
    main()
