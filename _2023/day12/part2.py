from _2023.load_input import load_input


def compute_arrangements(springs: str, groups: list[int]) -> int:
    raise NotImplementedError()


def compute_unfolded_arrangements(line: str) -> int:
    springs, groups_txt = line.split(" ")
    groups = [int(group) for group in groups_txt.split(",")]

    unfolded_springs = "?".join([springs] * 5)
    unfolded_groups = groups * 5

    return compute_arrangements(unfolded_springs, unfolded_groups)


def compute_solution(data: str) -> int:
    total_possible_arrangements = 0
    for line in data.splitlines():
        total_possible_arrangements += compute_unfolded_arrangements(line)
    return total_possible_arrangements


if __name__ == "__main__":
    print(compute_solution(load_input(12)))
