import pytest
from _2024.day5 import OrderingRule, OrderingRules, PrintQueue, Update
from _2024.day5.part2 import compute_solution

ORDERING_RULES = OrderingRules(
    [
        OrderingRule(47, 53),
        OrderingRule(97, 13),
        OrderingRule(97, 61),
        OrderingRule(97, 47),
        OrderingRule(75, 29),
        OrderingRule(61, 13),
        OrderingRule(75, 53),
        OrderingRule(29, 13),
        OrderingRule(97, 29),
        OrderingRule(53, 29),
        OrderingRule(61, 53),
        OrderingRule(97, 53),
        OrderingRule(61, 29),
        OrderingRule(47, 13),
        OrderingRule(75, 47),
        OrderingRule(97, 75),
        OrderingRule(47, 61),
        OrderingRule(75, 61),
        OrderingRule(47, 29),
        OrderingRule(75, 13),
        OrderingRule(53, 13),
    ]
)


@pytest.mark.parametrize(
    "list_of_pages, sorted_list_of_pages",
    [
        ([75, 97, 47, 61, 53], [97, 75, 47, 61, 53]),
        ([61, 13, 29], [61, 29, 13]),
        ([97, 13, 75, 29, 47], [97, 75, 47, 29, 13]),
    ],
)
def test_sorting_can_be_applied_on_updates(
    list_of_pages, sorted_list_of_pages
):
    update = Update(list_of_pages)
    new_update = update.sorted(ORDERING_RULES)

    assert new_update == sorted_list_of_pages


def test_solution_can_be_computed():
    print_queue = PrintQueue(
        ordering_rules=ORDERING_RULES,
        updates=[
            Update([75, 47, 61, 53, 29]),
            Update([97, 61, 53, 29, 13]),
            Update([75, 29, 13]),
            Update([75, 97, 47, 61, 53]),
            Update([61, 13, 29]),
            Update([97, 13, 75, 29, 47]),
        ],
    )
    assert compute_solution(print_queue) == 123
