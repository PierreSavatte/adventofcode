from day1.part2 import compute_window


def test_windows_are_correctly_computed():
    depth_series = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    result = compute_window(depth_series)

    assert result == [607, 618, 618, 617, 647, 716, 769, 792]
