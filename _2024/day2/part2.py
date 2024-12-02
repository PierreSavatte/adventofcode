from enum import Enum

from _2024.day2 import parse_input
from _2024.load_input import load_input


class MonotonicType(Enum):
    STRICTLY_INCREASING = "STRICTLY_INCREASING"
    STRICTLY_DECREASING = "STRICTLY_DECREASING"


def evaluate_monotonic_type(report: list[int]) -> MonotonicType:
    monotonic_types = []
    for a, b in zip(report, report[1:]):
        if a < b:
            monotonic_types.append(MonotonicType.STRICTLY_INCREASING)
        if a > b:
            monotonic_types.append(MonotonicType.STRICTLY_DECREASING)

    strictly_increasing = monotonic_types.count(
        MonotonicType.STRICTLY_INCREASING
    )
    strictly_decreasing = monotonic_types.count(
        MonotonicType.STRICTLY_DECREASING
    )
    if strictly_increasing >= strictly_decreasing:
        return MonotonicType.STRICTLY_INCREASING
    else:
        return MonotonicType.STRICTLY_DECREASING


def is_safe_with_problem_dampener(
    report: list[int], problem_already_fixed=False
) -> bool:
    monotonic_type = evaluate_monotonic_type(report)

    i = 0
    while i + 1 < len(report):
        a = report[i]
        b = report[i + 1]

        problem_detected = False

        # Checking that the levels are monotonic
        if a == b:
            problem_detected = True
        if a < b:
            if monotonic_type == MonotonicType.STRICTLY_DECREASING:
                problem_detected = True
        if a > b:
            if monotonic_type == MonotonicType.STRICTLY_INCREASING:
                problem_detected = True

        # Checking that adjacent levels are safe
        diff = abs(a - b)
        if not (1 <= diff <= 3):
            problem_detected = True

        # Evaluating if the problem (if any) can be fixed
        if problem_detected:
            if not problem_already_fixed:
                sub_report_a = report[0:i] + report[i + 1 :]
                sub_report_b = report[0 : i + 1] + report[i + 2 :]
                return is_safe_with_problem_dampener(
                    sub_report_a, problem_already_fixed=True
                ) or is_safe_with_problem_dampener(
                    sub_report_b, problem_already_fixed=True
                )
            else:
                return False

        i += 1
    return True


def count_safe_reports_with_problem_dampener(data: str) -> int:
    list_of_reports = parse_input(data)
    return sum(
        is_safe_with_problem_dampener(report) for report in list_of_reports
    )


if __name__ == "__main__":
    input_data = load_input(2)
    print(count_safe_reports_with_problem_dampener(input_data))
