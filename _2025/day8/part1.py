from functools import reduce

import tqdm
from _2025.day8 import BasePlayground
from _2025.load_input import load_input


class Playground(BasePlayground):
    def compute_solution(self, nb_connections: int) -> int:
        for _ in tqdm.tqdm(range(nb_connections)):
            self.make_next_connection()

        group_sizes = self.get_group_sizes()
        _3_largest_group_sizes = group_sizes[:3]
        return reduce(lambda a, b: a * b, _3_largest_group_sizes)


def main():
    playground = Playground.from_input(load_input(8))
    print(playground.compute_solution(nb_connections=1000))


if __name__ == "__main__":
    main()
