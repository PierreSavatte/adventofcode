from _2025.day2 import Solver


class Part2Solver(Solver):
    @staticmethod
    def is_invalid_id(id: int) -> bool:
        id_str = str(id)
        for i in range(1, len(id_str) // 2 + 1):
            duplicated_part = id_str[:i]
            nb_times_duplicated = len(id_str) // i
            if duplicated_part * nb_times_duplicated == id_str:
                return True
        return False


if __name__ == "__main__":
    solver = Part2Solver()
    print(solver.solve())
