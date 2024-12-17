from _2024.day17 import Computer, parse_input
from _2024.load_input import load_input
from tqdm import tqdm


def get_min_register_a_for_auto_replication(computer: Computer):
    program_string = computer.program_string
    register_a = -1
    output = ""
    progress_bar = tqdm(total=1_000_000_000)
    while output != program_string:
        register_a += 1

        new_computer = computer.copy()
        new_computer.register_a = register_a

        output = new_computer.run()
        progress_bar.update(1)
    progress_bar.close()

    return register_a


def compute_solution(computer: Computer) -> int:
    return get_min_register_a_for_auto_replication(computer)


def main():
    input_data = load_input(17)
    computer = parse_input(input_data)
    print(compute_solution(computer))


if __name__ == "__main__":
    main()
