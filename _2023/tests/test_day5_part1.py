import pytest

from _2023.day5 import Almanach, Page, Mapping
from _2023.day5.part1 import compute_solution


def test_page_can_be_parsed():
    page_data = "\n".join(
        [
            "fertilizer-to-water map:",
            "49 53 8",
            "0 11 42",
            "42 0 7",
            "57 7 4",
        ]
    )

    assert Page.from_input(data=page_data) == Page(
        source="fertilizer",
        destination="water",
        mappings=[
            Mapping(destination_start=49, source_start=53, length=8),
            Mapping(destination_start=0, source_start=11, length=42),
            Mapping(destination_start=42, source_start=0, length=7),
            Mapping(destination_start=57, source_start=7, length=4),
        ],
    )


def test_almanach_can_be_parsed(get_data):
    data = get_data("test_file_day5")

    almanach = Almanach.from_input(data)

    page_source_destinations = [
        (page.source, page.destination) for page in almanach.pages
    ]
    assert page_source_destinations == [
        ("seed", "soil"),
        ("soil", "fertilizer"),
        ("fertilizer", "water"),
        ("water", "light"),
        ("light", "temperature"),
        ("temperature", "humidity"),
        ("humidity", "location"),
    ]
    assert almanach.seeds == [79, 14, 55, 13]


@pytest.mark.parametrize(
    "source, expected_destination",
    [
        (0, 0),
        (49, 49),
        (50, 52),
        (51, 53),
        (96, 98),
        (98, 50),
        (99, 51),
    ],
)
def test_page_can_map_source_and_destination_numbers(
    source, expected_destination
):
    page = Page(
        source="seed",
        destination="soil",
        mappings=[
            Mapping(destination_start=50, source_start=98, length=2),
            Mapping(destination_start=52, source_start=50, length=48),
        ],
    )

    assert page.map(source=source) == expected_destination


def test_almanach_can_get_page_for_any_key():
    page_seed_soil = Page(source="seed", destination="soil", mappings=[])
    page_soil_fertilizer = Page(
        source="soil", destination="fertilizer", mappings=[]
    )
    pages = [page_seed_soil, page_soil_fertilizer]
    almanach = Almanach(seeds=[], pages=pages)
    assert almanach.get_page(source="seed") == page_seed_soil
    assert almanach.get_page(source="soil") == page_soil_fertilizer


@pytest.mark.parametrize(
    "seed, expected_mapping",
    [
        (79, 82),
        (14, 43),
        (55, 86),
        (13, 35),
    ],
)
def test_almanach_can_map_seed_to_location(get_data, seed, expected_mapping):
    data = get_data("test_file_day5")
    almanach = Almanach.from_input(data)

    return almanach.map(seed=seed) == expected_mapping


def test_solution_can_be_computed(get_data):
    assert compute_solution(get_data("test_file_day5")) == 35
