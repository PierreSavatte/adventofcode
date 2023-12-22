from _2023.day18 import DigPlan, Order, Direction


def test_input_can_be_parsed(get_data):
    data = get_data("test_file_day18")
    assert DigPlan.from_data(data)[:3] == [
        Order(direction=Direction.RIGHT, length=6, color="#70c710"),
        Order(direction=Direction.DOWN, length=5, color="#0dc571"),
        Order(direction=Direction.LEFT, length=2, color="#5713f0"),
    ]
