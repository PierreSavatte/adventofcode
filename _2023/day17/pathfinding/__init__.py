from _2023.day17 import Node, Map


def get_neighbors(map: Map, current: Node) -> list[Node]:
    neighbors = []
    for node in map.get_immediate_neighbors(current):
        # Skipping according to puzzle constraint:
        # it can move at most three blocks in a single direction
        if node.direction_streak >= 4:
            continue
        neighbors.append(node)
    return neighbors
