from _2024.day22.part2 import get_best_sequence, get_price_differences


def test_price_difference_can_be_computed_from_secret_number_sequence():
    secret_numbers_sequence = [
        123,
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
    ]
    assert get_price_differences(secret_numbers_sequence) == [
        -3,
        6,
        -1,
        -1,
        0,
        2,
        -2,
        0,
        -2,
    ]


def test_change_in_price_can_be_computed():
    sequence, score = get_best_sequence([1, 2, 3, 2024])
    assert sequence == (-2, 1, -1, 3)
    assert score == 23
