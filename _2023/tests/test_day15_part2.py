from _2023.day15.part2 import Boxes, Lens, compute_solution


def test_executing_command_gives_the_expected_result():
    boxes = Boxes()

    boxes.run_command("rn=1")
    assert boxes == [
        [Lens(label="rn", focal=1)],
        *[[] for _ in range(1, 256)],
    ]

    boxes.run_command("cm-")
    assert boxes == [
        [Lens(label="rn", focal=1)],
        *[[] for _ in range(1, 256)],
    ]

    boxes.run_command("qp=3")
    assert boxes == [
        [Lens(label="rn", focal=1)],
        [Lens(label="qp", focal=3)],
        *[[] for _ in range(2, 256)],
    ]

    boxes.run_command("cm=2")
    assert boxes == [
        [Lens(label="rn", focal=1), Lens(label="cm", focal=2)],
        [Lens(label="qp", focal=3)],
        *[[] for _ in range(2, 256)],
    ]

    boxes.run_command("qp-")
    assert boxes == [
        [Lens(label="rn", focal=1), Lens(label="cm", focal=2)],
        *[[] for _ in range(1, 256)],
    ]

    boxes.run_command("pc=4")
    assert boxes == [
        [Lens(label="rn", focal=1), Lens(label="cm", focal=2)],
        [],
        [],
        [Lens(label="pc", focal=4)],
        *[[] for _ in range(4, 256)],
    ]

    boxes.run_command("ot=9")
    assert boxes == [
        [Lens(label="rn", focal=1), Lens(label="cm", focal=2)],
        [],
        [],
        [Lens(label="pc", focal=4), Lens(label="ot", focal=9)],
        *[[] for _ in range(4, 256)],
    ]

    boxes.run_command("ab=5")
    assert boxes == [
        [Lens(label="rn", focal=1), Lens(label="cm", focal=2)],
        [],
        [],
        [
            Lens(label="pc", focal=4),
            Lens(label="ot", focal=9),
            Lens(label="ab", focal=5),
        ],
        *[[] for _ in range(4, 256)],
    ]

    boxes.run_command("pc-")
    assert boxes == [
        [Lens(label="rn", focal=1), Lens(label="cm", focal=2)],
        [],
        [],
        [Lens(label="ot", focal=9), Lens(label="ab", focal=5)],
        *[[] for _ in range(4, 256)],
    ]

    boxes.run_command("pc=6")
    assert boxes == [
        [Lens(label="rn", focal=1), Lens(label="cm", focal=2)],
        [],
        [],
        [
            Lens(label="ot", focal=9),
            Lens(label="ab", focal=5),
            Lens(label="pc", focal=6),
        ],
        *[[] for _ in range(4, 256)],
    ]

    boxes.run_command("ot=7")
    assert boxes == [
        [Lens(label="rn", focal=1), Lens(label="cm", focal=2)],
        [],
        [],
        [
            Lens(label="ot", focal=7),
            Lens(label="ab", focal=5),
            Lens(label="pc", focal=6),
        ],
        *[[] for _ in range(4, 256)],
    ]


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day15")) == 145
