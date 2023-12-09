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


class Rank(Enum):
    FiveOfKind = 1
    FourOfKind = 2
    FullHouse = 3
    ThreeOfKind = 4
    TwoPair = 5
    OnePair = 6
    HighCard = 7


cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


class Hand:
    def __init__(self, hand, bet):
        self.hand = [*hand]
        self.hand_type = Rank.HighCard
        self.bet = bet
        self.rank = None
        self.get_hand_type()

    def __repr__(self):
        return f"{self.hand} - {self.bet} - {self.hand_type}"

    def get_hand_type(self):
        dic = defaultdict(int)
        wilds = 0
        for card in self.hand:
            if card == "J":
                wilds += 1
                continue
            dic[card] += 1

        values = list(dic.values())
        values.sort()
        values.reverse()
        if len(values) == 0:
            values = [5]
        else:
            values[0] += wilds
        if values[0] == 5:
            self.hand_type = Rank.FiveOfKind
        elif values[0] == 4:
            self.hand_type = Rank.FourOfKind
        elif values[0] == 3 and values[1] == 2:
            self.hand_type = Rank.FullHouse
        elif values[0] == 3:
            self.hand_type = Rank.ThreeOfKind
        elif values[0] == 2 and values[1] == 2:
            self.hand_type = Rank.TwoPair
        elif values[0] == 2:
            self.hand_type = Rank.OnePair
        else:
            self.hand_type = Rank.HighCard


hands = []
for line in input:
    hand, bet = line.split(" ")
    hands.append(Hand(hand, bet))

hands.sort(
    key=lambda x: (10 - x.hand_type.value) * 1000000000
    + (14 - cards.index(x.hand[0])) * 1000000
    + (14 - cards.index(x.hand[1])) * 10000
    + (14 - cards.index(x.hand[2])) * 100
    + (14 - cards.index(x.hand[3]))
    + (14 - cards.index(x.hand[4])) / 100.0
)


total = 0

print("\n".join([x.__repr__() for x in hands]))
for i in range(len(hands)):
    total += int(hands[i].bet) * (i + 1)
print(total)
