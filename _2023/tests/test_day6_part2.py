from _2023.day6 import Race
from _2023.day6.part2 import compute_solution, parse_input


def test_input_can_be_parsed(get_data):
    race = parse_input(data=get_data("test_file_day6"))
    assert race == Race(time=71530, min_distance=940200)


def test_solution_can_be_computed(get_data):
    assert compute_solution(data=get_data("test_file_day6")) == 71503
