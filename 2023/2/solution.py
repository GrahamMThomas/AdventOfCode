from enum import Enum
import re
import sys
sys.path.append(r'../../')

from dataclasses import dataclass
from typing import List
from aoc.input_file import read_input

input = read_input()



class MarbleColor(Enum):
    red = 1
    green = 2
    blue = 3

LIMITS = {
    MarbleColor.red: 12,
    MarbleColor.green: 13,
    MarbleColor.blue: 14
}

@dataclass
class MarblePull:
    num: int
    color: MarbleColor

def is_game_possible(line) -> bool:
    games = line.split(': ')[1].split('; ')
    for game in games:
        entries = []

        str_entries = [x.strip() for x in game.split(', ')]
        for entry in str_entries:
            re_entry = re.match(r'(\d+) (\w+)', entry)
            entries.append(MarblePull(int(re_entry.group(1)), MarbleColor[re_entry.group(2)]))
            if not validate_entries(entries):
                return False
    return True

def validate_entries(entries: List[MarblePull]) -> bool:
    for entry in entries:
        if entry.num > LIMITS[entry.color]:
            return False
    return True

total = 0
for line in input:
    game_id = int(line.split(':')[0][5:])
    if(is_game_possible(line)):
        total += game_id

print(total)