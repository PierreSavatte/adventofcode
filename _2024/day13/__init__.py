from dataclasses import dataclass

POSITION = tuple[int, int]
DELTA_POSITION = tuple[int, int]
NB_PRESS = tuple[int, int]


class Unsolvable(Exception):
    ...


@dataclass
class Machine:
    prize: POSITION
    button_a: DELTA_POSITION
    button_b: DELTA_POSITION

    def get_prize(self) -> NB_PRESS:
        x, y = self.prize
        delta_x_a, delta_y_a = self.button_a
        delta_x_b, delta_y_b = self.button_b

        max_nb_press_b = min(x // delta_x_b, y // delta_y_b)

        max_nb_press_b = min(max_nb_press_b, 100)

        for nb_press_b in range(max_nb_press_b, 0, -1):

            rest_x = x - nb_press_b * delta_x_b
            rest_y = y - nb_press_b * delta_y_b

            nb_press_a_to_solve_x = rest_x // delta_x_a
            nb_press_a_to_solve_y = rest_y // delta_y_a

            if nb_press_a_to_solve_x != nb_press_a_to_solve_y:
                continue
            nb_press_a = min(nb_press_a_to_solve_x, 100)

            rest_x = rest_x - nb_press_a * delta_x_a
            rest_y = rest_y - nb_press_a * delta_y_a

            if rest_x != 0 or rest_y != 0:
                continue
            return nb_press_a_to_solve_x, nb_press_b

        raise Unsolvable(self)


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
