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
        self.puzzle = []
        for i in range(5):
            self.puzzle.append(puzzle)
        self.puzzle = "?".join(self.puzzle)
        self.requirements = [int(x) for x in requirements] * 5

    def get_solves(self):
        puzzles = [self.puzzle[0]]

        valid_puzzles = 0
        while len(puzzles) != 0:
            puzzle = puzzles.pop()
            print(puzzle)
            if "?" in puzzle[-1]:
                option1 = puzzle.replace("?", ".", 1)
                option2 = puzzle.replace("?", "#", 1)
                if self.still_valid(option1):
                    puzzles.append(puzzle.replace("?", ".", 1))
                if self.still_valid(option2):
                    puzzles.append(puzzle.replace("?", "#", 1))
            else:
                if self.puzzle_works(puzzle):
                    valid_puzzles += 1
                elif len(puzzle) < len(self.puzzle):
                    puzzle += self.puzzle[len(puzzle)]
                    puzzles.append(puzzle)

        return valid_puzzles

    def still_valid(self, proposed_segment):
        groups = self.get_puzzle_groups(proposed_segment)
        for i in range(len(groups)):
            if i == len(groups) - 1:
                if groups[i] <= self.requirements[i]:
                    return True
            if groups[i] != self.requirements[i]:
                return False

    def get_puzzle_groups(self, puzzle):
        groups = re.findall(r"#+", puzzle)
        groups = [len(x) for x in groups]
        return groups

    def puzzle_works(self, proposed_puzzle):
        groups = self.get_puzzle_groups(proposed_puzzle)
        return groups == self.requirements


puzzles = []
for line in input:
    tmp = line.split(" ")
    puzzle = tmp[0]
    requirements = re.findall(r"(\d+)", tmp[1])
    puzzles.append(Puzzle(puzzle, requirements))

total = 0
for puzzle in puzzles:
    print(f"{puzzle.puzzle} {puzzle.requirements}")
    total += puzzle.get_solves()

print(total)

## Perf ##
print(f"Time taken: {((datetime.now() - start).total_seconds() * 1000):.2f}ms")
