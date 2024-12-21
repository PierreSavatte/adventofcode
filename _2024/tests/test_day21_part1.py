import pytest
from _2024.day21 import DirectionalKeyPad, DoorKeyPad, compute_complexity
from _2024.day21.part1 import compute_solution


def test_shortest_typing_route_can_be_computed():
    typing_sequences = DoorKeyPad().compute_shortest_typing_sequences("029A")

    assert typing_sequences == {
        "<A^A^>^AvvvA",
        "<A^A>^^AvvvA",
        "<A^A^^>AvvvA",
    }


def test_typing_route_for_directional_key_pad_can_be_computed():
    typing_sequences = DoorKeyPad().compute_shortest_typing_sequences("029A")
    typing_sequences = (
        DirectionalKeyPad().compute_typing_sequences_from_typing_sequences(
            typing_sequences
        )
    )
    assert "v<<A>>^A<A>AvA<^AA>A<vAAA>^A" in typing_sequences


@pytest.mark.parametrize(
    "code, expected_typing_sequence",
    [
        (
            "029A",
            "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
        ),
        (
            "980A",
            "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
        ),
        (
            "179A",
            "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
        ),
        (
            "456A",
            "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
        ),
        (
            "379A",
            "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
        ),
    ],
)
def test_typing_route_for_sub_directional_key_pad_can_be_computed(
    code, expected_typing_sequence
):
    door_key_pad = DoorKeyPad()
    directional_key_pad = DirectionalKeyPad()

    typing_sequences = door_key_pad.compute_shortest_typing_sequences(code)
    typing_sequences = (
        directional_key_pad.compute_typing_sequences_from_typing_sequences(
            typing_sequences
        )
    )
    typing_sequences = (
        directional_key_pad.compute_typing_sequences_from_typing_sequences(
            typing_sequences
        )
    )

    assert expected_typing_sequence in typing_sequences


def test_complexity_can_be_computed():
    assert (
        compute_complexity(
            "029A",
            "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
        )
        == 68 * 29
    )


def test_solution_can_be_computed():
    assert compute_solution({"029A", "980A", "179A", "456A", "379A"}) == 126384
