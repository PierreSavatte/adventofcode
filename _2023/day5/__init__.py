from dataclasses import dataclass
from typing import Optional


@dataclass
class Mapping:
    destination_start: int
    source_start: int
    length: int

    def map(self, source: int) -> Optional[int]:
        source_range = range(
            self.source_start, self.source_start + self.length + 1
        )
        if source not in source_range:
            return None

        distance_from_source_start = source - self.source_start
        destination = self.destination_start + distance_from_source_start

        return destination


@dataclass
class Page:
    source: str
    destination: str
    mappings: list[Mapping]

    @classmethod
    def from_input(cls, data: str) -> "Page":
        lines = data.split("\n")
        header = lines.pop(0)
        mapping_name, _ = header.split()
        source, destination = mapping_name.split("-to-")

        mappings = []
        for line in lines:
            destination_start, source_start, length = line.split()
            mappings.append(
                Mapping(
                    destination_start=int(destination_start),
                    source_start=int(source_start),
                    length=int(length),
                )
            )

        return Page(
            source=source,
            destination=destination,
            mappings=mappings,
        )

    def map(self, source: int) -> int:
        for mapping in self.mappings:
            destination = mapping.map(source)
            if destination is not None:
                return destination
        # Any source numbers that aren't mapped correspond
        # to the same destination number
        return source


@dataclass
class Almanach:
    seeds: list[int]
    pages: list[Page]

    @classmethod
    def from_input(cls, data: str) -> "Almanach":
        sections = data.split("\n\n")
        seeds_section = sections.pop(0)
        _, seeds_txt = seeds_section.split(": ")
        seeds = [int(seed_str) for seed_str in seeds_txt.split()]

        pages = [Page.from_input(section) for section in sections]

        return Almanach(seeds=seeds, pages=pages)

    def get_page(self, source: str) -> Page:
        for page in self.pages:
            if page.source == source:
                return page

    def map(self, seed: int) -> int:
        source = "seed"
        input = seed
        while source != "location":
            page = self.get_page(source)
            source = page.destination
            input = page.map(input)
        return input

    @property
    def seeds_ranges(self) -> list[range]:
        groups = [self.seeds[i : i + 2] for i in range(0, len(self.seeds), 2)]

        ranges = []
        for start, length in groups:
            ranges.append(range(start, start + length + 1))
        return ranges
