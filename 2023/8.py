from typing import Set, List
import math

# Find out required steps for each node in the list to reach one of the valid end node(s)
def required_steps(start_nodes: List[str], valid_end_nodes: Set[str]) -> List[int]:
    sides = {'L': 0, 'R': 1}

    required_steps_arr = []
    for start in start_nodes:
        cnt = 0

        while start not in valid_end_nodes:
            inst_id = cnt % len(instructions)
            start = mp[start][sides[instructions[inst_id]]]
            cnt += 1

        required_steps_arr.append(cnt)

    return required_steps_arr

input = open("input").readlines()

instructions = input[0][:-1]
mp = dict()

#Contains start and end nodes that satisfied requirements for part 2
start_nodes, valid_end_nodes = [], set()

# Get start node, and left and right end nodes in each line
for i in range(2, len(input)):
    start, dests = input[i].split(' = ')
    left, right = dests.split()
    left = left[1:-1]
    right = right[:-1]

    mp[start] = (left, right)
    if start[-1] == 'A':
        start_nodes.append(start)
    if left[-1] == 'Z':
        valid_end_nodes.add(left)
    if right[-1] == 'Z':
        valid_end_nodes.add(right)

# Part 1
print(f"Part 1: {required_steps(['AAA'], set(['ZZZ']))[-1]}")

# Part 2
required_steps_arr = required_steps(start_nodes, valid_end_nodes)

# Find LCM
for i in range(1, len(required_steps_arr)):
    required_steps_arr[i] = required_steps_arr[i] * required_steps_arr[i-1] // math.gcd(required_steps_arr[i], required_steps_arr[i-1])

print(f"Part 2: {required_steps_arr[-1]}")