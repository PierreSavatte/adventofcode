from _2023.day18 import DigPlan, Plan
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    dig_plan = DigPlan.from_data(data)
    plan = Plan.from_dig_plan(dig_plan)
    return plan.compute_area()


if __name__ == "__main__":
    print(compute_solution(load_input(18)))
