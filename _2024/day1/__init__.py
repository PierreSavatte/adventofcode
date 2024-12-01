def parse_input(input_data: str) -> tuple[list[int], list[int]]:
    input_data = input_data.strip("\n")

    list_a = []
    list_b = []

    for line in input_data.split("\n"):
        a, b = line.split()
        list_a.append(int(a.strip()))
        list_b.append(int(b.strip()))

    return list_a, list_b


def get_distance_between_values(a: int, b: int) -> int:
    return abs(b - a)


def sort(l: list[int]) -> list[int]:
    l_ = l.copy()
    l_.sort()
    return l_


def get_distance_between_lists(list_a: list[int], list_b: list[int]):
    return sum(
        get_distance_between_values(a, b)
        for a, b in zip(sort(list_a), sort(list_b))
    )
