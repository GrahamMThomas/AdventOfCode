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


class Puzzle:
    def __init__(self, puzzle, requirements):
        self.puzzle = puzzle
        self.requirements = [int(x) for x in requirements]

    def get_solves(self):
        puzzles = []
        question_count = len([x for x in self.puzzle if x == "?"])
        possible_amount = 2**question_count

        for i in range(possible_amount):
            proposed_puzzle = self.puzzle
            configuration = str(bin(i)[2:].zfill(question_count))
            for j in configuration:
                if j == "0":
                    # repalce the first found character
                    proposed_puzzle = proposed_puzzle.replace("?", ".", 1)
                else:
                    proposed_puzzle = proposed_puzzle.replace("?", "#", 1)

            if self.puzzle_works(proposed_puzzle):
                puzzles.append(proposed_puzzle)

        return len(puzzles)

    def puzzle_works(self, proposed_puzzle):
        groups = re.findall(r"#+", proposed_puzzle)
        groups = [len(x) for x in groups]
        return groups == self.requirements


puzzles = []
for line in input:
    tmp = line.split(" ")
    puzzle = tmp[0]
    requirements = re.findall(r"(\d+)", tmp[1])
    puzzles.append(Puzzle(puzzle, requirements))

total = 0
for puzzle in puzzles:
    total += puzzle.get_solves()

print(total)

## Perf ##
print(f"Time taken: {((datetime.now() - start).total_seconds() * 1000):.2f}ms")
