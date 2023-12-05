# Adjust the path to the root of the project
import sys

sys.path.append(r"../../")

import re
from dataclasses import dataclass
from enum import Enum
from typing import List

from aoc.input_file import read_input

input = "\n".join(read_input())


class MapRange:
    def __init__(self, line):
        print(line)
        self.dest_range, self.source_range, self.length = line.strip().split(" ")
        self.dest_range = int(self.dest_range)
        self.source_range = int(self.source_range)
        self.length = int(self.length)

    def contains(self, x):
        return x >= self.source_range and x < self.source_range + self.length

    def f(self, x):
        diff = x - self.source_range
        return self.dest_range + diff

    def __repr__(self):
        return f"MapRange({self.dest_range}, {self.source_range}, {self.length})"


seeds, rest = input.split("seed-to-soil map:")
seeds = re.findall(r"\d+", seeds)

seed_to_soil, rest = rest.split("soil-to-fertilizer map:")
soil_to_fertilizer, rest = rest.split("fertilizer-to-water map:")
fertilizer_to_water, rest = rest.split("water-to-light map:")
water_to_light, rest = rest.split("light-to-temperature map:")
light_to_temperature, rest = rest.split("temperature-to-humidity map:")
temperature_to_humidity, rest = rest.split("humidity-to-location map:")


def get_map_ranges(map_string):
    map_ranges = []
    for line in map_string.split("\n"):
        if len(line) < 3 and len(map_ranges) > 1:
            break
        elif len(line) > 3:
            map_ranges.append(MapRange(line))

    return map_ranges


# print(seed_to_soil)
seed_to_soil_map_ranges = get_map_ranges(seed_to_soil)
print(seed_to_soil_map_ranges)
soil_to_fertilizer_map_ranges = get_map_ranges(soil_to_fertilizer)
fertilizer_to_water_map_ranges = get_map_ranges(fertilizer_to_water)
water_to_light_map_ranges = get_map_ranges(water_to_light)
light_to_temperature_map_ranges = get_map_ranges(light_to_temperature)
temperature_to_humidity_map_ranges = get_map_ranges(temperature_to_humidity)
humidity_to_location_map_ranges = get_map_ranges(rest)

ranges = [
    seed_to_soil_map_ranges,
    soil_to_fertilizer_map_ranges,
    fertilizer_to_water_map_ranges,
    water_to_light_map_ranges,
    light_to_temperature_map_ranges,
    temperature_to_humidity_map_ranges,
    humidity_to_location_map_ranges,
]


all_locs = []
for seed in seeds:
    x = int(seed)

    current_loc = x
    for a_range in ranges:
        for map_range in a_range:
            if map_range.contains(current_loc):
                print(f"\t{current_loc}")
                current_loc = map_range.f(current_loc)
                break

    all_locs.append(current_loc)
    print(f"Seed {x} -> {current_loc}")

print("Part 1:", min(all_locs))
