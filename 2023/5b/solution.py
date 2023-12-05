# Adjust the path to the root of the project
import sys

sys.path.append(r"../../")

import re
from dataclasses import dataclass
from enum import Enum
from typing import List

from aoc.input_file import read_input

input = "\n".join(read_input())


class SeedRange:
    def __init__(self, start, length):
        self.start = start
        self.length = length

    def __repr__(self):
        return f"SeedRange({self.start}, {self.length})"


class MapRange:
    def __init__(self, line):
        self.dest_range, self.source_range, self.length = line.strip().split(" ")
        self.dest_range = int(self.dest_range)
        self.source_range = int(self.source_range)
        self.length = int(self.length)

    def contains(self, x: SeedRange):
        seed_min = x.start
        seed_max = x.start + x.length
        map_min = self.source_range
        map_max = self.source_range + self.length

        if seed_min >= map_max or seed_max <= map_min:
            return False
        return True

    def f(self, x: SeedRange):
        seed_min = x.start
        seed_max = x.start + x.length
        map_min = self.source_range
        map_max = self.source_range + self.length

        # 10 5
        # 2 30

        if seed_min < map_min and seed_max >= map_max:
            return SeedRange(self.dest_range, self.length), [
                SeedRange(seed_min, map_min - seed_min),
                SeedRange(map_max, seed_max - map_max),
            ]
        elif seed_min >= map_min and seed_max < map_max:
            diff = seed_min - map_min
            end_diff = map_max - seed_max
            return SeedRange(self.dest_range + diff, x.length), []
        elif seed_min >= map_min and seed_min < map_max and seed_max >= map_max:
            diff = seed_min - map_min
            return SeedRange(self.dest_range + diff, self.length - diff), [
                SeedRange(map_max, seed_max - map_max)
            ]
        elif seed_max >= map_min and seed_max < map_max and seed_min < map_min:
            diff = seed_max - map_min
            return SeedRange(self.dest_range, diff), [
                SeedRange(x.start, x.length - diff)
            ]
        else:
            print("ERROR")

    def __repr__(self):
        return f"MapRange({self.dest_range}, {self.source_range}, {self.length})"


seeds, rest = input.split("seed-to-soil map:")
seeds = re.findall(r"\d+", seeds)
seed_ranges = []
for i in range(int(len(seeds) / 2)):
    seed_ranges.append(SeedRange(int(seeds[i * 2]), int(seeds[(i * 2) + 1])))

print(seed_ranges)

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

    map_ranges.sort(key=lambda x: x.source_range)
    return map_ranges


# print(seed_to_soil)
seed_to_soil_map_ranges = get_map_ranges(seed_to_soil)
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

print("Processing")
all_locs = []
for seed in seed_ranges:
    current_paths = [seed]
    for a_range in ranges:
        print(f"Processing {len(current_paths)} paths")
        old_paths = current_paths.copy()
        current_paths = []

        for path in old_paths:
            i = 0
            for map_range in a_range:
                if map_range.contains(path):
                    # print(f"\nProcessing {path} with {map_range}")
                    new_path, leftovers = map_range.f(path)
                    # print(leftovers)
                    current_paths.append(new_path)
                    old_paths += leftovers
                    break
                i += 1

                if i == len(a_range):
                    current_paths.append(path)

    all_locs += current_paths
    print(f"Seed {seed} -> {len(current_paths)}")

for x in seed_to_soil_map_ranges:
    print(x)

print(all_locs)
print("Part 1:", min([x.start for x in all_locs]))
