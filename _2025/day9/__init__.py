from functools import cache

Point = tuple[int, int]


def parse_input(input: str) -> list[Point]:
    return [  # type: ignore
        tuple(map(int, line.split(","))) for line in input.strip().splitlines()
    ]


@cache
def compute_area(a: Point, b: Point) -> int:
    a_x, a_y = a
    b_x, b_y = b

    height = abs(a_x - b_x) + 1
    width = abs(a_y - b_y) + 1

    return int(height * width)


def find_largest_rectangle(point: list[Point]) -> tuple[Point, Point]:
    cache = {}
    for i, a in enumerate(point):
        for b in point[: i + 1]:
            d = compute_area(a, b)
            if cache.get(d) is None:
                cache[d] = (a, b)

    max_distance = max(cache.keys())
    return cache[max_distance]
