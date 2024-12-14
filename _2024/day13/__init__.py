from dataclasses import dataclass

POSITION = tuple[int, int]
DELTA_POSITION = tuple[int, int]
NB_PRESS = tuple[int, int]


class Unsolvable(Exception):
    ...


@dataclass
class Matrix_2_2:
    # |-   -|
    # | a b |
    # | c d |
    # |-   -|
    a: float
    b: float
    c: float
    d: float

    @property
    def determinant(self) -> float:
        return self.a * self.d - self.c * self.b


@dataclass
class Machine:
    prize: POSITION
    button_a: DELTA_POSITION
    button_b: DELTA_POSITION

    def get_prize(self, correction_applied: bool = False) -> NB_PRESS:
        # https://en.wikipedia.org/wiki/System_of_linear_equations#Matrix_solution

        x, y = self.prize
        if correction_applied:
            x += 10000000000000
            y += 10000000000000

        delta_x_a, delta_y_a = self.button_a
        delta_x_b, delta_y_b = self.button_b

        matrix_a = Matrix_2_2(
            a=delta_x_a, b=delta_x_b, c=delta_y_a, d=delta_y_b
        )

        nb_pressed_a = int(
            (matrix_a.d * x - matrix_a.b * y) / matrix_a.determinant
        )
        nb_pressed_b = int(
            (-matrix_a.c * x + matrix_a.a * y) / matrix_a.determinant
        )

        # Verification
        landing_x = delta_x_a * nb_pressed_a + delta_x_b * nb_pressed_b
        landing_y = delta_y_a * nb_pressed_a + delta_y_b * nb_pressed_b
        if landing_x != x or landing_y != y:
            raise Unsolvable()

        return int(nb_pressed_a), int(nb_pressed_b)


def parse_line_data(
    data: str, position_split_character: str
) -> DELTA_POSITION:
    delta_data = data.split(": ")[1]
    x_data, y_data = delta_data.split(", ")

    x_delta = int(x_data.split(position_split_character)[1])
    y_delta = int(y_data.split(position_split_character)[1])

    return x_delta, y_delta


def parse_input(data: str) -> list[Machine]:
    data = data.strip("\n")

    machines = []
    machines_data = data.split("\n\n")
    for machine_data in machines_data:
        button_a_data, button_b_data, prize_data = machine_data.split("\n")

        button_a = parse_line_data(button_a_data, position_split_character="+")
        button_b = parse_line_data(button_b_data, position_split_character="+")
        prize = parse_line_data(prize_data, position_split_character="=")

        machines.append(
            Machine(
                button_a=button_a,
                button_b=button_b,
                prize=prize,
            )
        )

    return machines
