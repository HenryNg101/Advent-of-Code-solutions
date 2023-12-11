import numpy as np

input = [list(line.strip()) for line in open("input").readlines()]
visited = set()
queue = []
row_sz, col_sz = len(input), len(input[0])

pipes_directions = {
    '|': [(1,0), (-1,0)], '-': [(0,1), (0,-1)], 'L': [(0, 1), (-1,0)], 'S': [],
    'J': [(0, -1), (-1,0)], '7': [(0, -1), (1,0)],'F': [(0,1), (1, 0)], '.': []
}
adjacent_locs = [(0,1), (0,-1), (1,0), (-1,0)]

#Find out and reassign the starting 'S' position
for r in range(row_sz):
    for c in range(col_sz):
        if input[r][c] == 'S':
            start_pipe_directions = []
            
            for loc_r, loc_c in adjacent_locs:
                new_r, new_c = r + loc_r, c + loc_c
                
                if new_r < 0 or new_r >= row_sz or new_c < 0 or new_c >= col_sz:
                    continue
            
                for move_r, move_c in pipes_directions[input[new_r][new_c]]:
                    if new_r + move_r == r and new_c + move_c == c:
                        start_pipe_directions.append((loc_r, loc_c))
                        break
            
            for pipe_type, pipe_directions in pipes_directions.items():
                if pipe_directions == start_pipe_directions:
                    input[r][c] = pipe_type
                    break
            
            queue.append((r, c))
            break


# BFS to find out the furthest distance for part 1
res_a = -1
while queue:
    sz = len(queue)
    for _ in range(sz):
        curr_r, curr_c = queue.pop(0)
        visited.add((curr_r, curr_c))
        
        for loc_r, loc_c in pipes_directions[input[curr_r][curr_c]]:
            new_r, new_c = curr_r + loc_r, curr_c + loc_c
            if (new_r, new_c) not in visited:
                queue.append((new_r, new_c))
            
    res_a += 1

print(f'Part 1: {res_a}')


# DFS from one unvisited node, used for part 2 algorithm
def dfs(r, c):
    st = []
    st.append((r, c))
    valid_area = True
    res = 0
    
    while len(st) > 0:
        curr_r, curr_c = st.pop()
        
        if curr_r in [0, row_sz - 1] or curr_c in [0, col_sz - 1]:
            valid_area = False
        # Only take the ones that are int, not float coordinates
        if int(curr_r) == curr_r and int(curr_c) == curr_c and not (curr_r, curr_c) in visited:
            res += 1
        
        visited.add((curr_r, curr_c))
        
        for loc_r, loc_c in adjacent_locs:
            new_r, new_c = curr_r + loc_r, curr_c + loc_c
            
            if (new_r, new_c) in visited or new_r < 0 or new_r >= row_sz or new_c < 0 or new_c >= col_sz:
                continue
            
            st.append((new_r, new_c))

    return res if valid_area else 0

# Updated value for part 2, by half the values of coordinates, to consider little gaps
# We now consider that, coordinates of little gaps in between are .5
pipes_directions = {
    key: [(r / 2, c / 2) for r, c in value] for key, value in pipes_directions.items()
}
adjacent_locs = [(r / 2, c / 2) for r, c in adjacent_locs]

# Expand to fill little gaps, using direction of the pipes in the main loop
expanded_st = set()
for r, c in visited:
    for move_r, move_c in pipes_directions[input[r][c]]:
        expanded_st.add((r + move_r, c + move_c))

visited |= expanded_st

res_b = 0
for r in np.arange(0, row_sz, 0.5):
    for c in np.arange(0, col_sz, 0.5):
        res_b += dfs(r, c) if (r, c) not in visited else 0

print(f'Part 2: {res_b}')
