from dataclasses import dataclass

MAP = list[list[str]]

POSITION = tuple[int, int]


@dataclass
class Region:
    character: str
    positions: list[POSITION]
    area: int
    perimeter: int

    map: MAP

    @property
    def fence_price(self) -> int:
        return self.perimeter * self.area

    def add_new_position(self, position: POSITION):
        self.positions.append(position)

        self.area += 1

        x, y = position

        cell_up = (x, y - 1)
        cell_left = (x - 1, y)
        cell_down = (x, y + 1)
        cell_right = (x + 1, y)
        other_cells = [cell_up, cell_left, cell_down, cell_right]

        for other_cell in other_cells:
            other_cell_x, other_cell_y = other_cell
            if not in_map(self.map, other_cell):
                self.perimeter += 1
                continue

            other_character = self.map[other_cell_y][other_cell_x]
            if other_character != self.character:
                self.perimeter += 1


def merge_regions(regions: list[Region]) -> Region:
    character = regions[0].character
    map = regions[0].map

    positions = []
    area = 0
    perimeter = 0
    for region in regions:
        positions.extend(region.positions)
        area += region.area
        perimeter += region.perimeter

    return Region(
        character=character,
        positions=positions,
        area=area,
        perimeter=perimeter,
        map=map,
    )


class RegionList(list[Region]):
    def __init__(self, *args, map: MAP):
        super().__init__(*args)
        self.map = map

    def get_region_with(
        self,
        character: str,
        cell_up: POSITION,
        cell_left: POSITION,
    ) -> Region:
        potential_regions = []
        for region in self:
            if character == region.character:
                if cell_up in region.positions:
                    potential_regions.append(region)
                elif cell_left in region.positions:
                    potential_regions.append(region)

        if len(potential_regions) == 1:
            region = potential_regions[0]
        elif len(potential_regions) > 0:
            for region in potential_regions:
                self.remove(region)
            region = merge_regions(potential_regions)
            self.append(region)
        else:
            region = Region(
                map=self.map,
                character=character,
                positions=[],
                area=0,
                perimeter=0,
            )
            self.append(region)

        return region


def in_map(map: MAP, position: POSITION) -> bool:
    map_size = len(map)
    x, y = position
    return 0 <= x < map_size and 0 <= y < map_size


def parse_input(data: str) -> MAP:
    data = data.strip("\n")

    return [[cell for cell in line] for line in data.split("\n")]


def compute_regions(map: MAP) -> list[Region]:
    i = 0
    regions = RegionList(map=map)
    for y, line in enumerate(map):
        for x, character in enumerate(line):
            cell_up = (x, y - 1)
            cell_left = (x - 1, y)

            region = regions.get_region_with(
                character=character,
                cell_up=cell_up,
                cell_left=cell_left,
            )

            region.add_new_position((x, y))
    return sorted(regions, key=lambda region: region.character)
