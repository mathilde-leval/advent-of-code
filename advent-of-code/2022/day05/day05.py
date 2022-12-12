import os
import re

CURRENT_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURRENT_DIR, "input.txt")


def handle_stack_line(line, stacks):
    current_char = 0
    current_stack = 0
    while current_char < 36:
        current_crate = line[current_char + 1]
        if current_crate.isalpha():
            stacks[current_stack].insert(0, current_crate)
        current_char += 4
        current_stack += 1
    return stacks


MOVE_NUMBER_REGEX = r"move (\d*) from"
FROM_STACK_REGEX = r"from (\d*) to"
TO_STACK_REGEX = r"to (\d*)"


def parse_instruction(line):
    move = re.search(MOVE_NUMBER_REGEX, line).group(1)
    from_stack = re.search(FROM_STACK_REGEX, line).group(1)
    to_stack = re.search(TO_STACK_REGEX, line).group(1)
    return {
        "move": int(move),
        "from_stack": int(from_stack),
        "to_stack": int(to_stack),
    }


def load_stacks_and_instructions(input_path):
    stacks = [[] for _ in range(9)]
    instructions = []
    with open(input_path, "r") as f:
        line_number = 0
        for line in f:
            if line_number < 8:
                stacks = handle_stack_line(line, stacks)
            if line_number > 9:
                instructions.append(parse_instruction(line))
            line_number += 1
    return stacks, instructions


def apply_instructions_part1(stacks, instructions):
    for instruction in instructions:
        from_stack = stacks[instruction["from_stack"] - 1]
        to_stack = stacks[instruction["to_stack"] - 1]
        for _ in range(instruction["move"]):
            moving_crate = from_stack.pop()
            to_stack.append(moving_crate)


def apply_instructions_part2(stacks, instructions):
    for instruction in instructions:
        from_stack = stacks[instruction["from_stack"] - 1]
        to_stack = stacks[instruction["to_stack"] - 1]
        crates_to_extend = []
        for _ in range(instruction["move"]):
            moving_crate = from_stack.pop()
            crates_to_extend.insert(0, moving_crate)
        to_stack.extend(crates_to_extend)


def part_1(input_path):
    loaded_stacks, loaded_instructions = load_stacks_and_instructions(input_path)
    apply_instructions_part1(loaded_stacks, loaded_instructions)
    top_crates = [stack[-1] for stack in loaded_stacks]
    return "".join(top_crates)


def part_2(input_path):
    loaded_stacks, loaded_instructions = load_stacks_and_instructions(input_path)
    apply_instructions_part2(loaded_stacks, loaded_instructions)
    top_crates = [stack[-1] for stack in loaded_stacks]
    return "".join(top_crates)


top_crates_part1 = part_1(INPUT_PATH)
print(f"Top crates CrateMover 9000: {top_crates_part1}")

top_crates_part2 = part_2(INPUT_PATH)
print(f"Top crates CrateMover 9001: {top_crates_part2}")
