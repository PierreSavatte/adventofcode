from dataclasses import dataclass
from typing import Optional

from _2023.utils import transpose_table


def transpose(lines: list[str]):
    table = transpose_table(lines)
    return ["".join(line) for line in table]


@dataclass
class Reflection:
    x: Optional[int]
    y: Optional[int]

    def summarize(self) -> int:
        if self.x is not None:
            return self.x + 1
        if self.y is not None:
            return (self.y + 1) * 100


@dataclass
class Pattern:
    reflection: Reflection
    lines: list[str]

    @classmethod
    def from_data(cls, data: str) -> "Pattern":
        lines = []
        potential_reflections = []
        for i, line in enumerate(data.splitlines()):
            if lines and line == lines[-1]:
                potential_reflections.append(i - 1)
            lines.append(line)

        reflection_line = get_reflection_line(
            lines=lines, potential_reflections=potential_reflections
        )
        if reflection_line is not None:
            reflection = Reflection(y=reflection_line, x=None)
        else:
            columns = transpose(lines)
            reflection_column = get_reflection_line(
                lines=columns, potential_reflections=[]
            )
            if reflection_column is not None:
                reflection = Reflection(x=reflection_column, y=None)
            else:
                raise RuntimeError("Didn't find any reflections")

        return Pattern(reflection=reflection, lines=lines)


def get_reflection_line(
    lines: list[str], potential_reflections: list[int]
) -> Optional[int]:
    if not potential_reflections:
        potential_reflections = range(1, len(lines) - 1)

    for x in potential_reflections:
        is_reflection = True
        for i in range(x + 1):
            current_line = x - i
            expected_reflected_line = x + i + 1
            if expected_reflected_line >= len(lines):
                # Skip lines not in pattern
                continue

            if lines[current_line] != lines[expected_reflected_line]:
                is_reflection = False
                break

        if is_reflection:
            return x


def parse_patterns(data: str) -> list[str]:
    return data.split("\n\n")
