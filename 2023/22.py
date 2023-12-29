from collections import defaultdict
from copy import deepcopy
import sys
import time
import functools as ft

# Start the timer
start_time = time.time()

def is_supporting(brick1, brick2):
    # (sx1, sy1, sz1), (ex1, ey1, ez1) = brick1
    # (sx2, sy2, sz2), (ex2, ey2, ez2) = brick2

    brick1 = set([tuple(cube) for cube in brick1])
    brick2 = set([tuple(cube) for cube in brick2])
    
    for (x, y, z) in brick1:
        if (x, y, z+1) not in brick1 and (x, y, z+1) in brick2:
            return True
        
    return False

def kahn(start_id, indegrees):
    st = [start_id]
    res = -1
    while st:
        curr = st.pop()
        res += 1

        for next in mp[curr]:
            indegrees[next] -= 1
            if indegrees[next] == 0:
                st.append(next)
    return res

input = [line.strip() for line in open("input").readlines()]
bricks = []
for line in input:
    start, end = line.split("~")
    start_x, start_y, start_z = [int(x) for x in start.split(",")]
    end_x, end_y, end_z = [int(x) for x in end.split(",")]

    # Add every single cube for each brick ? Damn
    if start_z != end_z:
        bricks.append([(start_x, start_y, z) for z in range(start_z, end_z + 1)])

    elif start_y != end_y:
        bricks.append([(start_x, y, start_z) for y in range(start_y, end_y + 1)])

    else:
        bricks.append([(x, start_y, start_z) for x in range(start_x, end_x + 1)])

cubes_positions = set([(x, y, z) for brick in bricks for (x, y, z) in brick])

# Simulate bricks falling until stop
while True:
    continue_simulation = False
    for i, brick in enumerate(bricks):
        # Skip the currently removed brick, for sure

        is_brick_fall = True
        for (x, y, z) in brick:
            is_brick_fall &= (z > 1) and ((x, y, z - 1) not in cubes_positions or (x, y, z - 1) in brick)
            if not is_brick_fall:
                break
                
        if is_brick_fall:
            continue_simulation = True
            for (x, y, z) in brick:
                cubes_positions.discard((x, y, z))
                cubes_positions.add((x, y, z - 1))
            bricks[i] = [(x, y, z - 1) for (x, y, z) in brick]
            
    if not continue_simulation:
        break

# print(f"Elapsed time: {time.time() - start_time} seconds")

# This needed to be optimized
mp = defaultdict(list)
indegrees = defaultdict(int)

# for i in range(len(bricks)):
#     bricks[i] = (bricks[i][0], bricks[i][-1])

# sys.exit(0)
for i in range(len(bricks)):
    for j in range(i+1, len(bricks)):
        if is_supporting(bricks[i], bricks[j]):
            mp[i].append(j)
            indegrees[j] += 1
        if is_supporting(bricks[j], bricks[i]):
            mp[j].append(i)
            indegrees[i] += 1

# print(f"Elapsed time: {time.time() - start_time} seconds")

p1, p2 = 0, 0
for i in range(len(bricks)):
    indegrees_cpy = defaultdict(int)
    for k, v in indegrees.items():
        indegrees_cpy[k] = v

    count = kahn(i, indegrees_cpy)
    if count == 0:
        p1 += 1
    p2 += count

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f"Elapsed time: {time.time() - start_time} seconds")