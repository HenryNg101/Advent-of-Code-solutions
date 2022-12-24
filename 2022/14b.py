import time

start_time = time.process_time()

def traverse(mp: set, max_r: int):
    curr_r, curr_c = 0, 500
    count = 0

    #Move this one down first
    while curr_r < max_r - 1:
        if (curr_r + 1, curr_c) not in mp:
            curr_r += 1
        elif (curr_r + 1, curr_c - 1) not in mp:
            curr_r, curr_c = curr_r + 1, curr_c - 1
        elif (curr_r + 1, curr_c + 1) not in mp:
            curr_r, curr_c = curr_r + 1, curr_c + 1
        else:
            break
    count += 1
    mp.add((curr_r, curr_c))
    if (curr_r, curr_c) == (0, 500):
            return count

    while True:
        next_r, next_c = curr_r - 1, curr_c
        while next_r < max_r - 1:
            if (next_r + 1, next_c) not in mp:
                next_r += 1
            elif (next_r + 1, next_c - 1) not in mp:
                next_r, next_c = next_r + 1, next_c - 1
            elif (next_r + 1, next_c + 1) not in mp:
                next_r, next_c = next_r + 1, next_c + 1
            else:
                break

        count += 1
        mp.add((next_r, next_c))
        curr_r = min(curr_r, next_r)

        if (next_r, next_c) == (0, 500):
            return count

content = open("input").read().split('\n')
content.pop()

mp = set()
max_r = 0

for line in content:
    line = [[int(k) for k in pair.split(',')] for pair in line.split(' -> ')]
    col, row = line[0]
    for i in range(1, len(line)):
        while col != line[i][0] or row != line[i][1]:
            mp.add((row, col))
            if col == line[i][0]:
                if row < line[i][1]:
                    row += 1
                else:
                    row -= 1
            else:
                if col < line[i][0]:
                    col += 1
                else:
                    col -= 1
        mp.add((row, col))
        max_r = max(max_r, row)

max_r += 2      #The actual ground
print(traverse(mp, max_r))
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")