import os

CURRENT_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURRENT_DIR, "input.txt")


LINE_TO_SCORE_PART_1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

LINE_TO_SCORE_PART_2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


def load_rounds(input_path):
    with open(input_path, "r") as f:
        for line in f:
            yield line


def compute_score(input_path, score_dict):
    total_score = 0
    for line in load_rounds(input_path):
        score = score_dict[line.strip()]
        total_score += score
    return total_score


total_score_part_1 = compute_score(INPUT_PATH, LINE_TO_SCORE_PART_1)
print(f"Total score part 1: {total_score_part_1}")

total_score_part_2 = compute_score(INPUT_PATH, LINE_TO_SCORE_PART_2)
print(f"Total score part 2: {total_score_part_2}")
