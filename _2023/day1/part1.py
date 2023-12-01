from _2023.load_input import load_input


def get_first_integer(line: str) -> str:
    i = 0
    while i < len(line):
        if line[i].isdecimal():
            return line[i]
        i += 1


def parse_line(line: str) -> int:
    first = get_first_integer(line)
    opposite_line = "".join(list(reversed(line)))
    last = get_first_integer(opposite_line)
    return int("".join([first, last]))


def compute_answer(data: str):
    return sum(parse_line(line) for line in data.split("\n"))


if __name__ == "__main__":
    print(compute_answer(load_input(1)))
