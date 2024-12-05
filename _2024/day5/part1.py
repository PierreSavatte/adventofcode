from _2024.day5 import PrintQueue, parse_input
from _2024.load_input import load_input


def compute_solution(print_queue: PrintQueue) -> int:
    return sum(
        update.get_middle_page()
        for update in print_queue.updates
        if update.validate_order(print_queue.ordering_rules)
    )


def main():
    input_data = load_input(5)
    print_queue = parse_input(input_data)
    print(compute_solution(print_queue))


if __name__ == "__main__":
    main()
