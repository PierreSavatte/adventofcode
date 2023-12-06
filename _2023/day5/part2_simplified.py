from _2023.day5 import Almanach, Page
from _2023.load_input import load_input


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

    locations = []
    for range_number, range in enumerate(almanach.seeds_ranges):
        print(
            f"running computation for {range_number}: {range} (length={range.stop - range.start})"
        )
        for seed_number, seed in enumerate(range):
            location = get_location(almanach.pages, seed)
            locations.append(location)

    return min(locations)


if __name__ == "__main__":
    print(compute_solution(load_input(5)))
