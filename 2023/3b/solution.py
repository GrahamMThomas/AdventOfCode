# Adjust the path to the root of the project for library access
import sys

sys.path.append(r"../../")

import re
from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import defaultdict

from aoc.input_file import read_input
from aoc.fluff import print_intro

input = read_input()
print_intro(__file__, input)

## Solution ##


class EngineNumber:
    def __init__(self, number: int):
        self.number = number
        self.adjacent_squares = []
        self.valid = False

    def length(self):
        return len(str(self.number))


class Gear:
    def __init__(self):
        self.engines = []


class Grid:
    def __init__(self):
        self.grid = []

    def add(self, row):
        self.grid.append(row)

    def is_space(self, coords) -> bool:
        return (
            coords[0] >= 0
            and coords[1] >= 0
            and coords[0] < len(self.grid)
            and coords[1] < len(self.grid[0])
        )

    def get(self, coords):
        if not self.is_space(coords):
            return None
        return self.grid[coords[1]][coords[0]]


grid = Grid()
line_number = 0
gears = []

all_numbers = []
for line in input:
    grid.add(list(line))
    splitted_line = re.findall(r"(\d+)", line)
    numbers = [EngineNumber(int(x)) for x in splitted_line if x.isdecimal()]

    latest_index = 0
    for engine_number in numbers:
        i = line.index(str(engine_number.number), latest_index)
        latest_index = i + engine_number.length()
        engine_number.adjacent_squares.append((i - 1, line_number))
        engine_number.adjacent_squares.append((latest_index, line_number))
        for x in range(i - 1, latest_index + 1):
            engine_number.adjacent_squares.append((x, line_number - 1))
            engine_number.adjacent_squares.append((x, line_number + 1))

    all_numbers += numbers

    line_number += 1

gears = defaultdict(Gear)
for number in all_numbers:
    for adjacent_square in number.adjacent_squares:
        entry = grid.get(adjacent_square)
        if entry == "*":
            print("blah")
            gears[adjacent_square].engines.append(number)

print(gears)
print(
    sum(
        [
            v.engines[0].number * v.engines[1].number
            for k, v in gears.items()
            if len(v.engines) == 2
        ]
    )
)
