import re


input = ""
with open("input.txt", "r") as f:
    input = f.read()

valid_numerics = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def replace_word_with_digit(line: str):
    new_line = ""
    offset = 0
    for i in range(len(line)):
        replaced = False

        for j in range(len(valid_numerics)):
            if line[i + offset :].startswith(valid_numerics[j]):
                replaced = True
                offset += len(valid_numerics[j]) - 2
                new_line += str(j + 1)
                break

        if i + offset >= len(line):
            break
        if not replaced:
            new_line += line[i + offset]

    return new_line


def get_digit(line: str):
    new_lien = replace_word_with_digit(line)
    all_digits = [x for x in new_lien if x.isdigit()]
    return all_digits[0] + all_digits[-1]


print(sum([int(get_digit(line)) for line in input.split("\n")]))
#
# print(input)
# for i in range(10):
#     line = input.split("\n")[i + 120]
#     print(line + " - " + get_digit(replace_word_with_digit(line)))

# print(replace_word_with_digit("gnmkdm7sevenseven3four7fhrhppmtkpzvtlfqoneighth"))
