from _2025.day2 import Solver


class Part1Solver(Solver):
    @staticmethod
    def is_invalid_id(id: int) -> bool:
        id_str = str(id)
        i = len(id_str) // 2
        return id_str[:i] == id_str[i:]


if __name__ == "__main__":
    solver = Part1Solver()
    print(solver.solve())
