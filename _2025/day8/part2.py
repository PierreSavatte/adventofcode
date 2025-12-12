import tqdm
from _2025.day8 import BasePlayground, Position
from _2025.load_input import load_input


class Playground(BasePlayground):
    def get_last_connection_pair(self) -> tuple[Position, Position]:
        progress_bar = tqdm.tqdm(total=len(self.positions))
        while len(self.groups) > 1:
            closest_boxes = self.pop_closest_boxes()
            has_linked_boxes = self.update_groups(closest_boxes)

            if has_linked_boxes:
                progress_bar.update()
        return closest_boxes

    def compute_solution(self) -> int:
        a, b = self.get_last_connection_pair()
        return a.x * b.x


def main():
    playground = Playground.from_input(load_input(8))
    print(playground.compute_solution())


if __name__ == "__main__":
    main()
