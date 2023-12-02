from typing import List

def read_input(filename: str = 'input.txt') -> List[str]:
    with open(filename, 'r') as f:
        input = f.read().splitlines()
        print(f"Loaded input from file. {len(input)} lines")
        return input