import time

# Start the timer
start_time = time.time()

input = [line.strip() for line in open("input").readlines()]

arr = []
positions = []
velocities = []
for line in input:
    pos, vel = [[int(val) for val in coordinate.split(', ')] for coordinate in line.split(' @ ')]
    
    # Get a, b in y = ax + b
    pos_x, pos_y, _ = pos
    vel_x, vel_y, _ = vel

    slope = vel_y / vel_x # Value a
    intercept = pos_y - slope * pos_x   # Value b

    positions.append(pos)
    velocities.append(vel)
    arr.append((slope, intercept))

res = 0
min_coordinate, max_coordinate = 200000000000000, 400000000000000
for i in range(len(input)):
    for j in range(i+1, len(input)):
        first_slope, first_intercept = arr[i]
        second_slope, second_intercept = arr[j]

        # Case of 2 parallel lines
        if first_slope == second_slope:
            continue
        crossed_x = (second_intercept - first_intercept) / (first_slope - second_slope)
        crossed_y = first_slope * crossed_x + first_intercept

        # Check if cross past (The line only starts from one direction)
        if crossed_x > positions[i][0] and velocities[i][0] <= 0:
            continue
        if crossed_x < positions[i][0] and velocities[i][0] >= 0:
            continue
        if crossed_y > positions[i][1] and velocities[i][1] <= 0:
            continue
        if crossed_y < positions[i][1] and velocities[i][1] >= 0:
            continue
        if crossed_x > positions[j][0] and velocities[j][0] <= 0:
            continue
        if crossed_x < positions[j][0] and velocities[j][0] >= 0:
            continue
        if crossed_y > positions[j][1] and velocities[j][1] <= 0:
            continue
        if crossed_y < positions[j][1] and velocities[j][1] >= 0:
            continue

        res += int((min_coordinate <= crossed_x <= max_coordinate) and (min_coordinate <= crossed_y <= max_coordinate))

print(f'Part 1: {res}')
print(f'Elapsed time: {time.time() - start_time} seconds')