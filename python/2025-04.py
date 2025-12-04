from inputGetter import get_input
from collections import deque

content = get_input(2025, 4).split('\n')

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
sz_r, sz_c = len(content), len(content[0])

mp = dict()
q = deque()
visited = set()
for r in range(0, sz_r):
    for c in range(0, sz_c):
        if content[r][c] == '@':
            mp[(r, c)] = set()
            
            for add_r, add_c in directions:
                new_r, new_c = r + add_r, c + add_c
                if 0 <= new_r < sz_r and 0 <= new_c < sz_c and content[new_r][new_c] == '@':
                    mp[(r, c)].add((new_r, new_c))
                        
            if len(mp[(r, c)]) < 4:
                q.append((r, c))
                visited.add((r, c))

print(f"Part A: {len(q)}")

# BFS
res_b = 0
while len(q) > 0:
    sz = len(q)
    res_b += sz
    for _ in range(sz):
        r, c = q.popleft()
        
        for (new_r, new_c) in mp[(r, c)]:
            mp[(new_r, new_c)].remove((r, c))
            if len(mp[(new_r, new_c)]) < 4 and (new_r, new_c) not in visited:
                q.append((new_r, new_c))
                visited.add((new_r, new_c))

print(f"Part B: {res_b}")