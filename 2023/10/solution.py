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


class Node:
    def __init__(self, char, loc):
        self.char = char
        self.loc = loc
        self.visited = False
        self.steps = 0

    def move(self, from_loc):
        if self.steps == 0:
            self.steps = map[from_loc[1]][from_loc[0]].steps + 1
        else:
            self.steps = min(self.steps, map[from_loc[1]][from_loc[0]].steps + 1)

        if self.char == "S":
            self.steps = 0
        self.visited = True

        if self.char == "|":
            if self.loc[1] + 1 == from_loc[1]:
                return (self.loc[0], self.loc[1] - 1)
            elif self.loc[1] - 1 == from_loc[1]:
                return (self.loc[0], self.loc[1] + 1)
            else:
                self.print_fail(from_loc)
        elif self.char == "-":
            if self.loc[0] + 1 == from_loc[0]:
                return (self.loc[0] - 1, self.loc[1])
            elif self.loc[0] - 1 == from_loc[0]:
                return (self.loc[0] + 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == "L":
            if self.loc[0] == from_loc[0] - 1:
                return (self.loc[0], self.loc[1] - 1)
            elif self.loc[1] - 1 == from_loc[1]:
                return (self.loc[0] + 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == "J":
            if self.loc[0] - 1 == from_loc[0]:
                return (self.loc[0], self.loc[1] - 1)
            elif self.loc[1] - 1 == from_loc[1]:
                return (self.loc[0] - 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == "7":
            if self.loc[0] - 1 == from_loc[0]:
                return (self.loc[0], self.loc[1] + 1)
            elif self.loc[1] + 1 == from_loc[1]:
                return (self.loc[0] - 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == "F":
            if self.loc[0] + 1 == from_loc[0]:
                return (self.loc[0], self.loc[1] + 1)
            elif self.loc[1] + 1 == from_loc[1]:
                return (self.loc[0] + 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == ".":
            self.print_fail(from_loc)
        elif self.char == "S":
            self.visited = True
            return from_loc

    def print_fail(self, from_loc):
        print(f"FAIL: {self.char} at {self.loc}:")
        for i in range(3):
            for j in range(3):
                x = self.loc[0] - 1 + j
                y = self.loc[1] - 1 + i
                if (x, y) == from_loc:
                    print("X", end="")
                else:
                    print(map[y][x].char, end="")
            print()


starting_pos = (0, 0)

map = []
for i, line in enumerate(input):
    row = []
    for j, char in enumerate(line):
        row.append(Node(char, (j, i)))
        if char == "S":
            starting_pos = (j, i)
    map.append(row)


locs = [
    [starting_pos, (starting_pos[0], starting_pos[1] - 1)],
    [starting_pos, (starting_pos[0] + 1, starting_pos[1])],
    [starting_pos, (starting_pos[0], starting_pos[1] + 1)],
    [starting_pos, (starting_pos[0] - 1, starting_pos[1])],
]
# map[starting_pos[1]][starting_pos[0]]

for loc_vector in locs:
    print()
    steps = 0

    from_loc = loc_vector[0]
    to_loc = loc_vector[1]
    while True:
        square = map[to_loc[1]][to_loc[0]]
        if square.char == "S" and square.visited:
            break

        steps += 1
        # print(steps)
        # square.print_fail(loc)

        # if square.visited:
        #     print("FOUND")
        #     exit(0)

        original_loc = to_loc
        to_loc = square.move(from_loc)
        if to_loc == None:
            break
        from_loc = original_loc

    max_value = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            max_value = max(max_value, map[y][x].steps)
            map[y][x].visited = False
            map[y][x].steps = 0
    print(max_value)
