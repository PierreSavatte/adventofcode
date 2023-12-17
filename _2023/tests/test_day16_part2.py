from _2023.day16.part2 import compute_solution


def test_solution_can_be_computed(get_data):
    data = get_data("test_file_day16")

    assert compute_solution(data) == 52
