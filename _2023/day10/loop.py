from dataclasses import dataclass
from _2023.day10 import Tile, Position

#
#
# @dataclass
# class LoopTile(Tile):
#     distance_from_start: int
#
#     @classmethod
#     def from_tile(cls, tile: Tile, distance_from_start: int) -> "LoopTile":
#         return LoopTile(
#             position=tile.position,
#             type=tile.type,
#             distance_from_start=distance_from_start,
#         )
#
#
# class Loop(list):
#     def add_tile(self, tile: Tile, distance_from_start: int):
#         self.append(
#             LoopTile.from_tile(
#                 tile=tile, distance_from_start=distance_from_start
#             )
#         )
#
#     def get_position_index(self, position: Position) -> int:
#         for i, tile in enumerate(self):
#             if tile.position == position:
#                 return i
#
#         raise ValueError(f"{position} is not in list")
#
#     @property
#     def positions(self) -> list[Position]:
#         return [tile.position for tile in self]
#
#     @property
#     def distances(self) -> dict[Position, int]:
#         return {tile.position: tile.distance_from_start for tile in self}
#
#     def validate_distances(self):
#         new_distance = 0
#         for tile_index in range(len(self) - 1, -1, -1):
#             tile = self[tile_index]
#
#             if tile.distance_from_start <= new_distance:
#                 break
#             else:
#                 tile.distance_from_start = new_distance
#             new_distance += 1
