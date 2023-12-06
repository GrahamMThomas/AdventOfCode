# Adjust the path to the root of the project
import sys

sys.path.append(r"../../")

import re
from dataclasses import dataclass
from enum import Enum
from typing import List

from aoc.input_file import read_input

input = read_input()


class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def __repr__(self) -> str:
        return f"Race({self.time}, {self.distance})"

    def calc_distance(self, button_time):
        speed = button_time
        return speed * (self.time - button_time)

    def beats(self, button_time):
        return self.calc_distance(button_time) > self.distance


times = re.findall(r"(\d+)", input[0])
distances = re.findall(r"(\d+)", input[1])

my_time = "".join(times)
my_distance = "".join(distances)
race = Race(int(my_time), int(my_distance))


wins = 0
for second in range(race.time):
    if race.beats(second):
        wins += 1

print(wins)
