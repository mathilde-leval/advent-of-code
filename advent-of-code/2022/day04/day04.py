import os

CURRENT_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURRENT_DIR, "input.txt")


def load_assignments(input_path):
    with open(input_path, "r") as f:
        for line in f:
            first_assignment, second_assignment = line.split(",")
            a, b = first_assignment.split("-")
            c, d = second_assignment.split("-")
            yield {
                "a": int(a.strip()),
                "b": int(b.strip()),
                "c": int(c.strip()),
                "d": int(d.strip()),
            }


def is_fully_contained(assignment):
    return (
        assignment["d"] >= assignment["b"] and assignment["c"] <= assignment["a"]
    ) or (assignment["b"] >= assignment["d"] and assignment["a"] <= assignment["c"])


def no_overlap(assignment):
    return assignment["c"] > assignment["b"] or assignment["a"] > assignment["d"]


def part_1(input_path):
    fully_contained_assignments_sum = 0
    for assignment in load_assignments(input_path):
        if is_fully_contained(assignment):
            fully_contained_assignments_sum += 1
    return fully_contained_assignments_sum


def part_2(input_path):
    overlap_sum = 0
    for assignment in load_assignments(input_path):
        if not no_overlap(assignment):
            overlap_sum += 1
    return overlap_sum


sum_part_1 = part_1(INPUT_PATH)
print(f"Sum of fully contained assignments: {sum_part_1}")
sum_part_2 = part_2(INPUT_PATH)
print(f"Sum of overlapping assignments: {sum_part_2}")
