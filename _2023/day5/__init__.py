from dataclasses import dataclass
from typing import Optional


@dataclass
class Range:
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
    ranges: list[Range]

    @classmethod
    def from_input(cls, data: str) -> "Page":
        lines = data.split("\n")
        header = lines.pop(0)
        mapping_name, _ = header.split()
        source, destination = mapping_name.split("-to-")

        ranges = []
        for line in lines:
            destination_start, source_start, length = line.split()
            ranges.append(
                Range(
                    destination_start=int(destination_start),
                    source_start=int(source_start),
                    length=int(length),
                )
            )

        return Page(
            source=source,
            destination=destination,
            ranges=ranges,
        )

    def map(self, source: int) -> int:
        for range in self.ranges:
            mapping = range.map(source)
            if mapping is not None:
                return mapping
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

