from collections import defaultdict
from copy import deepcopy
import time

# Start the timer
start_time = time.time()

# Check if first brick (brick1) supports second brick or not (brick2)
# Basically, for one brick to support another, it must have highest z = lowest z of the other - 1
# And, a way to have at least one mutual x and y (Basically interval problem)
def is_supporting(brick1, brick2):
    (sx1, sy1, sz1), (ex1, ey1, ez1) = brick1
    (sx2, sy2, sz2), (ex2, ey2, ez2) = brick2
    return ez1 + 1 == sz2 and (ey1 >= sy2 and ey2 >= sy1) and (ex1 >= sx2 and ex2 >= sx1)

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

supporting_bricks = defaultdict(list)   # Store list of bricks that a brick supports
supported_indegrees = defaultdict(int)    # Store indegree, or basically, how many bricks support a specific brick
bricks = [(brick[0], brick[-1]) for brick in bricks]    # Get updated start and end point for bricks after falling

for i in range(len(bricks)):
    for j in range(i+1, len(bricks)):
        if is_supporting(bricks[i], bricks[j]):
            supporting_bricks[i].append(j)
            supported_indegrees[j] += 1
        if is_supporting(bricks[j], bricks[i]):
            supporting_bricks[j].append(i)
            supported_indegrees[i] += 1

p1, p2 = 0, 0
for i in range(len(bricks)):
    indegrees_cpy = deepcopy(supported_indegrees)

    # Use Kahn algorithm, to count the number of subsequent bricks would fall if one brick is gone
    st = [i]
    fallen_bricks_cnt = -1
    while st:
        curr = st.pop()
        fallen_bricks_cnt += 1

        for next in supporting_bricks[curr]:
            indegrees_cpy[next] -= 1
            if indegrees_cpy[next] == 0:
                st.append(next)

    p1 += fallen_bricks_cnt == 0
    p2 += fallen_bricks_cnt

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f"Elapsed time: {time.time() - start_time} seconds")