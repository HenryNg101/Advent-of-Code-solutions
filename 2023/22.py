import sys
from copy import deepcopy
import time

# Start the timer
start_time = time.time()

# Simulate bricks falling until stop, return the amount of fallen bricks during the process
def bricks_falling_simulation(cubes_positions, bricks):
    fallen_bricks_ids = set()
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
                fallen_bricks_ids.add(i)

                for (x, y, z) in brick:
                    cubes_positions.discard((x, y, z))
                    cubes_positions.add((x, y, z - 1))

                bricks[i] = [(x, y, z - 1) for (x, y, z) in brick]
                
        if not continue_simulation:
            break

    return len(fallen_bricks_ids)


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

bricks_falling_simulation(cubes_positions, bricks)  # Let initial bricks fall first

# Just remove brick, one by one, then count
p1, p2 = 0, 0
for i, brick in enumerate(bricks):
    cubes_positions_copy = deepcopy(cubes_positions)
    bricks_copy = [brick for j, brick in enumerate(bricks) if j != i]
    for (x, y, z) in brick:
        cubes_positions_copy.discard((x, y, z))

    # Another falling simulation
    fallen_bricks_cnt = bricks_falling_simulation(cubes_positions_copy, bricks_copy)
    if fallen_bricks_cnt == 0:
        p1 += 1
    p2 += fallen_bricks_cnt

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f"Elapsed time: {time.time() - start_time} seconds")