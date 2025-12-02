from typing import List
from pathlib import Path
from dataclasses import dataclass

PROJECT_DIR = Path(__file__).parent
SOURCE = PROJECT_DIR / "./input.txt"


@dataclass
class Range:
    start: str
    end: str


# Reading turns from file
def read_id_ranges(file_path: Path) -> List[Range]:
    id_ranges = list()
    with open(file_path, "r") as file:
        ranges = file.readline().split(",")

        for id_range in ranges:
            split_location = id_range.find("-")
            start_val = id_range[0:split_location]
            end_val = id_range[split_location + 1 :]
            id_ranges.append(Range(start_val, end_val))
    return id_ranges


def is_valid(value: str) -> bool:
    id_length = len(value)
    half_id = id_length // 2
    # print(f"value[:half_id] {value[:half_id]} == value[half_id:] {value[half_id:]}")

    if id_length % 2 != 0:
        return True

    if value[:half_id] == value[half_id:]:
        return False
    else:
        return True


def invalid_sum(ranges: List[Range]) -> int:
    sum = 0
    for id_range in ranges:
        for i in range(int(id_range.start), int(id_range.end) + 1):
            if not is_valid(str(i)):
                sum += i

    return sum


print(invalid_sum(read_id_ranges(SOURCE)))
# print(invalid_sum([Range("11", "22")]))
