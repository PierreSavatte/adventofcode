from _2024.day13 import Machine, Unsolvable, parse_input
from _2024.load_input import load_input


def compute_solution(machines: list[Machine]) -> int:
    token_cost_a = 3
    token_cost_b = 1

    solution = 0
    for machine in machines:
        try:
            nb_press_a, nb_press_b = machine.get_prize()
        except Unsolvable:
            continue

        solution += nb_press_a * token_cost_a + nb_press_b * token_cost_b

    return solution


def main():
    input_data = load_input(13)
    machines = parse_input(input_data)
    print(compute_solution(machines))


if __name__ == "__main__":
    main()
