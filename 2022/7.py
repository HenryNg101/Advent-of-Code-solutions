import time

start_time = time.process_time()
# Custom directory's tree data structure
class Directory:
    def __init__(self, parent_dir=None) -> None:
        self.parent_dir = parent_dir
        self.directories = dict()   # Contains Directory objects, mapped by the dir's name
        self.size = 0

# Main algo here, traverse filesystem's tree first, add final size of child dirs later
def traverse(root: Directory):
    global sum_dirs

    for dir in root.directories.values():
        root.size += traverse(dir)
    if root.size <= 100000:
        sum_dirs += root.size
    return root.size

def find_min_dir_with_threshold(root: Directory, min_sz: int):
    global min_dir_sz

    if root.size >= min_sz:
        min_dir_sz = min(root.size, min_dir_sz)
    for dir in root.directories.values():
        find_min_dir_with_threshold(dir, min_sz)

sum_dirs = 0   #Task A result
min_dir_sz = 30000000   #Task B result
root = Directory()
curr_dir = root

content = open("input").read().split('\n')
content.pop()
for line in content:
    tokens = line.split()
    # Handle the command
    if tokens[0] == '$' and tokens[1] == 'cd':
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
        elif tokens[0].isnumeric():
            curr_dir.size += int(tokens[0])

traverse(root)
find_min_dir_with_threshold(root, 30000000 - (70000000 - root.size))
print(f'Part a answer is: {sum_dirs}')
print(f'Part b answer is: {min_dir_sz}')
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
