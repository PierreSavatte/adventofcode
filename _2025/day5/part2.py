from _2025.day5 import Ingredients
from _2025.load_input import load_input


def compute_simplified_ranges(ranges: list[range]) -> list[range]:
    has_merged_ranges = True
    while has_merged_ranges:
        has_merged_ranges = False

        i = 0
        while i < len(ranges):
            r_1 = ranges[i]

            j = i + 1
            while j < len(ranges):
                r_2 = ranges[j]

                if (r_1.start in r_2 or r_1.stop - 1 in r_2) or (
                    r_2.start in r_1 or r_2.stop - 1 in r_1
                ):
                    new_range = range(
                        min(r_2.start, r_1.start), max(r_2.stop, r_1.stop)
                    )

                    ranges.pop(j)
                    ranges.pop(i)
                    ranges.append(new_range)
                    has_merged_ranges = True
                    break

                j += 1

            if has_merged_ranges:
                break

            i += 1

    return ranges


def compute_solution(ingredients: Ingredients) -> int:
    simplified_ranges = compute_simplified_ranges(ingredients.ranges)
    return sum(len(range) for range in simplified_ranges)


def main():
    ingredients = Ingredients(load_input(5))
    print(compute_solution(ingredients))


if __name__ == "__main__":
    main()
