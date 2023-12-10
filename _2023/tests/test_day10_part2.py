import pytest

from _2023.day10 import Map
from .test_day10_part1 import (
    REGULAR_MAP,
    SIMPLE_MAP,
    MORE_COMPLEX_MAP,
    MORE_COMPLEX_LOOP_MAP,
)


@pytest.mark.parametrize(
    "input_data, expected_loop_map",
    [(REGULAR_MAP, SIMPLE_MAP), (MORE_COMPLEX_MAP, MORE_COMPLEX_LOOP_MAP)],
)
def test_map_can_compute_its_loop_map(input_data, expected_loop_map):
    map = Map.from_input(input_data)
    loop_map = map.compute_loop_map()
    assert loop_map.to_str() == expected_loop_map
