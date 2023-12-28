import time, z3

# Start the timer
start_time = time.time()

input = [line.strip() for line in open("input").readlines()]

lines_infos = []
positions = []
velocities = []
for line in input:
    pos, vel = [[int(val) for val in coordinate.split(', ')] for coordinate in line.split(' @ ')]
    
    # Get a, b in y = ax + b
    pos_x, pos_y, pos_z = pos
    vel_x, vel_y, vel_z = vel

    slope = vel_y / vel_x # Value a
    intercept = pos_y - slope * pos_x   # Value b

    positions.append(pos)
    velocities.append(vel)
    lines_infos.append((slope, intercept))

res = 0
min_coordinate, max_coordinate = 200000000000000, 400000000000000
for i in range(len(input)):
    for j in range(i+1, len(input)):
        first_slope, first_intercept = lines_infos[i]
        second_slope, second_intercept = lines_infos[j]

        # Case of 2 parallel lines
        if first_slope == second_slope:
            continue
        crossed_x = (second_intercept - first_intercept) / (first_slope - second_slope)
        crossed_y = first_slope * crossed_x + first_intercept

        # Check if cross past (The line only starts from one direction), by checking if these values are not same signs
        if (crossed_x - positions[i][0]) * velocities[i][0] <= 0:
            continue
        if (crossed_x - positions[j][0]) * velocities[j][0] <= 0:
            continue
        if (crossed_y - positions[i][1]) * velocities[i][1] <= 0:
            continue
        if (crossed_y - positions[j][1]) * velocities[j][1] <= 0:
            continue

        res += int((min_coordinate <= crossed_x <= max_coordinate) and (min_coordinate <= crossed_y <= max_coordinate))

print(f'Part 1: {res}')

# Part 2 algotihm
z3_solver = z3.Solver()

# Store result for starting point and velocity of the 3d line for part 2
pos_x, pos_y, pos_z = z3.Real('x'), z3.Real('y'), z3.Real('z')
vel_x, vel_y, vel_z = z3.Real('vel_x'), z3.Real('vel_y'), z3.Real('vel_z')

for i in range(len(positions)):
    col_t = z3.Real(f'T{i}')    # Collision time
    z3_solver.add(pos_x + col_t * vel_x - positions[i][0] - col_t * velocities[i][0] == 0)
    z3_solver.add(pos_y + col_t * vel_y - positions[i][1] - col_t * velocities[i][1] == 0)
    z3_solver.add(pos_z + col_t * vel_z - positions[i][2] - col_t * velocities[i][2] == 0)

if z3_solver.check() == z3.sat:
    sol_model = z3_solver.model()
    print(f'Part 2: {sol_model.eval(pos_x + pos_y + pos_z)}')
else:
    print(f'Part 2 has no solution!!!')

print(f'Elapsed time: {time.time() - start_time} seconds')