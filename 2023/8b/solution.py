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


instructions = input[0]

graph = defaultdict(list)

for line in input[1:]:
    # CTK = (JLT, HRF)
    match = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", line)
    # print(match)
    if match is None:
        continue

    key = match.group(1)
    left = match.group(2)
    right = match.group(3)

    # print(f"{key} -> {left}, {right}")

    graph[key].append(left)
    graph[key].append(right)

nodes = [node for node in graph.keys() if node[2] == "A"]

for j in range(len(nodes)):
    i = 0
    indices = []
    while True:
        if instructions[i % len(instructions)] == "L":
            nodes[j] = graph[nodes[j]][0]
        else:
            nodes[j] = graph[nodes[j]][1]

        i += 1
        if nodes[j][2] == "Z":
            indices.append(i)

        if len(indices) == 10:
            print(indices)
            break

# Plug output into https://www.calculatorsoup.com/calculators/math/lcm.php
