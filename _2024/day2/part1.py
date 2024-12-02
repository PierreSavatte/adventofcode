from _2024.day2 import is_safe, parse_input
from _2024.load_input import load_input


def count_safe_reports(data: str) -> int:
    list_of_reports = parse_input(data)
    return sum(is_safe(report) for report in list_of_reports)


if __name__ == "__main__":
    input_data = load_input(2)
    print(count_safe_reports(input_data))
