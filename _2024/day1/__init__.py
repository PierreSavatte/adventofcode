def parse_input(input_data: str) -> tuple[list[int], list[int]]:
    input_data = input_data.strip("\n")

    list_a = []
    list_b = []

    for line in input_data.split("\n"):
        a, b = line.split()
        list_a.append(int(a.strip()))
        list_b.append(int(b.strip()))

    return list_a, list_b


def sort(l: list[int]) -> list[int]:
    l_ = l.copy()
    l_.sort()
    return l_
