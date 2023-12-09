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


class MarbleColor(Enum):
    red = 1
    green = 2
    blue = 3


LIMITS = {MarbleColor.red: 12, MarbleColor.green: 13, MarbleColor.blue: 14}


@dataclass
class MarblePull:
    num: int
    color: MarbleColor


def get_game_cube(line) -> int:
    games = line.split(": ")[1].split("; ")
    maximums = {MarbleColor.red: 0, MarbleColor.green: 0, MarbleColor.blue: 0}
    for game in games:
        entries = []

        str_entries = [x.strip() for x in game.split(", ")]

        for entry in str_entries:
            re_entry = re.match(r"(\d+) (\w+)", entry)
            maximums[MarbleColor[re_entry.group(2)]] = max(
                maximums[MarbleColor[re_entry.group(2)]], int(re_entry.group(1))
            )

    return (
        maximums[MarbleColor.blue]
        * maximums[MarbleColor.green]
        * maximums[MarbleColor.red]
    )


total = 0
for line in input:
    game_id = int(line.split(":")[0][5:])
    total += get_game_cube(line)

print(total)
