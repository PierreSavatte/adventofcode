import math

from _2023.day5 import Almanach, Page
from _2023.load_input import load_input
from tqdm import tqdm


def get_page(pages: list[Page], source: str) -> Page:
    for page in pages:
        if page.source == source:
            return page


def get_location(pages: list[Page], seed: int) -> int:
    source = "seed"
    input = seed
    while source != "location":
        page = get_page(pages, source)
        for mapping in page.mappings:
            source_range = range(
                mapping.source_start, mapping.source_start + mapping.length + 1
            )
            if input in source_range:
                distance_from_source_start = input - mapping.source_start
                input = mapping.destination_start + distance_from_source_start
                break

        source = page.destination
    return input


def compute_solution(data: str) -> int:
    almanach = Almanach.from_input(data)

    lowest_location = math.inf
    total_number_ranges = len(almanach.seeds_ranges)
    for range_number, range in enumerate(almanach.seeds_ranges, start=1):
        print(
            f"running computation for {range_number}/{total_number_ranges}: "
            f"{range} (length={range.stop - range.start})"
        )
        for seed in tqdm(range):
            location = get_location(almanach.pages, seed)
            if location < lowest_location:
                print(f"got a lower location: {location}")
                lowest_location = location

    return lowest_location


if __name__ == "__main__":
    print(compute_solution(load_input(5)))
