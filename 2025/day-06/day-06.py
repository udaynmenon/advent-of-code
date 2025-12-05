from typing import List, Any, Tuple, Final
from pathlib import Path
from dataclasses import dataclass

# --- Configuration & Constants ---
PROJECT_DIR = Path(__file__).parent
INPUT_FILE = PROJECT_DIR / "input.txt"


def parse_input(file_path: Path) -> Any:
    """
    Parses the input file into a usable data structure
    """
    data = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue

            # TODO: Parse logic here
            # data.append(clean_line)
            pass

    return data


def solve_part_one(data: Any) -> int:
    """
    Solves Part 1 of the puzzle.
    """
    result = 0
    # TODO: Implement Part 1 logic
    return result


def solve_part_two(data: Any) -> int:
    """
    Solves Part 2 of the puzzle.
    """
    result = 0
    # TODO: Implement Part 2 logic
    return result


def main():
    """
    Orchestrates the solution.
    """
    # Parse Input
    data = parse_input(INPUT_FILE)

    if data is None:
        print("No data loaded. Exiting.")
        return

    # Part 1
    print(f"Solution 1: {solve_part_one(data)}")

    # Part 2
    print(f"Solution 2: {solve_part_two(data)}")


if __name__ == "__main__":
    main()
