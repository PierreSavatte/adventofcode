class Ingredients:
    def __init__(self, input: str):
        self.ranges = []
        self.availables = []

        in_range_section = True
        for line in input.strip().splitlines():
            line = line.strip()
            if line == "":
                in_range_section = False
                continue

            if in_range_section:
                a, b = line.split("-")
                self.ranges.append(range(int(a), int(b) + 1))

            else:
                self.availables.append(int(line))

    def is_fresh(self, ingredient: int) -> bool:
        return any(ingredient in range for range in self.ranges)
