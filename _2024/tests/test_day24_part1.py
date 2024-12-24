import pytest
from _2024.day24 import Computer, Gate, Operation, parse_input
from _2024.day24.part1 import compute_solution

TEST_INPUT = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
"""

COMPUTER = Computer(
    data={
        "x00": True,
        "x01": False,
        "x02": True,
        "x03": True,
        "x04": False,
        "y00": True,
        "y01": True,
        "y02": True,
        "y03": True,
        "y04": True,
    },
    gates=[
        Gate(operation=Operation.XOR, inputs=["ntg", "fgs"], output="mjb"),
        Gate(operation=Operation.OR, inputs=["y02", "x01"], output="tnw"),
        Gate(operation=Operation.OR, inputs=["kwq", "kpj"], output="z05"),
        Gate(operation=Operation.OR, inputs=["x00", "x03"], output="fst"),
        Gate(operation=Operation.XOR, inputs=["tgd", "rvg"], output="z01"),
        Gate(operation=Operation.OR, inputs=["vdt", "tnw"], output="bfw"),
        Gate(operation=Operation.AND, inputs=["bfw", "frj"], output="z10"),
        Gate(operation=Operation.OR, inputs=["ffh", "nrd"], output="bqk"),
        Gate(operation=Operation.AND, inputs=["y00", "y03"], output="djm"),
        Gate(operation=Operation.OR, inputs=["y03", "y00"], output="psh"),
        Gate(operation=Operation.OR, inputs=["bqk", "frj"], output="z08"),
        Gate(operation=Operation.OR, inputs=["tnw", "fst"], output="frj"),
        Gate(operation=Operation.AND, inputs=["gnj", "tgd"], output="z11"),
        Gate(operation=Operation.XOR, inputs=["bfw", "mjb"], output="z00"),
        Gate(operation=Operation.OR, inputs=["x03", "x00"], output="vdt"),
        Gate(operation=Operation.AND, inputs=["gnj", "wpb"], output="z02"),
        Gate(operation=Operation.AND, inputs=["x04", "y00"], output="kjc"),
        Gate(operation=Operation.OR, inputs=["djm", "pbm"], output="qhw"),
        Gate(operation=Operation.AND, inputs=["nrd", "vdt"], output="hwm"),
        Gate(operation=Operation.AND, inputs=["kjc", "fst"], output="rvg"),
        Gate(operation=Operation.OR, inputs=["y04", "y02"], output="fgs"),
        Gate(operation=Operation.AND, inputs=["y01", "x02"], output="pbm"),
        Gate(operation=Operation.OR, inputs=["ntg", "kjc"], output="kwq"),
        Gate(operation=Operation.XOR, inputs=["psh", "fgs"], output="tgd"),
        Gate(operation=Operation.XOR, inputs=["qhw", "tgd"], output="z09"),
        Gate(operation=Operation.OR, inputs=["pbm", "djm"], output="kpj"),
        Gate(operation=Operation.XOR, inputs=["x03", "y03"], output="ffh"),
        Gate(operation=Operation.XOR, inputs=["x00", "y04"], output="ntg"),
        Gate(operation=Operation.OR, inputs=["bfw", "bqk"], output="z06"),
        Gate(operation=Operation.XOR, inputs=["nrd", "fgs"], output="wpb"),
        Gate(operation=Operation.XOR, inputs=["frj", "qhw"], output="z04"),
        Gate(operation=Operation.OR, inputs=["bqk", "frj"], output="z07"),
        Gate(operation=Operation.OR, inputs=["y03", "x01"], output="nrd"),
        Gate(operation=Operation.AND, inputs=["hwm", "bqk"], output="z03"),
        Gate(operation=Operation.XOR, inputs=["tgd", "rvg"], output="z12"),
        Gate(operation=Operation.OR, inputs=["tnw", "pbm"], output="gnj"),
    ],
)


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == COMPUTER


@pytest.mark.parametrize(
    "operation, inputs, result",
    [
        # Operation.AND
        (Operation.AND, {"input_1": False, "input_2": False}, False),
        (Operation.AND, {"input_1": True, "input_2": False}, False),
        (Operation.AND, {"input_1": False, "input_2": True}, False),
        (Operation.AND, {"input_1": True, "input_2": True}, True),
        # Operation.OR
        (Operation.OR, {"input_1": False, "input_2": False}, False),
        (Operation.OR, {"input_1": True, "input_2": False}, True),
        (Operation.OR, {"input_1": False, "input_2": True}, True),
        (Operation.OR, {"input_1": True, "input_2": True}, True),
        # Operation.XOR
        (Operation.XOR, {"input_1": False, "input_2": False}, False),
        (Operation.XOR, {"input_1": True, "input_2": False}, True),
        (Operation.XOR, {"input_1": False, "input_2": True}, True),
        (Operation.XOR, {"input_1": True, "input_2": True}, False),
    ],
)
def test_operation_can_be_computed(operation, inputs, result):
    computer = Computer(
        data=inputs,
        gates=[
            Gate(
                operation=operation,
                inputs=["input_1", "input_2"],
                output="output",
            ),
        ],
    )

    computer.run()

    assert computer.data["output"] == result


def test_computer_can_run_all_operations():
    computer = COMPUTER.copy()

    computer.run()

    assert computer.data == {
        "bfw": True,
        "bqk": True,
        "djm": True,
        "ffh": False,
        "fgs": True,
        "frj": True,
        "fst": True,
        "gnj": True,
        "hwm": True,
        "kjc": False,
        "kpj": True,
        "kwq": False,
        "mjb": True,
        "nrd": True,
        "ntg": False,
        "pbm": True,
        "psh": True,
        "qhw": True,
        "rvg": False,
        "tgd": False,
        "tnw": True,
        "vdt": True,
        "wpb": False,
        "x00": True,
        "x01": False,
        "x02": True,
        "x03": True,
        "x04": False,
        "y00": True,
        "y01": True,
        "y02": True,
        "y03": True,
        "y04": True,
        "z00": False,
        "z01": False,
        "z02": False,
        "z03": True,
        "z04": False,
        "z05": True,
        "z06": True,
        "z07": True,
        "z08": True,
        "z09": True,
        "z10": True,
        "z11": False,
        "z12": False,
    }


def test_computer_output_can_be_read():
    computer = Computer(
        data={
            "z00": False,
            "z01": False,
            "z02": False,
            "z03": True,
            "z04": False,
            "z05": True,
            "z06": True,
            "z07": True,
            "z08": True,
            "z09": True,
            "z10": True,
            "z11": False,
            "z12": False,
        },
        gates=[],
    )

    assert computer.read_output() == 2024


def test_solution_can_be_computed():
    computer = COMPUTER.copy()
    assert compute_solution(computer) == 2024
