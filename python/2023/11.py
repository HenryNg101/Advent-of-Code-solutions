import time

# Start the timer
start_time = time.time()
input = [line.strip() for line in open("input").readlines()]
r_sz, c_sz = len(input), len(input[0])

# All galaxy locations
galaxies = [[r, c] for r in range(r_sz) for c in range(c_sz) if input[r][c] == '#']

# Get rows and columns that has no galaxy
galaxies_cnt_rows = [sum(1 for c in range(c_sz) if input[r][c] == '#') for r in range(r_sz)]
galaxies_cnt_cols = [sum(1 for r in range(r_sz) if input[r][c] == '#') for c in range(c_sz)]
cnt_rows = [r for r, count in enumerate(galaxies_cnt_rows) if count == 0]
cnt_cols = [c for c, count in enumerate(galaxies_cnt_cols) if count == 0]

def distance_after_expand(galaxies, new_size_rate: int):
    # Expand the map
    for i in range(len(galaxies)):
        add_r, add_c = 0, 0

        # When a column/row has n times the size, there are n-1 columns/rows added
        for r in cnt_rows:
            add_r += (new_size_rate - 1) if galaxies[i][0] > r else 0
        for c in cnt_cols:
            add_c += (new_size_rate - 1) if galaxies[i][1] > c else 0

        galaxies[i][0] += add_r
        galaxies[i][1] += add_c

    # Calculate sum of distances between all pairs
    res = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            res += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    return res

print(f'Part 1: {distance_after_expand([galaxy[:] for galaxy in galaxies], 2)}')
print(f'Part 2: {distance_after_expand(galaxies, 1000000)}')
print(f'Elapsed time: {time.time() - start_time} seconds')