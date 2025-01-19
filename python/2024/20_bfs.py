import time
from collections import defaultdict, deque
import math
from functools import lru_cache
import sys
from queue import Queue
sys.setrecursionlimit(100000000)

start_time = time.time()
content = open('input.txt', 'r').read()
content = [list(line) for line in content.split('\n')]
sz_r, sz_c = len(content), len(content[0])

end_r, end_c = -1, -1
for r in range(sz_r):
    for c in range(sz_c):
        if content[r][c] == 'S':
            end_r, end_c = r, c
            break

def bfs(r, c, depth):
    q = Queue()
    q.put((r, c))
    visited = set()
    visited.add((r, c))
    result = 0

    for distance in range(0, depth + 1):
        q_sz = q.qsize()
        for _ in range(q_sz):
            curr_r, curr_c = q.get()
            if isinstance(content[curr_r][curr_c], int) and abs(content[curr_r][curr_c] - content[r][c]) - distance >= 100:
                result += 1
        
            for add_r, add_c in directions:
                new_r, new_c = curr_r + add_r, curr_c + add_c
                if 0 <= new_r < sz_r and 0 <= new_c < sz_c and (new_r, new_c) not in visited:
                    q.put((new_r, new_c))
                    visited.add((new_r, new_c))
    return result

res_a, res_b, dis = 0, 0, 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while True:    
    is_ending = content[end_r][end_c] == 'E'
    
    content[end_r][end_c] = dis
    res_a += bfs(end_r, end_c, 2)
    res_b += bfs(end_r, end_c, 20)
    
    if is_ending:
        break
    
    # Get new one
    for dir_r, dir_c in directions:
        new_r, new_c = end_r + dir_r, end_c + dir_c
        if 0 <= new_r < sz_r and 0 <= new_c < sz_c and (content[new_r][new_c] == '.' or content[new_r][new_c] == 'E'):
            end_r, end_c = new_r, new_c
            break
    dis += 1

print(f'Part A: {res_a}')
print(f'Part B: {res_b}')
print(f'Elapsed time: {time.time() - start_time} seconds')