from functools import reduce

import tqdm
from _2025.day8 import BasePlayground
from _2025.load_input import load_input


class Playground(BasePlayground):
    def compute_solution(self) -> int:
        a, b = self.get_last_connection_pair()
        return a.x * b.x


def main():
    playground = Playground.from_input(load_input(8))
    print(playground.compute_solution())


if __name__ == "__main__":
    main()
