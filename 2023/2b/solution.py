import sys

sys.path.append(r"../../")

from enum import Enum
import re
from dataclasses import dataclass
from typing import List
from aoc.input_file import read_input

input = read_input()


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
