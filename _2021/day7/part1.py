FILE = "input"


def parse_file(file_path):
    with open(file_path, "r") as fp:
        data = fp.readline()
    return [int(individual) for individual in data.strip("\n").split(",")]


def median(list):
    n = len(list)
    sorted_list = sorted(list)
    if n % 2 == 0:
        return sorted_list[(n + 1) // 2]
    else:
        sorted_list[n // 2] + sorted_list[n // 2 + 1] // 2


def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def resolution(crab_positions):
    optimal_position = median(crab_positions)

    solution = 0
    for crab_position in crab_positions:
        solution += diff(crab_position, optimal_position)
    return solution


def challenge_resolution():
    lines = parse_file(FILE)
    return resolution(lines)


if __name__ == "__main__":
    print(challenge_resolution())
