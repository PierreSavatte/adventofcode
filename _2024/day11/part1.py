import time

from _2024.day11 import change, parse_input
from _2024.load_input import load_input
from tqdm import tqdm


def compute_solution(stones: list[int], nb_change: int) -> int:
    progress_bar = tqdm(
        total=nb_change,
        postfix={
            "nb_stones": len(stones),
            "last_iteration_time": f"{0} seconds",
        },
    )
    for i in range(nb_change):
        now = time.time()
        stones = change(stones)
        last_iteration_time = time.time() - now
        progress_bar.set_postfix(
            {
                "nb_stones": len(stones),
                "last_iteration_time": f"{last_iteration_time:.4f} seconds",
            }
        )
        progress_bar.update(1)
    progress_bar.close()
    return len(stones)


def main():
    input_data = load_input(11)
    stones = parse_input(input_data)
    print(compute_solution(stones, nb_change=25))


if __name__ == "__main__":
    main()
