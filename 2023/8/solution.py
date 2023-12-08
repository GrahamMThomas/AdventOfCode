# Adjust the path to the root of the project
import sys

sys.path.append(r"../../")

import re
from dataclasses import dataclass
from collections import defaultdict
from enum import Enum
from typing import List

from aoc.input_file import read_input

input = read_input()

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

loc = "AAA"

i = 0
while True:
    if instructions[i % len(instructions)] == "L":
        loc = graph[loc][0]
    else:
        loc = graph[loc][1]

    i += 1
    if loc == "ZZZ":
        break


print(i)
