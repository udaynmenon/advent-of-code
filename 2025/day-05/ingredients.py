# Link to puzzle: https://adventofcode.com/2025/day/5

from typing import List, Tuple, Set
from pathlib import Path
from dataclasses import dataclass

# --- Configuration & Constants ---
PROJECT_DIR = Path(__file__).parent
SOURCE = PROJECT_DIR / "input.txt"


@dataclass
class Range:
    start: int
    end: int


def parse_ingredients(file_path: Path) -> Tuple[List[Range], Set[int]]:
    """
    Parses the input file into two datasets:
    1. A list of fresh ingredient ID ranges.
    2. A set of specific available ingredient IDs to check.
    """
    raw_id_ranges: List[Range] = []
    available_ingredients: Set[int] = set()
    parse_range_mode = True

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()

            if not clean_line:
                parse_range_mode = False
                continue

            if parse_range_mode:
                raw_ranges = clean_line.split(",")

                for raw_range in raw_ranges:
                    start_str, end_str = raw_range.split("-")
                    raw_id_ranges.append(Range(int(start_str), int(end_str)))

            else:
                available_ingredients.add(int(clean_line))

    return raw_id_ranges, available_ingredients


def is_fresh(ingredient_id: int, id_ranges: List[Range]) -> bool:
    for r in id_ranges:
        if r.start <= ingredient_id <= r.end:
            return True

        if r.start > ingredient_id:
            return False
    return False


def merge_overlapping_ranges(raw_id_range: List[Range]) -> List[Range]:
    sorted_ranges = sorted(raw_id_range, key=lambda r: r.start)

    merged = list()

    current_range = sorted_ranges[0]

    for r in sorted_ranges[1:]:
        if r.start <= current_range.end + 1:
            current_range.end = max(current_range.end, r.end)
        else:
            merged.append(current_range)

            current_range = r

    merged.append(current_range)

    return merged


def solve_part_one(ingredients: set, id_ranges: List[Range]) -> int:
    total_fresh = 0

    for ingredient in ingredients:
        if is_fresh(ingredient, id_ranges):
            total_fresh += 1

    return total_fresh


def solve_part_two(new_ranges: List[Range]) -> int:
    total_fresh = 0

    for r in new_ranges:
        count = r.end - r.start + 1
        total_fresh += count

    return total_fresh


def main():
    """
    Orchestrates the solution.
    """
    raw_id_ranges, available_ingredients = parse_ingredients(SOURCE)
    if not raw_id_ranges and available_ingredients:
        return

    merged_id_ranges = merge_overlapping_ranges(raw_id_ranges)

    # Part 1
    print(f"Solution 1: {solve_part_one(available_ingredients, merged_id_ranges)}")

    # Part 2
    print(f"Solution 2: {solve_part_two(merged_id_ranges)}")


if __name__ == "__main__":
    main()
