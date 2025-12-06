from _2025.day5 import Ingredients
from _2025.load_input import load_input


def compute_solution(ingredients: Ingredients) -> int:
    return sum(
        ingredients.is_fresh(ingredient)
        for ingredient in ingredients.availables
    )


def main():
    ingredients = Ingredients(load_input(5))
    print(compute_solution(ingredients))


if __name__ == "__main__":
    main()
