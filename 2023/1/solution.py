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


def get_digit(line: str):
    all_digits = [x for x in line if x.isdigit()]
    return all_digits[0] + all_digits[-1]


print(sum([int(get_digit(line)) for line in input]))
