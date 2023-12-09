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

totals = 0
for card in input:
    numbers = card.split(": ")[1]
    winning_numbers = numbers.split(" | ")[0]
    your_numbers = numbers.split(" | ")[1]
    win_nums = set(re.findall(r"\d+", winning_numbers))
    your_nums = set(re.findall(r"\d+", your_numbers))
    matching_numbers = len(win_nums.intersection(your_nums))
    if matching_numbers > 0:
        totals += 2 ** (matching_numbers - 1)

print(totals)
