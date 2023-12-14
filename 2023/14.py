def move_north() -> None:
    for r in range(sz_r):
        for c in range(sz_c):
            if input[r][c] == 'O':
                r_cpy = r-1
                
                while r_cpy >= 0 and input[r_cpy][c] == '.':
                    r_cpy -= 1
                input[r][c] = '.'
                input[r_cpy+1][c] = 'O'

def move_south() -> None:
    for r in range(sz_r-1, -1, -1):
        for c in range(sz_c):
            if input[r][c] == 'O':
                r_cpy = r+1
                
                while r_cpy < sz_r and input[r_cpy][c] == '.':
                    r_cpy += 1
                input[r][c] = '.'
                input[r_cpy-1][c] = 'O'

def move_east() -> None:
    for r in range(0, sz_r, 1):
        for c in range(sz_c-1, -1, -1):
            if input[r][c] == 'O':
                c_cpy = c+1
                
                while c_cpy < sz_c and input[r][c_cpy] == '.':
                    c_cpy += 1
                input[r][c] = '.'
                input[r][c_cpy-1] = 'O'

def move_west() -> None:
    for r in range(0, sz_r, 1):
        for c in range(0, sz_c, 1):
            if input[r][c] == 'O':
                c_cpy = c-1
                
                while c_cpy >= 0 and input[r][c_cpy] == '.':
                    c_cpy -= 1
                input[r][c] = '.'
                input[r][c_cpy+1] = 'O'

# Calculate the load for support beams of the current input map
def calculate_load():
    return sum([sz_r - r for r in range(sz_r) for c in range(sz_c) if input[r][c] == "O"])

input = [list(line.strip()) for line in open("input").readlines()]
sz_r, sz_c = len(input), len(input[0])
cache = dict()
cycles_count = 1000000000

for iteration in range(cycles_count):
    # Run the cycle
    move_north()
    if iteration == 0:
        print(f'Part 1: {calculate_load()}')
    move_west()
    move_south()
    move_east()

    key = str(input)    # Convert the result list to a hashable value

    # Cut off in here, when a loop is detected, and start doing calculations
    if key in cache:
        pairs, loop_start_id = list(cache.items()), 0
        while loop_start_id < len(pairs) and pairs[loop_start_id][0] != key:
            loop_start_id += 1

        pairs = pairs[loop_start_id:]
        print(f'Part 2: {pairs[(cycles_count - loop_start_id - 1) % len(pairs)][1]}')
        break

    cache[key] = calculate_load()