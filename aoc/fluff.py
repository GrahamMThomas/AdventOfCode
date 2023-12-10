from pathlib import Path
import re
from typing import List


def print_intro(path_to_solution: str, input: List[str]) -> None:
    path = Path(path_to_solution).parts
    day = path[-2]
    part = "B" if "b" in day else "A"
    day = int(re.findall(r"\d+", day)[0])
    year = path[-3]

    intro_message = f"Advent of Code {year} - Day {day} Part {part}"
    input_message = f"Input: {len(input)} lines"
    santa = "🦌🛷🎅"
    left = 25 - day + 1

    print()
    print(f"🎄{'⬛' * left}{santa}{'✨'*(day-1)}")
    print(" " * 13 + intro_message)
    print(" " * int(13 + (len(intro_message) - len(input_message)) / 2) + input_message)
    print()
