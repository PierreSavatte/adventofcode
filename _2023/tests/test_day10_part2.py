import pytest

from _2023.day10 import Map
from _2023.day10.part2 import compute_solution
from .test_day10_part1 import (
    REGULAR_MAP,
    SIMPLE_MAP,
    MORE_COMPLEX_MAP,
    MORE_COMPLEX_LOOP_MAP,
)


SIMPLE_LOOP_MAP = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
ENCLOSED_SIMPLE_LOOP_MAP = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|II|.|II|.
.L--J.L--J.
..........."""

LOOP_MAP = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""
ENCLOSED_LOOP_MAP = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""

COMPLEX_LOOP_MAP = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
ENCLOSED_COMPLEX_LOOP_MAP = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJIL-7..
L--J.L7IIILJS7F-7L7.
....F-JIIF7FJ|L7L7L7
....L7IF7||L7|IL7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""


@pytest.mark.parametrize(
    "input_data, expected_loop_map",
    [(REGULAR_MAP, SIMPLE_MAP), (MORE_COMPLEX_MAP, MORE_COMPLEX_LOOP_MAP)],
)
def test_map_can_compute_its_loop_map(input_data, expected_loop_map):
    map = Map.from_input(input_data)
    loop_map = map.compute_loop_map()
    assert loop_map.to_str() == expected_loop_map


@pytest.mark.parametrize(
    "input_data, expected_enclosed_map",
    [
        (SIMPLE_LOOP_MAP, ENCLOSED_SIMPLE_LOOP_MAP),
        (LOOP_MAP, ENCLOSED_LOOP_MAP),
        (COMPLEX_LOOP_MAP, ENCLOSED_COMPLEX_LOOP_MAP),
    ],
)
def test_map_can_compute_enclosed_map(input_data, expected_enclosed_map):
    map = Map.from_input(input_data)

    assert map.compute_enclosed_map().to_str() == expected_enclosed_map


@pytest.mark.parametrize(
    "input_data, expected_enclosed_tiles",
    [(SIMPLE_LOOP_MAP, 4), (LOOP_MAP, 4), (COMPLEX_LOOP_MAP, 8)],
)
def test_map_can_compute_enclosed_tiles(input_data, expected_enclosed_tiles):
    map = Map.from_input(input_data)

    assert map.compute_enclosed_tiles() == expected_enclosed_tiles


@pytest.mark.parametrize(
    "input_data, expected_solution",
    [(SIMPLE_LOOP_MAP, 4), (LOOP_MAP, 4), (COMPLEX_LOOP_MAP, 8)],
)
def test_solution_can_be_computed(input_data, expected_solution):
    assert compute_solution(input_data) == expected_solution
