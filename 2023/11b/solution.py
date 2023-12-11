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


bad_rows = []

map = []
for i, line in enumerate(input):
    row = []
    for j, char in enumerate(line):
        row.append(char)

    if len([x for x in row if x == "#"]) == 0:
        bad_rows.append(i)

    map.append(row)


bad_cols = []

for i in range(len(map[0])):
    empty = True
    for row in map:
        if row[i] == "#":
            empty = False
            break

    if empty:
        bad_cols.append(i)

galaxies = []

for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == "#":
            galaxies.append(Galaxy(len(galaxies), (i, j)))

print(f"Galaxy Count: {len(galaxies)}")


pairs = set()
for i in range(len(galaxies)):
    for j in range(len(galaxies)):
        if i == j:
            continue

        if i > j:
            pairs.add((j, i))
        else:
            pairs.add((i, j))

print(f"Pair Count: {len(pairs)}")

factor = 999999
distances = []
for pair in pairs:
    g1 = galaxies[pair[0]]
    g2 = galaxies[pair[1]]

    x_gaps = [
        x
        for x in bad_cols
        if (g1.loc[1] < x < g2.loc[1]) or (g2.loc[1] < x < g1.loc[1])
    ]
    y_gaps = [
        y
        for y in bad_rows
        if (g1.loc[0] < y < g2.loc[0]) or (g2.loc[0] < y < g1.loc[0])
    ]
    distances.append(
        abs(g1.loc[0] - g2.loc[0])
        + abs(g1.loc[1] - g2.loc[1])
        + len(x_gaps) * factor
        + len(y_gaps) * factor
    )

print(sum(distances))
## Perf ##
print(f"Time taken: {((datetime.now() - start).total_seconds() * 1000):.2f}ms")
