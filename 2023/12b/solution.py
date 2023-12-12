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
        all_segments = re.findall(r"([\?\#]+)", self.puzzle)
        segments = set(all_segments)

        segment_mag = defaultdict(lambda: [])
        for segment in list(segments):
            solves = self.get_segment_solves(segment, single_seg=len(segments) == 1)
            segment_mag[segment] = solves

        tree = [()]
        for segment in all_segments:
            new_tree = []
            for tree_attempt in tree:
                for solve in segment_mag[segment]:
                    new_solve = tree_attempt + solve
                    if self.validate_partial_puzzle(new_solve):
                        new_tree.append(new_solve)

            tree = new_tree

        return len(tree)

    def get_segment_solves(self, segment, single_seg=False):
        puzzles = [segment[0]]

        puzzle_groups = set()
        i = 0
        while len(puzzles) != 0:
            i += 1
            # print(len(puzzles[0]))
            puzzle = puzzles.pop()
            if i % 1000000 == 0:
                print(puzzle)
            if "?" in puzzle[-1]:
                option1 = puzzle.replace("?", ".", 1)
                option2 = puzzle.replace("?", "#", 1)
                if self.still_valid(option1, single_seg):
                    puzzles.append(puzzle.replace("?", ".", 1))
                if self.still_valid(option2, single_seg):
                    puzzles.append(puzzle.replace("?", "#", 1))
            else:
                if len(puzzle) < len(segment):
                    puzzle += segment[len(puzzle)]
                    puzzles.append(puzzle)
                elif self.contains_valid_numerics(puzzle):
                    puzzle_groups.add(tuple(self.get_puzzle_groups(puzzle)))

        return puzzle_groups

    def still_valid(self, proposed_segment, single_seg=False):
        groups = self.get_puzzle_groups(proposed_segment)
        if len(groups) == 0:
            return True

        if groups[-1] > max(self.requirements):
            return False

        if len(groups) == 1:
            return True

        if single_seg and groups[:-1] != self.requirements[: len(groups) - 1]:
            return False

        subgroup = groups[:-1]
        subgroup = ",".join([str(x) for x in subgroup])
        req_str = ",".join([str(x) for x in self.requirements])
        if subgroup in req_str:
            return True

        return False

    def validate_partial_puzzle(self, groups):
        if len(groups) > len(self.requirements):
            return False

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

    def contains_valid_numerics(self, proposed_puzzle):
        groups = self.get_puzzle_groups(proposed_puzzle)
        return len(set(groups).difference(set(self.requirements))) == 0


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
