from _2025.load_input import load_input


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


def get_max_joltage(batteries: str) -> int:
    for a in range(9, -1, -1):
        i = batteries.find(str(a))
        if i == -1:
            continue

        sub_batteries = batteries[i + 1 :]
        for b in range(9, -1, -1):
            j = sub_batteries.find(str(b))
            if j == -1:
                continue

            return int(f"{a}{b}")
    return 0


def get_total_joltage_output(banks: list[str]) -> int:
    return sum(get_max_joltage(batteries) for batteries in banks)


def main():
    input = load_input(3)
    print(get_total_joltage_output(parse_input(input)))


if __name__ == "__main__":
    main()
