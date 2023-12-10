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
from datetime import datetime

input = read_input()
print_intro(__file__, input)

## Solution ##
start = datetime.now()


class Node:
    def __init__(self, char, loc):
        self.char = char
        self.loc = loc
        self.visited = False
        self.steps = 0
        self.outsider = False
        self.insider = False
        self.outsiders_locs = []  # Right

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
                self.outsiders_locs.append((self.loc[0] + 1, self.loc[1]))
                return (self.loc[0], self.loc[1] - 1)
            elif self.loc[1] - 1 == from_loc[1]:
                self.outsiders_locs.append((self.loc[0] - 1, self.loc[1]))
                return (self.loc[0], self.loc[1] + 1)
            else:
                self.print_fail(from_loc)
        elif self.char == "-":
            if self.loc[0] + 1 == from_loc[0]:
                self.outsiders_locs.append((self.loc[0], self.loc[1] - 1))
                return (self.loc[0] - 1, self.loc[1])
            elif self.loc[0] - 1 == from_loc[0]:
                self.outsiders_locs.append((self.loc[0], self.loc[1] + 1))
                return (self.loc[0] + 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == "L":
            if self.loc[0] + 1 == from_loc[0]:
                self.outsiders_locs.append((self.loc[0] + 1, self.loc[1] - 1))
                return (self.loc[0], self.loc[1] - 1)
            elif self.loc[1] - 1 == from_loc[1]:
                self.outsiders_locs.append((self.loc[0] - 1, self.loc[1]))
                self.outsiders_locs.append((self.loc[0] - 1, self.loc[1] + 1))
                self.outsiders_locs.append((self.loc[0] + 1, self.loc[1]))

                return (self.loc[0] + 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == "J":
            if self.loc[0] - 1 == from_loc[0]:
                self.outsiders_locs.append((self.loc[0], self.loc[1] + 1))
                self.outsiders_locs.append((self.loc[0] + 1, self.loc[1] + 1))
                self.outsiders_locs.append((self.loc[0] + 1, self.loc[1]))

                return (self.loc[0], self.loc[1] - 1)
            elif self.loc[1] - 1 == from_loc[1]:
                self.outsiders_locs.append((self.loc[0] - 1, self.loc[1] - 1))
                return (self.loc[0] - 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == "7":
            if self.loc[0] - 1 == from_loc[0]:
                self.outsiders_locs.append((self.loc[0] - 1, self.loc[1] + 1))
                return (self.loc[0], self.loc[1] + 1)
            elif self.loc[1] + 1 == from_loc[1]:
                self.outsiders_locs.append((self.loc[0] + 1, self.loc[1]))
                self.outsiders_locs.append((self.loc[0] + 1, self.loc[1] - 1))
                self.outsiders_locs.append((self.loc[0], self.loc[1] - 1))

                return (self.loc[0] - 1, self.loc[1])
            else:
                self.print_fail(from_loc)
        elif self.char == "F":
            if self.loc[0] + 1 == from_loc[0]:
                self.outsiders_locs.append((self.loc[0], self.loc[1] - 1))
                self.outsiders_locs.append((self.loc[0] - 1, self.loc[1] - 1))
                self.outsiders_locs.append((self.loc[0] - 1, self.loc[1]))

                return (self.loc[0], self.loc[1] + 1)
            elif self.loc[1] + 1 == from_loc[1]:
                self.outsiders_locs.append((self.loc[0] + 1, self.loc[1] + 1))

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

    def get_neighbors(self):
        neighbors = []
        for i in range(3):
            for j in range(3):
                x = self.loc[0] - 1 + j
                y = self.loc[1] - 1 + i
                if (x, y) == self.loc:
                    continue

                if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
                    continue
                neighbors.append((x, y))

        return neighbors


starting_pos = (0, 0)

map = []
for i, line in enumerate(input):
    row = []
    for j, char in enumerate(line):
        row.append(Node(char, (j, i)))
        if char == "S":
            starting_pos = (j, i)
    map.append(row)


loc_vector = [starting_pos, (starting_pos[0], starting_pos[1] - 1)]


steps = 0

from_loc = loc_vector[0]
to_loc = loc_vector[1]
while True:
    square = map[to_loc[1]][to_loc[0]]
    if square.char == "S":
        break

    steps += 1

    original_loc = to_loc
    to_loc = square.move(from_loc)
    if to_loc == None:
        break
    from_loc = original_loc

## Calculate all the outside boundary nodes

locs = [(0, 0)]
while len(locs) > 0:
    loc = locs.pop(0)
    square = map[loc[1]][loc[0]]
    square.outsider = True

    neighbors = [
        loc
        for loc in square.get_neighbors()
        if (not map[loc[1]][loc[0]].visited and not map[loc[1]][loc[0]].outsider)
    ]
    for x in neighbors:
        map[x[1]][x[0]].outsider = True

    locs += neighbors

# Set everything on the inside of the outside boundary and not on the path to be an insider

for y in range(len(map)):
    for x in range(len(map[0])):
        square = map[y][x]
        if not square.outsider and not square.visited:
            square.insider = True

# Check all current insiders to see if they are on the correct side of the path

for i in range(3):  # Do this 3 times to make sure any nested insiders are caught
    for y in range(len(map)):
        for x in range(len(map[0])):
            square = map[y][x]
            if not square.insider:
                continue

            neighbor_locs = square.get_neighbors()
            for loc in neighbor_locs:
                neighbor = map[loc[1]][loc[0]]

                if ((x, y) in neighbor.outsiders_locs) or neighbor.outsider:
                    square.outsider = True
                    square.insider = False
                    break

# Count all the insiders

count = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x].insider:
            count += 1

print(f"Answer: {count}")

# Check milliseconds
print(f"Time taken: {(datetime.now() - start).total_seconds() * 1000:.2f}ms")
