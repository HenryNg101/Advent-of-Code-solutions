import time

def print_map(mp):
    for line in mp:
        for char in line:
            print(char, end='')
        print()

start_time = time.process_time()
content = open("input").read()[:-1]     #Exclude the newline

#Some constants
rocks = [
    ['####'],
    ['.#.', '###', '.#.'],
    ['..#', '..#', '###'],
    ['#', '#', '#', '#'],
    ['##', '##']
]
width = 7

rocks_counter = 0
content_id = 0
highest_level = 0
mp = []

while rocks_counter < 2023:
    rock_id = rocks_counter % len(rocks)
    curr_rock = rocks[rock_id]
    left = 2
    right = left + len(curr_rock[0]) - 1
    bottom = len(curr_rock) - 1
    print(highest_level)
    print(f'{left} {right} {bottom}')

    while len(mp) > highest_level + 3 + len(curr_rock):
        mp.pop(0)

    while len(mp) < highest_level + 3 + len(curr_rock):
        mp.insert(0, ['.'] * width)

    #Special case of the '+' rock
    if rock_id == 1:
        while True:
            #Move left right in here
            if content[content_id] == '<':
                if left - 1 >= 0:
                    if mp[bottom][left] != '#' and mp[bottom-1][left-1] != '#':
                        left, right = left - 1, right - 1
            else:
                if left + 1 < width:
                    if mp[bottom][left] != '#' and mp[bottom-1][left + 1] != '#':
                        left, right = left + 1, right + 1
            
            content_id += 1
            if content_id >= len(content):
                content_id = 0

            #Then, check if bottom is filled with rock, or the ground
            if bottom + 1 >= len(mp):
                break
            elif mp[bottom + 1][left+1] == '#' or mp[bottom][left] == '#' or mp[bottom][right] == '#':
                break

            bottom += 1
            print(f'{left} {right} {bottom}')
    else:
        while True:
            #print(f'{left} {right} {bottom}')
            #Move left right in here
            if content[content_id] == '<':
                if left - 1 >= 0:
                    #print(left)
                    if mp[bottom][left - 1] != '#':
                        left, right = left - 1, right - 1
            else:
                if right + 1 < width:
                    if mp[bottom][right + 1] != '#':
                        left, right = left + 1, right + 1
            
            content_id += 1
            if content_id >= len(content):
                content_id = 0

            #Then, check if bottom is filled with rock, or the ground
            if bottom + 1 >= len(mp):
                break
            #Need to re-do this check
            else:
                check = False
                for i in range(left, right+1):
                    if mp[bottom + 1][i] == '#':
                        check = True
                        break
                if check: 
                    break

            bottom += 1
            print(f'{left} {right} {bottom}')

    for i in range(len(curr_rock)):
        for j in range(len(curr_rock[i])):
            r_pos = bottom - len(curr_rock) + i + 1
            c_pos = left + j
            if curr_rock[i][j] == '#':
                mp[r_pos][c_pos] = '#'

    print()
    print(f'{left} {right} {bottom}')
    print_map(mp)
    print()
    rocks_counter += 1

    id = 0
    while True:
        if '#' not in mp[len(mp) - id - 1]:
            break
        id += 1
    highest_level = id


print(highest_level)
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")

'''
Example input: >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
'''