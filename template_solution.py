# Adjust the path to the root of the project for library access
import sys

sys.path.append(r"../../")

import re
from dataclasses import dataclass
from enum import Enum
from typing import List
from collections import defaultdict
from datetime import datetime
from aoc.input_file import read_input
from aoc.fluff import print_intro

input = read_input()
print_intro(__file__, input)
start = datetime.now()

## Solution ##


## Perf ##
print(f"Time taken: {((datetime.now() - start).total_seconds() * 1000):.2f}ms")
