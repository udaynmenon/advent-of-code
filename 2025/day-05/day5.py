# Link to puzzle: https://adventofcode.com/2025/day/5

from typing import List, Final
from pathlib import Path

# Configuration and contants
PROJECT_DIR = Path(__file__).parent
SOURCE = PROJECT_DIR / "input.txt"


def parse_file(file_path: Path) -> int:
    return 0


def solve_part_one() -> int:
    return 0


def solve_part_two() -> int:
    return 0


def main():
    """
    Orchestrates the solution.
    """
    var = parse_file(SOURCE)
    if not var:
        return

    # Part 1
    print(f"Solution 1: {solve_part_one()}")

    # Part 2
    print(f"Solution 2: {solve_part_two()}")


if __name__ == "__main__":
    main()
