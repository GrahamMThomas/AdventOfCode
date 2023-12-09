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


class History:
    def __init__(self, line):
        self.values = re.findall(r"\-?\d+", line)
        self.values = [int(x) for x in self.values]

    def next_value(self):
        derivitives = [self.values.copy()]
        i = 0
        while True:
            new_derivitives = [
                derivitives[i][x + 1] - derivitives[i][x]
                for x in range(len(derivitives[i]) - 1)
            ]
            derivitives.append(new_derivitives)
            i += 1
            if all([x == new_derivitives[0] for x in new_derivitives]):
                break

        derivitives.reverse()
        carry_over = derivitives[0][0]
        for i in range(len(derivitives) - 1):
            carry_over = derivitives[i + 1][0] - carry_over

        return carry_over


histories = []
for line in input:
    histories.append(History(line))

values = []
for history in histories:
    values.append(history.next_value())

print(sum(values))
