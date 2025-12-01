from typing import List
from pathlib import Path
from dataclasses import dataclass

PROJECT_DIR = Path(__file__).parent
SOURCE = PROJECT_DIR / "./input.txt"


@dataclass
class Rotation:
    direction: str
    value: int


# Reading turns from file
def read_rotations(file_path: Path) -> List[Rotation]:
    rotations = list()
    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.rstrip("\n")
            rotations.append(Rotation(clean_line[0], int(clean_line[1:])))
    return rotations


# Computing new position
def rotate(position: int, rotation: Rotation) -> int:
    if rotation.direction == "L":
        new_position = position - rotation.value
    else:
        new_position = position + rotation.value

    return new_position


def password_basic(current_position: int, rotations: List[Rotation]) -> int:
    password = 0

    for rotation in rotations:
        position = rotate(current_position, rotation)
        current_position = position % 100
        print(
            f"Rotation: {rotation.direction} {rotation.value} | New position: {current_position}"
        )
        if current_position == 0:
            password += 1

    return password


def password_advanced(start_position: int, rotations: List[Rotation]) -> int:
    current = start_position
    total_zeroes_crossed = 0

    for rotation in rotations:
        if rotation.direction == "L":
            absolute_position = current - rotation.value
            zeroes_crossed = (current - 1) // 100 - (absolute_position - 1) // 100
        else:
            absolute_position = current + rotation.value
            zeroes_crossed = absolute_position // 100 - current // 100

        print(
            f"{rotation.direction}{rotation.value}: {current} -> {absolute_position} | Zeroes crossed: {zeroes_crossed}"
        )
        total_zeroes_crossed += zeroes_crossed
        current = absolute_position

    return total_zeroes_crossed


# --- Execution ---
rotations = read_rotations(SOURCE)
current_position = 50

# ---------------------------------------------------------------------------- #
#                                    Result                                    #
# ---------------------------------------------------------------------------- #

print(f"Starting at: {current_position}")

print(
    "# ----------------------------------- BASIC ---------------------------------- #"
)
print(f"Password Basic: {password_basic(current_position, rotations)}")
print(
    "# --------------------------------- ADVANCED --------------------------------- #"
)
print(f"Password Advanced: {password_advanced(current_position, rotations)}")
