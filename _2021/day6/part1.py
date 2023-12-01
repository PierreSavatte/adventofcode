FILE = "input"


def parse_file(file_path):
    with open(file_path, "r") as fp:
        data = fp.readline()
    return [int(individual) for individual in data.strip("\n").split(",")]


def compute_new_generation(old_generation):
    new_generation = []
    new_individuals = []
    for individual in old_generation:
        if individual == 0:
            new_generation.append(6)
            new_individuals.append(8)
        else:
            new_generation.append(individual - 1)
    return [*new_generation, *new_individuals]


def resolution(generation, nb_days=80):
    for i in range(nb_days):
        generation = compute_new_generation(generation)
    return len(generation)


def challenge_resolution():
    lines = parse_file(FILE)
    return resolution(lines)


if __name__ == "__main__":
    print(challenge_resolution())
