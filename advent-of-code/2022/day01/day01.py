import os

CURRENT_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURRENT_DIR, "input.txt")


def load_calories(input_path):
    calories = []
    with open(input_path, "r") as f:
        current_calories = 0
        for line in f:
            if line == "\n":
                calories.append(current_calories)
                current_calories = 0
            else:
                current_calories += int(line)
    return calories


# solve part 1
elves_calories = load_calories(INPUT_PATH)
max_calories = max(elves_calories)
print(f"Max calories: {max_calories}")

# solve part 2
top_3_calories = sorted(elves_calories, reverse=True)[:3]
summed_calories = sum(top_3_calories)
print(f"Summed top 3 calories: {summed_calories}")
