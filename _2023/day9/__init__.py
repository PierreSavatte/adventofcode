class Sequence(list):
    sequence: list[int]

    def compute_differences(self) -> dict[int, list[int]]:
        differences = {0: self}
        current_degree = 1
        while not all(d == 0 for d in differences[current_degree - 1]):
            list_ = differences[current_degree - 1]
            diff = []
            for i in range(0, len(list_) - 1):
                j = i + 1
                a = list_[i]
                b = list_[j]
                diff.append(b - a)
            differences[current_degree] = diff
            current_degree += 1
        return differences

    def get_next_value(self) -> int:
        differences = self.compute_differences()
        max_key = max(differences.keys())

        differences[max_key].append(0)
        for key in range(max_key - 1, -1, -1):
            previous_value = differences[key][-1]
            increase = differences[key + 1][-1]
            new_value = previous_value + increase
            differences[key].append(new_value)

        return differences[0][-1]

    def get_previous_value(self) -> int:
        differences = self.compute_differences()
        max_key = max(differences.keys())

        differences[max_key].insert(0, 0)
        for key in range(max_key - 1, -1, -1):
            first_value = differences[key][0]
            increase = differences[key + 1][0]
            new_value = first_value - increase
            differences[key].insert(0, new_value)

        return differences[0][0]
