def print_grids(grids):
    for line in grids:
        for char in line:
            print(char, end='')
        print()

def traverse(mp: set, max_r: int):
    global grids

    curr_r, curr_c = 0, 500
    #Move this one down first
    while curr_r < max_r:
        if (curr_r + 1, curr_c) not in mp:
            curr_r += 1
        elif (curr_r + 1, curr_c - 1) not in mp:
            curr_r, curr_c = curr_r + 1, curr_c - 1
        elif (curr_r + 1, curr_c + 1) not in mp:
            curr_r, curr_c = curr_r + 1, curr_c + 1
        else:
            break
    if curr_r >= max_r:
        return 0
    mp.add((curr_r, curr_c))
    grids[curr_r][curr_c] = 'o'
    #print_grids(grids)

    count = 1
    while True:
        next_r, next_c = curr_r - 1, curr_c
        while next_r < max_r:
            if (next_r + 1, next_c) not in mp:
                next_r += 1
            elif (next_r + 1, next_c - 1) not in mp:
                next_r, next_c = next_r + 1, next_c - 1
            elif (next_r + 1, next_c + 1) not in mp:
                next_r, next_c = next_r + 1, next_c + 1
            else:
                break

        if next_r >= max_r:
            return count

        count += 1
        mp.add((next_r, next_c))
        grids[next_r][next_c] = 'o'
        curr_r = min(curr_r, next_r)

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

grids = [['.' for _ in range(540)] for _ in range(200)]
for i in mp:
    grids[i[0]][i[1]] = '#'
print(traverse(mp, max_r))
#print_grids(grids)
