from heapq import heapify, heappop, heappush
import time

# Start the timer
start_time = time.time()

def dijkstra(min_blocks: int, max_blocks: int) -> int:
    shortest = [[1e9 for _ in range(sz_c)] for _ in range(sz_r)]
    visited = set()

    # Each tuple's info follow this order: Cost, Continous length of the current direction, current row, current column, direction
    # This helps the heap sort by cost, as the heap scans from left to right
    pq = [(0, 0, 0, 0, 'd'), (0, 0, 0, 0, 'r')]
    heapify(pq)
    while pq:
        cost, cont_length, r, c, direction = heappop(pq)
        shortest[r][c] = min(shortest[r][c], cost)

        if (r, c, cont_length, direction) in visited:
            continue
        visited.add((r, c, cont_length, direction))

        # For the case of keep the same direction
        move_r, move_c = next_moves[direction]
        next_r, next_c = r + move_r, c + move_c

        if 0 <= next_r < sz_r and 0 <= next_c < sz_c and cont_length < max_blocks:
            heappush(pq, (cost + input[next_r][next_c], cont_length + 1, next_r, next_c, direction))
        
        # For the case of left and right turn from original direction
        for turn in future_turns[direction]:
            move_r, move_c = next_moves[turn]
            next_r, next_c = r + move_r, c + move_c

            if 0 <= next_r < sz_r and 0 <= next_c < sz_c and cont_length >= min_blocks:
                heappush(pq, (cost + input[next_r][next_c], 1, next_r, next_c, turn))

    return shortest[-1][-1]

input = [[int(val) for val in list(line.strip())] for line in open("input").readlines()]
sz_r, sz_c = len(input), len(input[0])

# Directions that are considered left and right, from the current direction
future_turns = {'d': 'rl', 'u':'lr', 'l':'ud', 'r': 'du'}

# Next location, based on direction
next_moves = {'d': (1, 0), 'u': (-1, 0), 'l': (0, -1), 'r': (0, 1)}

print(f'Part 1: {dijkstra(0, 3)}')
print(f'Part 2: {dijkstra(4, 10)}')
print(f'Elapsed time: {time.time() - start_time} seconds')