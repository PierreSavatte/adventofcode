from _2021 import aoc_utils

FILE = "input"


class Signal:
    nb_segments = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6,
    }

    def __init__(self, patterns, output):
        self.patterns = patterns
        self.output = output

    @classmethod
    def from_input_file(cls, line):
        raw_patterns, raw_output = line.strip().split(" | ")
        return cls(
            patterns=raw_patterns.split(" "), output=raw_output.split(" ")
        )

    def __eq__(self, other):
        for i, obj in enumerate(other.patterns):
            if self.patterns[i] != obj:
                return False

        for i, obj in enumerate(other.output):
            if self.output[i] != obj:
                return False

        return True

    def count_1_4_7_8(self):
        expected_nb_segments = [
            self.nb_segments[1],
            self.nb_segments[4],
            self.nb_segments[7],
            self.nb_segments[8],
        ]
        result = 0
        for signal in self.output:
            if len(signal) in expected_nb_segments:
                result += 1

        return result


def parse_file(file_path):
    return aoc_utils.parse_file(file_path, line_parser=Signal.from_input_file)


def resolution(signals):
    counter = 0
    for signal in signals:
        counter += signal.count_1_4_7_8()

    return counter


def challenge_resolution():
    signals = parse_file(FILE)
    return resolution(signals)


if __name__ == "__main__":
    print(challenge_resolution())
