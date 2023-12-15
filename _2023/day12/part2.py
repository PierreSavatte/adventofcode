from _2023.load_input import load_input


def compute_arrangements(line: str) -> int:
    raise NotImplementedError()


def compute_solution(data: str) -> int:
    total_possible_arrangements = 0
    for line in data.splitlines():
        total_possible_arrangements += compute_arrangements(line)
    return total_possible_arrangements


if __name__ == "__main__":
    print(compute_solution(load_input(12)))
