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

races = []
for i in range(len(times)):
    races.append(Race(int(times[i]), int(distances[i])))

win_per_race = []
for race in races:
    wins = 0
    for second in range(race.time):
        if race.beats(second):
            wins += 1
    win_per_race.append(wins)

print(win_per_race[0] * win_per_race[1] * win_per_race[2] * win_per_race[3])
