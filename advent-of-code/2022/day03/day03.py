import os

CURRENT_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURRENT_DIR, "input.txt")


def load_rucksacks(input_path):
    with open(input_path, "r") as f:
        for line in f:
            yield line.strip()


def get_item_priority(item):
    item_code = ord(item)
    if item_code >= ord("a"):
        return 1 + item_code - ord("a")
    else:
        return 27 + item_code - ord("A")


def part_1(input_path):
    priority_sum = 0
    for line in load_rucksacks(input_path):
        middle_index = int(len(line) / 2)
        first_compartment = set(line[:middle_index])
        second_compartment = set(line[middle_index:])
        intersection = list(first_compartment.intersection(second_compartment))
        duplicated_item = intersection[0]
        priority_sum += get_item_priority(duplicated_item)
    return priority_sum


def part_2(input_path):
    priority_sum = 0
    all_lines = list(load_rucksacks(input_path))
    current_line = 0
    while current_line < len(all_lines):
        first_elf = set(all_lines[current_line])
        second_elf = set(all_lines[current_line + 1])
        third_elf = set(all_lines[current_line + 2])
        current_line += 3
        intersection = list(first_elf.intersection(second_elf).intersection(third_elf))
        common_item = intersection[0]
        priority_sum += get_item_priority(common_item)
    return priority_sum


priority_sum_part_1 = part_1(INPUT_PATH)
print(f"Sum of priorities part 1: {priority_sum_part_1}")

priority_sum_part_2 = part_2(INPUT_PATH)
print(f"Sum of priorities part 2: {priority_sum_part_2}")
