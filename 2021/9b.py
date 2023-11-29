from typing import List

#Do  bfs
def bfs(mp: List[str], row: int, col: int) -> int:
    r_sz, c_sz = len(mp), len(mp[0])
    visited = [[False for _ in range(c_sz)] for _ in range(r_sz)]
    stack = []
    
    stack.append((row, col))
    visited[row][col] = True

    res = 0

    while len(stack) > 0:
        r, c = stack.pop()
        res += 1

        if r > 0:
            if mp[r-1][c] != 9 and mp[r-1][c] > mp[r][c] and not visited[r-1][c]:
                stack.append((r-1, c))
                visited[r-1][c] = True

        if r < r_sz - 1:
            if mp[r+1][c] != 9 and mp[r+1][c] > mp[r][c] and not visited[r+1][c]:
                stack.append((r+1, c))
                visited[r+1][c] = True
        
        if c > 0:
            if mp[r][c-1] != 9 and mp[r][c-1] > mp[r][c] and not visited[r][c-1]:
                stack.append((r, c-1))
                visited[r][c-1] = True
        
        if c < c_sz - 1:
            if mp[r][c+1] != 9 and mp[r][c+1] > mp[r][c] and not visited[r][c+1]:
                stack.append((r, c+1))
                visited[r][c+1] = True

    return res

file_content = open("input").read()
heightmap = file_content.split("\n")    # Convert it to a heightmap data

r_sz, c_sz = len(heightmap), len(heightmap[0])
basins = [0, 0, 0]   #The final result

for r in range(r_sz):
    heightmap[r] = [int(i) for i in list(heightmap[r])]

for r in range(r_sz):
    for c in range(c_sz):
        check = True

        if r > 0:
            check &= heightmap[r-1][c] > heightmap[r][c]
        if r < r_sz - 1:
            check &= heightmap[r+1][c] > heightmap[r][c]
        if c > 0:
            check &= heightmap[r][c-1] > heightmap[r][c]
        if c < c_sz - 1:
            check &= heightmap[r][c+1] > heightmap[r][c]
        
        if check:
            basin = bfs(heightmap, r, c)
            if basin > basins[0]:
                basins[2] = basins[1]
                basins[1] = basins[0]
                basins[0] = basin

print(basins[0] * basins[1] * basins[2])