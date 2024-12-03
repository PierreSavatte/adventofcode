from _2024.day3 import compute_solution, parse_input
from _2024.load_input import load_input


def remove_ignored_part_of_input(data: str) -> str:
    while "don't()" in data:
        start_i = data.find("don't()")

        do_position = data[start_i:].find("do()")
        if do_position == -1:
            data = data[:start_i]
        else:
            end_i = data[start_i:].find("do()") + 4 + start_i
            data = data[:start_i] + data[end_i:]

    return data


if __name__ == "__main__":
    input_data = load_input(3)
    new_input_data = remove_ignored_part_of_input(input_data)
    groups = parse_input(new_input_data)
    print(compute_solution(groups))
