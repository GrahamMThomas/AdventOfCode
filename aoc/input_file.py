from typing import List


def read_input(filename: str = "input.txt") -> List[str]:
    with open(filename, "r") as f:
        input = f.read().splitlines()
        return input
