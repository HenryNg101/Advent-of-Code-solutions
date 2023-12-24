import time

# Start the timer
start_time = time.time()

'''
Main observations from this problem:
- Finding longest path in an undirected graph is a NP-hard problem => Can't just use normal BFS
- The longest path to the normal nodes that's only on one path (has less than 2 neighbor nodes, 
except starting and end node) is constant => Can ignore these nodes
- So, the problem can comes down to: Finding longest distance between the nodes that are not normal 
(has more than 2 neighbors, plus the start and end nodes)
'''

input = [list(line.strip()) for line in open("input").readlines()]
sz_r, sz_c = len(input), len(input[0])
directions = [(1,0), (-1,0), (0,1), (0,-1)]

# Adding these special nodes in
node_cnt = 0
special_nodes = set([(0, 1), (sz_r-1, sz_c-2)])
for r in range(sz_r):
    for c in range(sz_c):
        if input[r][c] != '#':
            node_cnt += 1
            neighbor_cnt = 0

            for add_r, add_c in directions:
                new_r, new_c = r + add_r, c + add_c
                if 0 <= new_r < sz_r and 0 <= new_c < sz_c and input[new_r][new_c] != '#':
                    neighbor_cnt += 1

            if neighbor_cnt > 2:
                special_nodes.add((r, c))

'''
- A comparision that shows that, the problem is optimized way better with this, 
from backtrack on almost 10k nodes, to less than 100 nodes. 
- This is necessary, considering that, complexity of backtracking is O(n!)
- Still, it's O(n!), so it's still very lengthy process
'''
print(f"Number of valid nodes for travelling: {node_cnt}")
print(f"Number of special nodes, after filtering: {len(special_nodes)}")

# Find distances from a special node to the closest special nodes, through DFS
# Why must be closest special nodes ? Because, 
node_distances = dict()
for r, c in special_nodes:
    node_distances[(r, c)] = []
    node_visited = set()
    st = [(r, c, 0)]
    while st:
        curr_r, curr_c, dis = st.pop()
        node_visited.add((curr_r, curr_c))

        if (curr_r, curr_c) in special_nodes and (curr_r, curr_c) != (r, c):
            node_distances[(r, c)].append((curr_r, curr_c, dis))
            continue

        for add_r, add_c in directions:
            new_r, new_c = curr_r + add_r, curr_c + add_c
            if (new_r, new_c) not in node_visited and 0 <= new_r < sz_r and 0 <= new_c < sz_c and input[new_r][new_c] != '#':
                st.append((new_r, new_c, dis+1))

# Backtrack on these special points
def dfs(r, c, dis):
    global res
    if (r, c) == (sz_r-1, sz_c-2):
        res = max(res, dis)

    visited.add((r, c))
    for new_r, new_c, new_dis in node_distances[(r, c)]:
        if (new_r, new_c) not in visited:
            dfs(new_r, new_c, dis + new_dis)
    visited.discard((r, c))

res = 0
visited = set()
dfs(0, 1, 0)
print(f"Part 2: {res}")
print(f'Elapsed time: {time.time() - start_time} seconds')