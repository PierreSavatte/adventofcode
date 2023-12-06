from dataclasses import dataclass

BOAT_STARTING_SPEED = 0
BOAT_SPEED_INCREASE = 1


@dataclass
class Option:
    holding_for: int


@dataclass
class Race:
    time: int
    min_distance: int

    def compute_winning_options(self) -> list[Option]:
        options = []
        for holding_time in range(1, self.time):
            remaining_time = self.time - holding_time
            boat_speed = holding_time * BOAT_SPEED_INCREASE
            distance = boat_speed * remaining_time
            if distance > self.min_distance:
                options.append(Option(holding_for=holding_time))
        return options
