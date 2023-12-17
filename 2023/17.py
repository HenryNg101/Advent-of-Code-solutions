from heapq import heapify, heappop, heappush
import time

# Start the timer
start_time = time.time()

class Node:
    def __init__(self, r, c, cont_length, direction, cost: int):
        self.r = r
        self.c = c
        self.cont_length = cont_length
        self.direction = direction
        self.cost = cost

    def __lt__(self, other):
        if self.cost == other.cost:
            return self.cont_length < other.cont_length
        return self.cost < other.cost

input = [[int(val) for val in list(line.strip())] for line in open("input").readlines()]
sz_r, sz_c = len(input), len(input[0])

def dijkstra(min_blocks: int, max_blocks: int) -> int:
    shortest = [[1e9 for _ in range(sz_c)] for _ in range(sz_r)]
    visited = set()

    pq = [Node(0, 0, 1, 'd', 0), Node(0, 0, 0, 'r', 0)]
    heapify(pq)

    while pq:
        node = heappop(pq)
        r, c, cont_length, direction, cost = node.r, node.c, node.cont_length, node.direction, node.cost
        shortest[r][c] = min(shortest[r][c], cost)

        if (r, c, cont_length, direction) in visited:
            continue
        visited.add((r, c, cont_length, direction))

        if direction == 'd':
            # Go straight
            if r + 1 < sz_r and cont_length < max_blocks:
                heappush(pq, Node(r+1, c, cont_length+1, direction, cost + input[r+1][c]))

            if cont_length >= min_blocks:
                # Turn left
                if c < sz_c -1:
                    heappush(pq, Node(r, c+1, 1, 'r', cost + input[r][c+1]))

                # Turn right
                if c > 0:
                    heappush(pq, Node(r, c-1, 1, 'l', cost + input[r][c-1]))

        elif direction == 'u':
            # Go straight
            if r > 0 and cont_length < max_blocks:
                heappush(pq, Node(r-1, c, cont_length+1, direction, cost + input[r-1][c]))

            if cont_length >= min_blocks:
                # Turn left
                if c > 0:
                    heappush(pq, Node(r, c-1, 1, 'l', cost + input[r][c-1]))

                # Turn right
                if c < sz_c -1:
                    heappush(pq, Node(r, c+1, 1, 'r', cost + input[r][c+1]))

        elif direction == 'r':
            # Go straight
            if c + 1 < sz_c and cont_length < max_blocks:
                heappush(pq, Node(r, c+1, cont_length+1, direction, cost + input[r][c+1]))

            if cont_length >= min_blocks:
                # Turn left
                if r > 0:
                    heappush(pq, Node(r-1, c, 1, 'u', cost + input[r-1][c]))

                # Turn right
                if r < sz_r - 1:
                    heappush(pq, Node(r+1, c, 1, 'd', cost + input[r+1][c]))

        elif direction == 'l':
            # Go straight
            if c > 0 and cont_length < max_blocks:
                heappush(pq, Node(r, c-1, cont_length+1, direction, cost + input[r][c-1]))

            if cont_length >= min_blocks:
                # Turn right
                if r > 0:
                    heappush(pq, Node(r-1, c, 1, 'u', cost + input[r-1][c]))

                # Turn left
                if r < sz_r - 1:
                    heappush(pq, Node(r+1, c, 1, 'd', cost + input[r+1][c]))
    return shortest[-1][-1]

print(f'Part 1: {dijkstra(0, 3)}')
print(f'Part 2: {dijkstra(4, 10)}')
print(f'Elapsed time: {time.time() - start_time} seconds')