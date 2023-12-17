import time

# Start the timer
start_time = time.time()

def dfs(start):
    visited, visited_pos = set(), set()
    st = [start]
    while st:
        curr_r, curr_c, add_r, add_c = st.pop()
        if (curr_r, curr_c, add_r, add_c) in visited_pos or curr_r < 0 or curr_r >= sz_r or curr_c < 0 or curr_c >= sz_c:
            continue
        visited.add((curr_r, curr_c))
        visited_pos.add((curr_r, curr_c, add_r, add_c))

        # Cases when a light is splitted into two
        light_type = input[curr_r][curr_c]
        if (light_type == '|' and add_r == 0) or (light_type == '-' and add_c == 0):
            add_r, add_c = add_c, add_r

            # Add another light in, aside from the main one light
            another_r = 0 - add_r if light_type == '|' else add_r
            another_c = 0 - add_c if light_type == '-' else add_c
            st.append((curr_r + another_r, curr_c + another_c, another_r, another_c))

        else:
            if light_type == '\\':
                add_r, add_c = add_c, add_r
            if light_type == '/':
                add_r, add_c = 0 - add_c, 0 - add_r

        # Add the new light in
        st.append((curr_r + add_r, curr_c + add_c, add_r, add_c))
    
    return len(visited)


input = [line.strip() for line in open("input").readlines()]
sz_r, sz_c = len(input), len(input[0])
res_b = 0

for r in range(sz_r):
    for c in range(sz_c):
        #Left
        if c == 0:
            res_b = max(res_b, dfs((r, c, 0, -1)))
        #Right
        if c == sz_c-1:
            res_b = max(res_b, dfs((r, c, 0, 1)))
        #Up
        if r == sz_r - 1:
            res_b = max(res_b, dfs((r, c, -1, 0)))
        #Down
        if r == 0:
            res_b = max(res_b, dfs((r, c, 1, 0)))

print(f'Part 1: {dfs((0, 0, 0, 1))}')
print(f'Part 2: {res_b}')
print(f'Elapsed time: {time.time() - start_time} seconds')