import time

# Start the timer
start_time = time.time()

input = [line.strip() for line in open("input").readlines()]
curr_r, curr_c = 0, 0

# Next location, based on direction
next_moves = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
visited = set([(0, 0)])

min_col, min_row, max_col, max_row = 0, 0, 0, 0

for line in input:
    direction, length, hex_code = line.split()
    length = int(length)

    for i in range(length):
        curr_r += next_moves[direction][0]
        curr_c += next_moves[direction][1]
        visited.add((curr_r, curr_c))

        min_col = min(min_col, curr_c)
        max_col = max(max_col, curr_c)
        min_row = min(min_row, curr_r)
        max_row = max(max_row, curr_r)

sz_r, sz_c = max_row - min_row + 1, max_col - min_col + 1
mp = [['.' for _ in range(sz_c)] for _ in range(sz_r)]

visited = set([(r - min_row, c - min_col) for r, c in visited])

def dfs(r, c):
    st = []
    st.append((r, c))
    valid_area = True
    res = 0
    
    while len(st) > 0:
        curr_r, curr_c = st.pop()
        
        if curr_r in [0, sz_r - 1] or curr_c in [0, sz_c - 1]:
            valid_area = False
        # Only take the ones that are int, not float coordinates
        if not (curr_r, curr_c) in visited:
            res += 1
        
        visited.add((curr_r, curr_c))
        
        for loc_r, loc_c in next_moves.values():
            new_r, new_c = curr_r + loc_r, curr_c + loc_c
            
            if (new_r, new_c) in visited or new_r < 0 or new_r >= sz_r or new_c < 0 or new_c >= sz_c:
                continue
            
            st.append((new_r, new_c))

    return res if valid_area else 0

res = len(visited)
for r in range(sz_r):
    for c in range(sz_c):
        res += dfs(r, c) if(r, c) not in visited else 0

print(f'Part 1: {res}')
print(f'Elapsed time: {time.time() - start_time} seconds')