import re


input = ""
with open("input.txt", "r") as f:
    input = f.read()


def get_digit(line: str):
    all_digits = [x for x in line if x.isdigit()]
    return all_digits[0] + all_digits[-1]


print(sum([int(get_digit(line)) for line in input.split("\n")]))
