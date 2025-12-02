from _2025.load_input import load_input


def parse_id_ranges(input: str) -> list[tuple[int, int]]:
    ids_tuple_list = input.strip().split(",")
    id_ranges = []
    for ids_tuple in ids_tuple_list:
        start, end = ids_tuple.split("-")
        id_ranges.append((int(start), int(end)))
    return id_ranges


def is_invalid_id(id: int) -> bool:
    id_str = str(id)
    i = len(id_str) // 2
    return id_str[:i] == id_str[i:]


def get_invalid_ids(start: int, end: int) -> list[int]:
    return [id for id in range(start, end + 1) if is_invalid_id(id)]


def compute_invalid_ids_sum(ids_tuple_list: list[tuple[int, int]]):
    invalid_ids = []
    for ids_tuple in ids_tuple_list:
        invalid_ids.extend(get_invalid_ids(*ids_tuple))
    return sum(invalid_ids)


def main():
    ids_tuple_list = parse_id_ranges(load_input(2))
    result = compute_invalid_ids_sum(ids_tuple_list)
    print(result)


if __name__ == "__main__":
    main()
