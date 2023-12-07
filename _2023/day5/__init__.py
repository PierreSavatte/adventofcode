from dataclasses import dataclass
from typing import Optional


@dataclass
class Mapping:
    destination_start: int
    source_start: int
    length: int

    @property
    def source_range(self):
        return range(self.source_start, self.source_start + self.length + 1)

    @property
    def destination_range(self):
        return range(self.source_start, self.source_start + self.length + 1)

    def map(self, source: int) -> Optional[int]:
        if source not in self.source_range:
            return None

        distance_from_source_start = source - self.source_start
        destination = self.destination_start + distance_from_source_start

        return destination

    def revert_map(self, destination: int) -> Optional[int]:
        if destination not in self.destination_range:
            return None

        distance_from_destination_start = destination - self.destination_start
        source = self.source_start + distance_from_destination_start

        return source


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

    def revert_map(self, destination: int) -> int:
        for mapping in self.mappings:
            source = mapping.revert_map(destination)
            if source is not None:
                return source
        # Any source numbers that aren't mapped correspond
        # to the same destination number
        return destination


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

    def get_page_from_destination(self, destination: str) -> Page:
        for page in self.pages:
            if page.destination == destination:
                return page

    def map(self, seed: int, source: str = "seed") -> int:
        input = seed
        while source != "location":
            page = self.get_page(source)
            source = page.destination
            input = page.map(input)
        return input

    def revert_map(self, input: int, source: str = "location"):
        while source != "seed":
            page = self.get_page_from_destination(source)
            source = page.source
            input = page.revert_map(input)
        return input

    @property
    def seeds_ranges(self) -> list[range]:
        groups = [self.seeds[i : i + 2] for i in range(0, len(self.seeds), 2)]

        ranges = []
        for start, length in groups:
            ranges.append(range(start, start + length + 1))
        return ranges
