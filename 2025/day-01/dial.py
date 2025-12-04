# Link to puzzle: https://adventofcode.com/2025/day/1

from typing import List, Final
from pathlib import Path
from dataclasses import dataclass

# --- Configuration & Constants ---
PROJECT_DIR = Path(__file__).parent
SOURCE = PROJECT_DIR / "input.txt"

START_POSITION: Final[int] = 50
DIAL_SIZE: Final[int] = 100
DIRECTION_LEFT: Final[str] = "L"
DIRECTION_RIGHT: Final[str] = "R"


@dataclass
class Rotation:
    direction: str
    value: int


def parse_rotations(file_path: Path) -> List[Rotation]:
    """
    Parses the input file into a list of Rotation objects
    """
    rotations = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue

            direction = clean_line[0]
            value = int(clean_line[1:])
            rotations.append(Rotation(direction, value))

    return rotations


def solve_part_one(start_pos: int, rotations: List[Rotation]) -> int:
    """
    Counts how many times the dial stops exactly at 0
    """
    current_pos = start_pos
    zero_hits = 0

    for rot in rotations:
        if rot.direction == DIRECTION_LEFT:
            current_pos -= rot.value
        else:
            current_pos += rot.value

        # Normalise to circular dial
        current_pos %= DIAL_SIZE

        if current_pos == 0:
            zero_hits += 1

    return zero_hits


def solve_part_two(start_pos: int, rotations: List[Rotation]) -> int:
    """
    Counts how many times the dial PASSES or LANDS on 0
    """
    current_abs = start_pos
    total_crossings = 0

    for rotation in rotations:
        prev_abs = current_abs

        # Left rotation
        if rotation.direction == DIRECTION_LEFT:
            current_abs -= rotation.value
            # Count multiples of 100 in range (new_abs, current_abs)
            crossings = (prev_abs - 1) // DIAL_SIZE - (current_abs - 1) // DIAL_SIZE

        # Right rotation
        else:
            current_abs += rotation.value
            # Count multiples of 100 in range (current_abs, new_abs)
            crossings = current_abs // DIAL_SIZE - prev_abs // DIAL_SIZE

        total_crossings += crossings

    return total_crossings


def main():
    """
    Orchestrates the solution.
    """
    rotations = parse_rotations(SOURCE)
    if not rotations:
        return

    # Part 1
    print(f"Solution 1: {solve_part_one(START_POSITION, rotations)}")

    # Part 2
    print(f"Solution 2: {solve_part_two(START_POSITION, rotations)}")


if __name__ == "__main__":
    main()
