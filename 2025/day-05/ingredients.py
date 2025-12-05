# Link to puzzle: https://adventofcode.com/2025/day/5

from typing import List, Final
from pathlib import Path
from dataclasses import dataclass

# --- Configuration & Constants ---
PROJECT_DIR = Path(__file__).parent
SOURCE = PROJECT_DIR / "test.txt"


@dataclass
class Range:
    start: int
    end: int


id_ranges = []


def parse_ingredients(file_path: Path) -> set:
    available_ingredients = set()

    ingredients_mode = False

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()

            if not clean_line:
                ingredients_mode = True
                continue

            if not ingredients_mode:
                raw_ranges = clean_line.split(",")

                for raw_range in raw_ranges:
                    start_str, end_str = raw_range.split("-")
                    id_ranges.append(Range(int(start_str), int(end_str)))

            else:
                available_ingredients.add(int(clean_line))

    # print(id_ranges)
    # print("tasdtsadt")
    # print(available_ingredients)

    return available_ingredients


def in_range(ingredient: int) -> bool:
    for r in id_ranges:
        if ingredient >= r.start and ingredient <= r.end:
            return True
    return False


def merge_overlapping_ranges():
    sorted_ranges = sorted(id_ranges, key=lambda r: r.start)

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


def solve_part_one(ingredients: set) -> int:
    total_fresh = 0

    for ingredient in ingredients:
        if in_range(ingredient):
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
    available_ingredients = parse_ingredients(SOURCE)
    if not available_ingredients:
        return

    # Part 1
    print(f"Solution 1: {solve_part_one(available_ingredients)}")

    # Part 2
    print(f"Solution 2: {solve_part_two(merge_overlapping_ranges())}")


if __name__ == "__main__":
    main()
