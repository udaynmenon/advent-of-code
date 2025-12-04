# Link to puzzle: https://adventofcode.com/2025/day/3

from typing import List, Final
from pathlib import Path

# --- Configuration & Constants ---
PROJECT_DIR = Path(__file__).parent
SOURCE = PROJECT_DIR / "input.txt"

# Number of digits required for each part of the puzzle
PART_ONE_TARGET_LENGTH: Final[int] = 2
PART_TWO_TARGET_LENGTH: Final[int] = 12

BatteryBank = List[int]


def parse_battery_banks(file_path: Path) -> List[BatteryBank]:
    battery_banks = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue

            bank = [int(digit) for digit in clean_line]
            battery_banks.append(bank)

    return battery_banks


def solve_max_subsequence(bank: BatteryBank, length: int) -> int:
    """
    Returns largest number possible K-length subsequence digits
    """
    n = len(bank)
    if n < length:
        return 0

    # Number of digits we can drop to get a valid number
    drop_quota = n - length
    stack: List[int] = []

    for digit in bank:
        # Decreasing stack
        while stack and stack[-1] < digit and drop_quota > 0:
            stack.pop()
            drop_quota -= 1

        stack.append(digit)

    # Truncate to target length
    final_digits = stack[:length]

    # Combine digits to form number
    result = int("".join(map(str, final_digits)))

    return result


def calculate_total_joltage(banks: List[BatteryBank], length) -> int:
    """
    Calculates the sum of maximum joltages for all banks based on the mode.
    """
    total_joltage = 0

    for bank in banks:
        max_joltage = solve_max_subsequence(bank, length)

        total_joltage += max_joltage

    return total_joltage


def main():
    """
    Orchestrates the solution.
    """
    battery_banks = parse_battery_banks(SOURCE)
    if not battery_banks:
        return

    # Part 1
    print(
        f"Solution 1: {calculate_total_joltage(battery_banks, PART_ONE_TARGET_LENGTH)}"
    )

    # Part 2
    print(
        f"Solution 2: {calculate_total_joltage(battery_banks, PART_TWO_TARGET_LENGTH)}"
    )


if __name__ == "__main__":
    main()
