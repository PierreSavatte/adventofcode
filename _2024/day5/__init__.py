class OrderingRule:
    def __init__(self, before: int, after: int):
        self.before = before
        self.after = after

    def __eq__(self, other):
        return (self.before == other.before) and (self.after == other.after)


class OrderingRules(list[OrderingRule]):
    def is_greater_than(self, a: int, b: int) -> bool:
        for ordering_rule in self:
            if ordering_rule.before == a and ordering_rule.after == b:
                return True
            if ordering_rule.after == a and ordering_rule.before == b:
                return False
        return False


class Update(list[int]):
    def validate_order(self, ordering_rules: OrderingRules) -> bool:
        for i, page in enumerate(self):
            other_pages = self[i + 1 :]
            for other_page in other_pages:
                if not ordering_rules.is_greater_than(page, other_page):
                    return False
        return True

    def get_middle_page(self) -> int:
        return self[len(self) // 2]


class PrintQueue:
    def __init__(
        self,
        ordering_rules: OrderingRules,
        updates: list[Update],
    ):
        self.ordering_rules = ordering_rules
        self.updates = updates

    def __eq__(self, other):
        return (
            self.ordering_rules == other.ordering_rules
            and self.updates == other.updates
        )

    def __repr__(self):
        return (
            "<PrintQueue "
            f"ordering_rules={self.ordering_rules} "
            f"updates={self.updates}>"
        )


def parse_input(data: str) -> PrintQueue:
    data = data.strip("\n")

    ordering_rules_str, updates_str = data.split("\n\n")

    ordering_rules = []
    for ordering_rule_str in ordering_rules_str.split("\n"):
        a, b = ordering_rule_str.split("|")
        ordering_rules.append(OrderingRule(int(a), int(b)))

    updates = []
    for update_str in updates_str.split("\n"):
        updates.append(Update([int(value) for value in update_str.split(",")]))

    return PrintQueue(
        ordering_rules=OrderingRules(ordering_rules),
        updates=updates,
    )
