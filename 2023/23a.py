import time

# Start the timer
start_time = time.time()

'''
One interesting observation that I found in the first part was that, actually, there's no cycle in the graph,
as the graph is directed in the arrow nodes, so, you can just BFS and call it the day :) The approach in second 
part would work for this too, with a bit of modification for arrows, but that's just overkill.
'''

input = [list(line.strip()) for line in open("input").readlines()]
sz_r, sz_c = len(input), len(input[0])
directions_mp = {
    '.': [(1,0), (-1,0), (0,1), (0,-1)], 'v': [(1, 0)], 
    '^': [(-1, 0)], '<': [(0, -1)], '>': [(0, 1)]
}

res = 0
queue = [(0, 1, None, None)]
depth = 0
while queue:
    sz = len(queue)
    for _ in range(sz):
        # The only BFS trick here is to watch out the previous node before this node, and u should be able to avoid cycle
        # Marking the visited nodes in map would only work with shortest path
        curr_r, curr_c, prev_r, prev_c = queue.pop(0)
        if (curr_r, curr_c) == (sz_r-1, sz_c-2):
            res = max(res, depth)

        for add_r, add_c in directions_mp[input[curr_r][curr_c]]:
            new_r, new_c = curr_r + add_r, curr_c + add_c
            if (new_r, new_c) != (prev_r, prev_c) and 0 <= new_r < sz_r and 0 <= new_c < sz_c and input[new_r][new_c] != '#':
                queue.append((new_r, new_c, curr_r, curr_c))
    depth += 1

print(f"Part 1: {res}")
print(f'Elapsed time: {time.time() - start_time} seconds')