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


class Card:
    def __init__(self, i, win_nums, your_nums):
        self.i = i
        self.win_nums = win_nums
        self.your_nums = your_nums

    def matching_nums(self) -> int:
        return len(self.win_nums.intersection(self.your_nums))


deck = []
totals = 0

for i in range(len(input)):
    numbers = input[i].split(": ")[1]
    winning_numbers = numbers.split(" | ")[0]
    your_numbers = numbers.split(" | ")[1]
    win_nums = set(re.findall(r"\d+", winning_numbers))
    your_nums = set(re.findall(r"\d+", your_numbers))
    deck.append(Card(i, win_nums, your_nums))

stack = deck.copy()
stack.reverse()
# print(stack)
total_cards = len(deck)

while len(stack) > 0:
    card = stack.pop()
    matching_numbers = card.matching_nums()
    # print(f"Card {card.i} has {matching_numbers} matching numbers")
    while matching_numbers > 0:
        if card.i + matching_numbers < len(deck):
            card_to_add = deck[card.i + matching_numbers]
            # print(f"Adding {card_to_add.i}")
            stack.append(card_to_add)
        total_cards += 1
        matching_numbers -= 1


print(total_cards)
