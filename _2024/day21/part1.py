from _2024.day21 import (
    TYPING_SEQUENCE,
    DirectionalKeyPad,
    DoorKeyPad,
    compute_complexity,
    parse_input,
)
from _2024.load_input import load_input


def get_shortest_path(
    typing_sequences: set[TYPING_SEQUENCE],
) -> TYPING_SEQUENCE:
    return sorted(typing_sequences, key=lambda x: len(x))[0]


def compute_solution(typing_sequences: set[TYPING_SEQUENCE]) -> int:
    door_key_pad = DoorKeyPad()
    directional_key_pad = DirectionalKeyPad()
    solution = 0
    for door_typing_sequence in typing_sequences:
        typing_sequences = door_key_pad.compute_shortest_typing_sequences(
            door_typing_sequence
        )
        for key_pad_step in [
            directional_key_pad,
            directional_key_pad,
            directional_key_pad,
        ]:
            typing_sequences = (
                key_pad_step.compute_typing_sequences_from_typing_sequences(
                    typing_sequences
                )
            )

        directional_keypad_typing_sequences = get_shortest_path(
            typing_sequences
        )
        solution += compute_complexity(
            numeric_keypad_typing_sequences=door_typing_sequence,
            directional_keypad_typing_sequences=(
                directional_keypad_typing_sequences
            ),
        )
    return solution


def main():
    input_data = load_input(21)
    typing_sequences = parse_input(input_data)
    print(compute_solution(typing_sequences))


if __name__ == "__main__":
    main()
