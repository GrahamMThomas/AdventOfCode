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

valid_numerics = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def replace_word_with_digit(line: str):
    new_line = ""
    offset = 0
    for i in range(len(line)):
        replaced = False

        for j in range(len(valid_numerics)):
            if line[i + offset :].startswith(valid_numerics[j]):
                replaced = True
                offset += len(valid_numerics[j]) - 2
                new_line += str(j + 1)
                break

        if i + offset >= len(line):
            break
        if not replaced:
            new_line += line[i + offset]

    return new_line


def get_digit(line: str):
    new_lien = replace_word_with_digit(line)
    all_digits = [x for x in new_lien if x.isdigit()]
    return all_digits[0] + all_digits[-1]


print(sum([int(get_digit(line)) for line in input]))
