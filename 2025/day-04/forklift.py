# Link to puzzle: https://adventofcode.com/2025/day/4

from typing import List, Tuple, Final
from pathlib import Path

# Configuration and contants
PROJECT_DIR = Path(__file__).parent
SOURCE = PROJECT_DIR / "./input.txt"

CHAR_PAPER: Final[str] = "@"
VAL_PAPER: Final[int] = 1
VAL_EMPTY: Final[int] = 0

ADJACENT_DELTAS: Final[List[Tuple[int, int]]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

Grid = List[List[int]]


def parse_grid(file_path: Path) -> Grid:
    """
    Parse input file and create a binary grid
    """
    grid = list()
    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.rstrip("\n")
            if not clean_line:
                continue

            row = []
            for char in clean_line:
                if char == CHAR_PAPER:
                    row.append(VAL_PAPER)
                else:
                    row.append(VAL_EMPTY)
            grid.append(row)

    return grid


def is_acessible(grid: Grid, i: int, j: int) -> bool:
    """
    Returns True if more than 3 adjacent cells have value 1
    """
    r = len(grid)
    c = len(grid[0])

    neighbours = 0

    for dr, dc in ADJACENT_DELTAS:
        nr, nc = i + dr, j + dc

        # Check Bounds
        if 0 <= nr < r and 0 <= nc < c:
            if grid[nr][nc] == VAL_PAPER:
                neighbours += 1

            if neighbours > 3:
                return True

    return False


def get_accessible_rolls(grid: Grid) -> List[Tuple[int, int]]:
    """
    Identifies and returns all paper rolls that are currently accessible.
    """
    rows, cols = len(grid), len(grid[0])

    accessible_rolls = list()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == VAL_PAPER:
                if not is_acessible(grid, r, c):
                    accessible_rolls.append((r, c))

    return accessible_rolls


def solve_part_one(grid: Grid) -> int:
    accessible = get_accessible_rolls(grid)
    return len(accessible)


def solve_part_two(grid: Grid) -> int:
    """
    Returns the total number of rolls removed.
    """

    total_removed = 0

    while True:
        accessible_rolls = get_accessible_rolls(grid)

        if not accessible_rolls:
            break

        total_removed += len(accessible_rolls)

        # Removing accessible rolls
        for r, c in accessible_rolls:
            grid[r][c] = VAL_EMPTY

    return total_removed


def main():
    """
    Orchestrates the solution.
    """
    grid = parse_grid(SOURCE)
    if not grid:
        return

    # Part 1
    print(f"Solution 1: {solve_part_one(grid)}")

    # Part 2
    print(f"Solution 2: {solve_part_two(grid)}")


if __name__ == "__main__":
    main()
