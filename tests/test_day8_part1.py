import os

import pytest
from day8.part1 import parse_file, Signal, resolution


@pytest.fixture
def expected_signals():
    return [
        Signal(
            patterns=[
                "be",
                "cfbegad",
                "cbdgef",
                "fgaecd",
                "cgeb",
                "fdcge",
                "agebfd",
                "fecdb",
                "fabcd",
                "edb",
            ],
            output=["fdgacbe", "cefdb", "cefbgd", "gcbe"],
        ),
        Signal(
            patterns=[
                "edbfga",
                "begcd",
                "cbg",
                "gc",
                "gcadebf",
                "fbgde",
                "acbgfd",
                "abcde",
                "gfcbed",
                "gfec",
            ],
            output=["fcgedb", "cgb", "dgebacf", "gc"],
        ),
        Signal(
            patterns=[
                "fgaebd",
                "cg",
                "bdaec",
                "gdafb",
                "agbcfd",
                "gdcbef",
                "bgcad",
                "gfac",
                "gcb",
                "cdgabef",
            ],
            output=["cg", "cg", "fdcagb", "cbg"],
        ),
        Signal(
            patterns=[
                "fbegcd",
                "cbd",
                "adcefb",
                "dageb",
                "afcb",
                "bc",
                "aefdc",
                "ecdab",
                "fgdeca",
                "fcdbega",
            ],
            output=["efabcd", "cedba", "gadfec", "cb"],
        ),
        Signal(
            patterns=[
                "aecbfdg",
                "fbg",
                "gf",
                "bafeg",
                "dbefa",
                "fcge",
                "gcbea",
                "fcaegb",
                "dgceab",
                "fcbdga",
            ],
            output=["gecf", "egdcabf", "bgf", "bfgea"],
        ),
        Signal(
            patterns=[
                "fgeab",
                "ca",
                "afcebg",
                "bdacfeg",
                "cfaedg",
                "gcfdb",
                "baec",
                "bfadeg",
                "bafgc",
                "acf",
            ],
            output=["gebdcfa", "ecba", "ca", "fadegcb"],
        ),
        Signal(
            patterns=[
                "dbcfg",
                "fgd",
                "bdegcaf",
                "fgec",
                "aegbdf",
                "ecdfab",
                "fbedc",
                "dacgb",
                "gdcebf",
                "gf",
            ],
            output=["cefg", "dcbef", "fcge", "gbcadfe"],
        ),
        Signal(
            patterns=[
                "bdfegc",
                "cbegaf",
                "gecbf",
                "dfcage",
                "bdacg",
                "ed",
                "bedf",
                "ced",
                "adcbefg",
                "gebcd",
            ],
            output=["ed", "bcgafe", "cdgba", "cbgef"],
        ),
        Signal(
            patterns=[
                "egadfb",
                "cdbfeg",
                "cegd",
                "fecab",
                "cgb",
                "gbdefca",
                "cg",
                "fgcdab",
                "egfdb",
                "bfceg",
            ],
            output=["gbdfcae", "bgc", "cg", "cgb"],
        ),
        Signal(
            patterns=[
                "gcafb",
                "gcf",
                "dcaebfg",
                "ecagb",
                "gf",
                "abcdeg",
                "gaef",
                "cafbge",
                "fdbac",
                "fegbdc",
            ],
            output=["fgae", "cfgab", "fg", "bagce"],
        ),
    ]


def test_file_is_parsed_correctly(expected_signals):
    data = parse_file(os.path.join("data", "test_file_day8"))

    assert data == expected_signals


def test_puzzle_is_resolved(expected_signals):
    result = resolution(expected_signals)

    assert result == 26
