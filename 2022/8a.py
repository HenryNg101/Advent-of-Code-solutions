import time

start_time = time.process_time()
# Template
content = open("input").read().split('\n')
content.pop()
content = [[int(ch) for ch in line] for line in content]

# Fill some values
check_ls = [[False for _ in line] for line in content]
for i in range(len(check_ls)):
    check_ls[i][0], check_ls[i][-1] = True, True

for i in range(len(check_ls[0])):
    check_ls[0][i], check_ls[-1][i] = True, True

# Check left
for r in range(1, len(content)-1):
    min_left = content[r][0]
    for c in range(1, len(content[0])-1):
        if content[r][c] > min_left:
            min_left = content[r][c]
            check_ls[r][c] = True

# Check right
for r in range(1, len(content)-1):
    min_right = content[r][-1]
    for c in range(len(content[0])-1, 0, -1):
        if content[r][c] > min_right:
            min_right = content[r][c]
            check_ls[r][c] = True

# Check up
for c in range(1, len(content[0])-1):
    min_up = content[0][c]
    for r in range(1, len(content)-1):
        if content[r][c] > min_up:
            min_up = content[r][c]
            check_ls[r][c] = True

# Check down
for c in range(1, len(content[0])-1):
    min_down = content[-1][c]
    for r in range(len(content)-1, 0, -1):
        if content[r][c] > min_down:
            min_down = content[r][c]
            check_ls[r][c] = True

counter = 0
for r in check_ls:
    for val in r:
        if val:
            counter += 1
print(counter)
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")