# Only applicable for this part, not for next part
# Need to optimize later for next part
content = open("input").read().split('\n')
content.pop()

def print_ls(visited):
    for r in visited:
        for val in r:
            if val: print('#', end=' ')
            else: print('.', end=' ')
        print()

visited = [[False for _ in range(1000)] for _ in range(1000)]
row_H = 500
col_H = 500
row_T = 500
col_T = 500
count = 0

for line in content:
    direction, moves = line.split(' ')
    moves = int(moves)
    new_r, new_c = row_H, col_H

    for _ in range(moves):
        if direction == 'U':
            new_r -= 1
        elif direction == 'D':
            new_r += 1
        elif direction == 'L':
            new_c -= 1
        else:
            new_c += 1
    
        if abs(new_r - row_T) >= 2 or abs(new_c - col_T) >= 2:
            row_T, col_T = row_H, col_H

        if not visited[row_T][col_T]:
            count += 1
            visited[row_T][col_T] = True

        row_H, col_H = new_r, new_c
    #print_ls(visited)
    #print()

print(count)
#print_ls(visited)