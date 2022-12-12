import os

CURRENT_DIR = os.path.dirname(__file__)
INPUT_PATH = os.path.join(CURRENT_DIR, "input.txt")
SMALL_INPUT_PATH = os.path.join(CURRENT_DIR, "small_input.txt")


class Node:
    def __init__(self, name, is_directory, size) -> None:
        self.name = name
        self.children = []
        self.is_directory = is_directory
        self.size = size
        self.parent = None

    def add_child(self, child):
        if not self.get_child(child.name):
            self.children.append(child)
            child.parent = self
            if child.size > 0:
                update_parent_size(self, child.size)

    def get_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                return child
        return None


def update_parent_size(node, size):
    node.size += size
    if node.parent:
        update_parent_size(node.parent, size)


def load_commands(input_file):
    with open(input_file, "r") as f:
        for line in f:
            yield line.split()


def parse_filetree(input_file):
    # initialize with root dir
    root_dir = Node("/", is_directory=True, size=0)
    current_node = root_dir
    for command in load_commands(input_file):
        command_start = command[0]
        if command_start == "$":
            command_name = command[1]
            if command_name == "cd":
                dir_name = command[2]
                if dir_name == "/":
                    current_node = root_dir
                elif dir_name == "..":
                    current_node = current_node.parent
                else:
                    current_node = current_node.get_child(dir_name)
        elif command_start == "dir":
            new_dir = Node(name=command[1], is_directory=True, size=0)
            current_node.add_child(new_dir)
        else:
            file_size = int(command_start)
            file_name = command[1]
            new_file = Node(name=file_name, is_directory=False, size=file_size)
            current_node.add_child(new_file)
    return root_dir


def find_directories(subtree, filter):
    directories = []
    for node in subtree.children:
        if node.is_directory and filter(node):
            directories.append(node)
        directories.extend(find_directories(node, filter))
    return directories


def part1():
    tree = parse_filetree(INPUT_PATH)
    filtered_directories = find_directories(tree, lambda n: n.size < 100000)
    sum_directories = sum([node.size for node in filtered_directories])
    print(f"Sum of sizes of directories: {sum_directories}")


part1()


def part2():
    tree = parse_filetree(INPUT_PATH)
    TOTAL_DISC_SPACE = 70000000
    REQUIRED_DISC_SPACE = 30000000
    UNUSED_DISC_SPACE = TOTAL_DISC_SPACE - tree.size
    SPACE_TO_FREE = REQUIRED_DISC_SPACE - UNUSED_DISC_SPACE
    candidate_directories = find_directories(tree, lambda n: n.size > SPACE_TO_FREE)
    optimal_directory_size = min([node.size for node in candidate_directories])
    print(f"Size of optimal directory to delete: {optimal_directory_size}")


part2()
