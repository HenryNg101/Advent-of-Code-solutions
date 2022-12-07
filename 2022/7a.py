# Custom directory's tree data structure
class Directory:
    def __init__(self, parent_dir=None) -> None:
        self.parent_dir = parent_dir
        self.directories = dict()  # Contains Directory objects, mapped by the dir's name
        self.size = 0


# Main algo here, traverse filesystem's tree first, add final size of child dirs later
def traverse(root: Directory):
    global sum_dirs

    for dir in root.directories.values():
        root.size += traverse(dir)
    if root.size <= 100000:
        sum_dirs += root.size
    return root.size


sum_dirs = 0
root = Directory()
curr_dir = root  # The one that tracks where you are in filesystem

content = open("input").read().split('\n')
content.pop()
for line in content:
    tokens = line.split()

    # Handle the command
    if tokens[0] == '$':
        if tokens[1] == 'ls':
            continue
        if tokens[2] == '/':
            curr_dir = root
        elif tokens[2] == '..':
            curr_dir = curr_dir.parent_dir
        else:
            curr_dir = curr_dir.directories[tokens[2]]

    # Handle "ls" command's output
    else:
        if tokens[0] == 'dir':
            if tokens[1] not in curr_dir.directories:
                curr_dir.directories[tokens[1]] = Directory(curr_dir)
        else:
            curr_dir.size += int(tokens[0])

traverse(root)
print(sum_dirs)
