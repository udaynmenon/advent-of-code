# Link to puzzle: https://adventofcode.com/2025/day/2

import re
from typing import List
from pathlib import Path
from dataclasses import dataclass

# --- Configuration & Constants ---
PROJECT_DIR = Path(__file__).parent
INPUT_FILE = PROJECT_DIR / "input.txt"

# Regex to find IDs consisting of a sequence repeated one or more times
RE_REPETITIVE = re.compile(r"^(\d+)\1+$")


@dataclass
class Range:
    start: int
    end: int


def parse_id_ranges(file_path: Path) -> List[Range]:
    """
    Parses the input file and returns a list of Range objects
    """
    ranges = []

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().strip()

        raw_ranges = content.split(",")

        for raw_range in raw_ranges:
            start_str, end_str = raw_range.split("-")
            ranges.append(Range(int(start_str), int(end_str)))

    return ranges


def is_repetitive_part_one(value_str: str) -> bool:
    """
    Invalid if sequence repeats exactly twice
    """
    length = len(value_str)
    if length % 2 != 0:
        return False

    mid = length // 2

    return value_str[:mid] == value_str[mid:]


def is_repetitive_part_two(value_str: str) -> bool:
    """
    Invalid if sequence repeats at least two times
    """
    return bool(RE_REPETITIVE.match(value_str))


def calculate_invalid_id_sum(ranges: List[Range], part: int) -> int:
    """
    Iterates through all ranges and sums up IDs that are considered invalid
    """
    total_invalid_sum = 0

    for r in ranges:
        for num in range(r.start, r.end + 1):
            num_str = str(num)
            is_invalid = False

            if part == 1:
                is_invalid = is_repetitive_part_one(num_str)
            elif part == 2:
                is_invalid = is_repetitive_part_two(num_str)

            if is_invalid:
                total_invalid_sum += num

    return total_invalid_sum


def main():
    """
    Orchestrates the solution.
    """
    id_ranges = parse_id_ranges(INPUT_FILE)

    if not id_ranges:
        return

    # Part 1
    print(f"Solution 1: {calculate_invalid_id_sum(id_ranges, part=1)}")

    # Part 2
    print(f"Solution 2: {calculate_invalid_id_sum(id_ranges, part=2)}")


if __name__ == "__main__":
    main()
