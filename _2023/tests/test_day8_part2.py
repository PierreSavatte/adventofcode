from _2023.day8 import parse_input
from _2023.day8.part2 import compute_solution
from _2023.load_input import load_input


def test_map_can_give_the_starting_nodes(get_data):
    map = parse_input(get_data("test_file_day8_part2"))

    assert map.starting_nodes == ["11A", "22A"]


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day8_part2")) == 6


def test_end_nodes_can_be_computed(get_data):
    map = parse_input(get_data("test_file_day8_part2"))

    assert map.ending_nodes == ["11Z", "22Z"]


def test_end_nodes_for_puzzle_can_be_computed(get_data):
    map = parse_input(load_input(8))

    assert map.ending_nodes == ["CPZ", "ZZZ", "FPZ", "DPZ", "MLZ", "MTZ"]
