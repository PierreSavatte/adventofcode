import pytest
from _2024.day5 import (
    OrderingRule,
    OrderingRules,
    PrintQueue,
    Update,
    parse_input,
)
from _2024.day5.part1 import compute_solution

TEST_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

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


def test_input_can_be_parsed():
    assert parse_input(TEST_INPUT) == PrintQueue(
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


@pytest.mark.parametrize(
    "a, b",
    [
        (75, 47),
        (75, 61),
        (75, 53),
        (75, 29),
        (47, 61),
        (47, 53),
        (47, 29),
        (61, 53),
        (61, 29),
        (53, 29),
    ],
)
def test_ordering_of_pages_can_be_validated(a, b):
    assert ORDERING_RULES.is_greater_than(a, b) is True


@pytest.mark.parametrize("a, b", [(75, 97), (13, 29)])
def test_ordering_of_pages_can_be_rejected(a, b):
    assert ORDERING_RULES.is_greater_than(a, b) is False


@pytest.mark.parametrize(
    "list_of_pages, expected_validation_status",
    [
        ([75, 47, 61, 53, 29], True),
        ([97, 61, 53, 29, 13], True),
        ([75, 29, 13], True),
        ([75, 97, 47, 61, 53], False),
        ([61, 13, 29], False),
        ([97, 13, 75, 29, 47], False),
    ],
)
def test_update_can_be_asserted_if_in_the_right_order(
    list_of_pages, expected_validation_status
):
    update = Update(list_of_pages)

    assert update.validate_order(ORDERING_RULES) is expected_validation_status


@pytest.mark.parametrize(
    "list_of_pages, middle_page",
    [
        ([75, 47, 61, 53, 29], 61),
        ([97, 61, 53, 29, 13], 53),
        ([75, 29, 13], 29),
    ],
)
def test_middle_page_can_be_evaluated(list_of_pages, middle_page):
    update = Update(list_of_pages)

    assert update.get_middle_page() == middle_page


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
    assert compute_solution(print_queue) == 143
