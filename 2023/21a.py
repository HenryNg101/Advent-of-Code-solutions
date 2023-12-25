import time

# Start the timer
start_time = time.time()

input = [list(line.strip()) for line in open("input").readlines()]

sz_r, sz_c = len(input), len(input[0])
queue = []
next_moves = [(1, 0),(-1, 0),(0, -1),(0, 1)]
# visited = set()

for r in range(sz_r):
    for c in range(sz_c):
        if input[r][c] == 'S':
            queue.append((r, c))
            break

iteration = 0
while queue:
    sz = len(queue)
    if iteration == 10:
        print(f'Part 1: {sz}')
        break

    visited = set()
    for _ in range(sz):
        r, c = queue.pop(0)

        for move_r, move_c in next_moves:
            new_r, new_c = r + move_r, c + move_c
            if (new_r, new_c) not in visited and new_r >= 0 and new_r < sz_r and new_c >= 0 and new_c < sz_c and input[new_r][new_c] != '#':
                queue.append((new_r, new_c))
                visited.add((new_r, new_c))

    iteration += 1

print(f'Elapsed time: {time.time() - start_time} seconds')