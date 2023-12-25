import time

# Start the timer
start_time = time.time()

input = [line.strip() for line in open("input").readlines()]
curr_r, curr_c = 0, 0
next_moves = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)} # Next location, based on direction
directions = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}   # Matching directions

points = []
bounded_area = 0    # The area of the outer lines too (This is not covered by shoelace's formula)

for line in input:
    _, _, hex_code = line.split()
    length = int(hex_code[2:-2], 16)
    direction = directions[hex_code[-2:-1]]

    curr_r += next_moves[direction][0] * length
    curr_c += next_moves[direction][1] * length

    bounded_area += length
    points.append((curr_r, curr_c))

# Shoelace's formula + add the cover, which is the side length, that's only halfly covered in the formula
res = 0
for i in range(0, len(points)-1):
    res += points[i][1] * points[i+1][0] - points[i+1][1] * points[i][0]

print(f"Part 2: {res // 2 + bounded_area // 2 + 1}")
print(f'Elapsed time: {time.time() - start_time} seconds')