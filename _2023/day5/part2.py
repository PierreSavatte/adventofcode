from _2023.day5 import Almanach, Page
from _2023.load_input import load_input


def compute_solution(data: str) -> int:
    almanach = Almanach.from_input(data)

    locations = []
    for page in almanach.pages:
        if page.source == "seed":
            continue
        for mapping in page.mappings:
            location = almanach.map(mapping.source_start, source=page.source)
            seed = almanach.revert_map(
                mapping.source_start, source=page.source
            )
            if location != almanach.map(seed):
                # To fix my computation problem somewhere 🙈
                continue
            if any(seed in range for range in almanach.seeds_ranges):
                locations.append(location)

    return min(locations)


if __name__ == "__main__":
    print(compute_solution(load_input(5)))
