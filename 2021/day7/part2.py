from day7.part1 import parse_file, diff

FILE = "input"


def cost(n):
    return int(n * (n + 1) / 2)


def resolution(crab_positions):
    min_i = min(crab_positions)
    max_i = max(crab_positions)
    optimal_solution = None
    for goal_position in range(min_i, max_i):
        solution = 0
        for crab_position in crab_positions:
            solution += cost(diff(crab_position, goal_position))

        if optimal_solution is None or solution < optimal_solution:
            optimal_solution = solution
    return optimal_solution


def challenge_resolution():
    lines = parse_file(FILE)
    return resolution(lines)


if __name__ == "__main__":
    print(challenge_resolution())
