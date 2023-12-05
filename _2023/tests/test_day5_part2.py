from _2023.day5.part2 import compute_solution


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day5")) == 46
