from dataclasses import dataclass, field
from typing import Optional

MAP = list[list[str]]

POSITION = tuple[int, int]


@dataclass
class Side:
    x_range: list[int]
    y_range: list[int]


def merge_sides(side_a: Side, side_b: Side) -> Optional[Side]:
    a_is_horizontal = len(side_a.x_range) > 1
    a_is_vertical = len(side_a.y_range) > 1
    if (
        # Not one of the two
        not (a_is_horizontal or a_is_vertical)
    ) or (
        # Both
        a_is_horizontal
        and a_is_vertical
    ):
        raise RuntimeError("The ranges are incorrect, cannot merge sides")

    b_is_horizontal = len(side_b.x_range) > 1
    b_is_vertical = len(side_b.y_range) > 1
    if (
        # Not one of the two
        not (b_is_horizontal or b_is_vertical)
    ) or (
        # Both
        b_is_horizontal
        and b_is_vertical
    ):
        raise RuntimeError("The ranges are incorrect, cannot merge sides")

    if not (
        (a_is_horizontal and b_is_horizontal)
        or (a_is_vertical and b_is_vertical)
    ):
        # The sides are orthogonal
        return None

    if a_is_vertical and b_is_vertical:
        a_range = side_a.y_range
        b_range = side_b.y_range

        if side_a.x_range != side_b.x_range:
            # Not talking about the same side
            return None

        other_range = side_a.x_range
        attr_name = "y_range"
        other_attr_name = "x_range"
    elif a_is_horizontal and b_is_horizontal:
        a_range = side_a.x_range
        b_range = side_b.x_range

        if side_a.y_range != side_b.y_range:
            # Not talking about the same side
            return None

        other_range = side_a.y_range
        attr_name = "x_range"
        other_attr_name = "y_range"
    else:
        return None

    is_continuous = a_range[1] == b_range[0] or b_range[1] == a_range[0]
    if is_continuous:
        all_values = [*a_range, *b_range]
        maximum = max(all_values)
        minimum = min(all_values)
        new_side = Side(x_range=[], y_range=[])

        setattr(new_side, attr_name, [minimum, maximum])
        setattr(new_side, other_attr_name, other_range)
        return new_side


@dataclass
class Region:
    character: str
    positions: list[POSITION]
    area: int
    perimeter: int

    map: MAP

    sides: list[Side] = field(default_factory=list)

    @property
    def fence_price(self) -> int:
        return self.perimeter * self.area

    @property
    def fence_price_including_bulk_discount(self) -> int:
        return len(self.sides) * self.area

    def add_new_side(self, side: Side):
        new_side = None
        for other_side in self.sides:
            new_side = merge_sides(side, other_side)
            if new_side:
                self.sides.remove(other_side)
                break

        if not new_side:
            new_side = side

        self.sides.append(new_side)

    def add_new_position(self, position: POSITION):
        self.positions.append(position)

        self.area += 1

        x, y = position

        cell_up = (x, y - 1)
        side_up = Side(x_range=[x, x + 1], y_range=[y])
        cell_left = (x - 1, y)
        side_left = Side(x_range=[x], y_range=[y, y + 1])
        cell_down = (x, y + 1)
        side_down = Side(x_range=[x, x + 1], y_range=[y + 1])
        cell_right = (x + 1, y)
        side_right = Side(x_range=[x + 1], y_range=[y, y + 1])

        for other_cell, side in [
            (cell_up, side_up),
            (cell_left, side_left),
            (cell_down, side_down),
            (cell_right, side_right),
        ]:
            other_cell_x, other_cell_y = other_cell
            if not in_map(self.map, other_cell):
                self.perimeter += 1
                self.add_new_side(side)
                continue

            other_character = self.map[other_cell_y][other_cell_x]
            if other_character != self.character:
                self.perimeter += 1
                self.add_new_side(side)


def merge_regions(regions: list[Region]) -> Region:
    character = regions[0].character
    map = regions[0].map

    positions = []
    sides = []
    area = 0
    perimeter = 0
    for region in regions:
        positions.extend(region.positions)
        area += region.area
        perimeter += region.perimeter

        for side in region.sides:

            merged_side = None
            for already_existing_side in sides:
                new_side = merge_sides(side, already_existing_side)
                if new_side:
                    merged_side = new_side
                    break

            if not merged_side:
                merged_side = side
            sides.append(merged_side)

    return Region(
        character=character,
        positions=positions,
        area=area,
        perimeter=perimeter,
        sides=sides,
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
