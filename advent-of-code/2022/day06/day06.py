import os

CURRENT_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURRENT_DIR, "input.txt")


def load_datastream(input_file):
    with open(input_file, "r") as f:
        return f.read()


def get_start_of_entity(input_file, marker_length):
    datastream = load_datastream(input_file)
    current_char = 0
    while current_char < len(datastream) - marker_length:
        marker_candidate = datastream[current_char : current_char + marker_length]
        if len(set(marker_candidate)) == marker_length:
            return current_char + marker_length
        current_char += 1
    raise ValueError("No start of packet marker found.")


start_of_packet = get_start_of_entity(INPUT_PATH, marker_length=4)
print(f"Start of packet characters: {start_of_packet}")
start_of_message = get_start_of_entity(INPUT_PATH, marker_length=14)
print(f"Start of message characters: {start_of_message}")
