from dataclasses import dataclass
from enum import Enum
from typing import Optional
from copy import deepcopy

Position = tuple[int, int]


class Direction(Enum):
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    DOWN = (0, 1)
    UP = (0, -1)

    def compute_new_position(self, position: Position) -> Position:
        return position[0] + self.value[0], position[1] + self.value[1]


class TileType(Enum):
    EMPTY_SPACE = "."
    MIRROR_UP = "/"
    MIRROR_DOWN = "\\"
    SPLITTER_UP_DOWN = "|"
    SPLITTER_RIGHT_LEFT = "-"


MIRROR_UP_NEW_DIRECTION_MAPPING = {
    Direction.RIGHT: Direction.UP,
    Direction.LEFT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.UP: Direction.RIGHT,
}

MIRROR_DOWN_NEW_DIRECTION_MAPPING = {
    Direction.RIGHT: Direction.DOWN,
    Direction.LEFT: Direction.UP,
    Direction.UP: Direction.LEFT,
    Direction.DOWN: Direction.RIGHT,
}

MIRROR_MAPPING = {
    TileType.MIRROR_UP: MIRROR_UP_NEW_DIRECTION_MAPPING,
    TileType.MIRROR_DOWN: MIRROR_DOWN_NEW_DIRECTION_MAPPING,
}


SPLITTER_UP_DOWN_NEW_DIRECTIONS = [Direction.UP, Direction.DOWN]
SPLITTER_RIGHT_LEFT_NEW_DIRECTIONS = [Direction.RIGHT, Direction.LEFT]


SPLITTER_MAPPING = {
    TileType.SPLITTER_UP_DOWN: SPLITTER_UP_DOWN_NEW_DIRECTIONS,
    TileType.SPLITTER_RIGHT_LEFT: SPLITTER_RIGHT_LEFT_NEW_DIRECTIONS,
}


@dataclass
class Tile:
    type: TileType
    position: Position


@dataclass
class State:
    position: Position
    direction: Direction


class Lightbeam:
    def __init__(self, head: Position, direction: Direction):
        self.current_state = State(position=head, direction=direction)
        self.states = []

    @property
    def head(self) -> Position:
        return self.current_state.position

    @property
    def direction(self) -> Direction:
        return self.current_state.direction

    def check_already_visited_tile(self, tile) -> bool:
        for state in self.states:
            if state.position == tile.position:

                if tile.type in [
                    TileType.EMPTY_SPACE,
                    TileType.MIRROR_UP,
                    TileType.MIRROR_DOWN,
                ]:
                    return self.direction == state.direction

                elif tile.type in [
                    TileType.SPLITTER_UP_DOWN,
                    TileType.SPLITTER_RIGHT_LEFT,
                ]:
                    splitter_directions = SPLITTER_MAPPING[tile.type]
                    if state.direction in splitter_directions:
                        return self.direction == state.direction
                    else:
                        return state not in splitter_directions

    def _update_state(self, state: State):
        self.states.append(self.current_state)
        self.current_state = state

    def _continues_empty_space(self, tile: Tile):
        new_state = State(
            position=tile.position,
            direction=self.direction,
        )
        self._update_state(new_state)

    def continues(self, tile: Tile) -> Optional["Lightbeam"]:
        if self.check_already_visited_tile(tile):
            raise StopIteration(
                "The lightbeam already visited this tile with this state "
                "(or a similar)"
            )

        if tile.type == TileType.EMPTY_SPACE:
            self._continues_empty_space(tile)

        elif tile.type in [TileType.MIRROR_UP, TileType.MIRROR_DOWN]:
            new_direction_mapping = MIRROR_MAPPING[tile.type]
            new_direction = new_direction_mapping[self.direction]
            self._update_state(
                State(position=tile.position, direction=new_direction)
            )

        elif tile.type in [
            TileType.SPLITTER_UP_DOWN,
            TileType.SPLITTER_RIGHT_LEFT,
        ]:
            splitter_directions = SPLITTER_MAPPING[tile.type]
            if self.direction in splitter_directions:
                self._continues_empty_space(tile)
            else:
                other = deepcopy(self)

                self_new_direction = splitter_directions[0]
                other_new_direction = splitter_directions[1]

                for obj, new_direction in [
                    (self, self_new_direction),
                    (other, other_new_direction),
                ]:
                    obj._update_state(
                        State(position=tile.position, direction=obj.direction)
                    )
                return other
        return None


@dataclass
class Contraption:
    tiles: list[list[Tile]]

    @classmethod
    def from_data(cls, data: str) -> "Contraption":
        tiles = []
        for y, line in enumerate(data.splitlines()):
            tiles_line = []
            for x, character in enumerate(line):
                tiles_line.append(
                    Tile(type=TileType(character), position=(x, y))
                )
            tiles.append(tiles_line)
        return Contraption(tiles=tiles)

    def get_tile_at_position(self, position: Position) -> Tile:
        x, y = position
        return self.tiles[y][x]
