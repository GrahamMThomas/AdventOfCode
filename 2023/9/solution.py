# Adjust the path to the root of the project
import sys

sys.path.append(r"../../")

import re
from dataclasses import dataclass
from enum import Enum
from typing import List

from aoc.input_file import read_input

input = read_input()


class History:
    def __init__(self, line):
        self.values = re.findall(r"\-?\d+", line)
        self.values = [int(x) for x in self.values]

    def next_value(self):
        derivitives = [self.values.copy()]
        i = 0
        print(derivitives[0])
        while True:
            new_derivitives = [
                derivitives[i][x + 1] - derivitives[i][x]
                for x in range(len(derivitives[i]) - 1)
            ]
            print(new_derivitives)
            derivitives.append(new_derivitives)
            i += 1
            if all([x == new_derivitives[0] for x in new_derivitives]):
                break

        derivitives.reverse()
        carry_over = derivitives[0][-1]
        for i in range(len(derivitives) - 1):
            print(
                f"carry_over: {carry_over}, derivitives[i + 1][-1]: {derivitives[i + 1][-1]}"
            )
            carry_over = derivitives[i + 1][-1] + carry_over

        return carry_over


histories = []
for line in input:
    histories.append(History(line))

print(histories[1].next_value())

# values = []
# for history in histories:
#     values.append(history.next_value())
#
# print(sum(values))
