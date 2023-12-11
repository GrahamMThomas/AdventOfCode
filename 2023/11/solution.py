# Adjust the path to the root of the project for library access
import sys

sys.path.append(r"../../")

import re
from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import defaultdict
from datetime import datetime
from aoc.input_file import read_input
from aoc.fluff import print_intro

input = read_input()
print_intro(__file__, input)
start = datetime.now()


## Solution ##
class Galaxy:
    def __init__(self, number, loc):
        self.number = number
        self.loc = loc


map = []
for i, line in enumerate(input):
    row = []
    for j, char in enumerate(line):
        row.append(char)

    if len([x for x in row if x == "#"]) == 0:
        print("Emtpy row")
        map.append(row.copy())

    map.append(row)

offset = 0

if all([len(row) == len(map[0]) for row in map]):
    print("All rows are the same length")

for i in range(len(map[0])):
    i_o = i + offset
    empty = True
    for row in map:
        if row[i_o] == "#":
            empty = False
            break

    if empty:
        print("Empty column")
        for j in range(len(map)):
            map[j].insert(i_o, ".")
        offset += 1


if all([len(row) == len(map[0]) for row in map]):
    print("All rows are the same length")

galaxies = []

for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == "#":
            galaxies.append(Galaxy(len(galaxies), (j, i)))
print(len(galaxies))


pairs = set()
for i in range(len(galaxies)):
    for j in range(len(galaxies)):
        if i == j:
            continue

        if i > j:
            pairs.add((j, i))
        else:
            pairs.add((i, j))

distances = []
for pair in pairs:
    g1 = galaxies[pair[0]]
    g2 = galaxies[pair[1]]

    distances.append(abs(g1.loc[0] - g2.loc[0]) + abs(g1.loc[1] - g2.loc[1]))

print(sum(distances))
## Perf ##
print(f"Time taken: {((datetime.now() - start).total_seconds() * 1000):.2f}ms")
