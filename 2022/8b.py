import time

start_time = time.process_time()
# Template
content = open("input").read().split('\n')
content.pop()
content = [[int(ch) for ch in line] for line in content]

res = 0

for r in range(len(content)):
    for c in range(len(content[0])):
        left = 0
        for x in range(c-1, -1, -1):
            left += 1
            if content[r][x] >= content[r][c]: break
        
        right = 0
        for x in range(c+1, len(content[0])):
            right += 1
            if content[r][x] >= content[r][c]: break
        
        up = 0
        for x in range(r-1, -1, -1):
            up += 1
            if content[x][c] >= content[r][c]: break

        down = 0
        for x in range(r+1, len(content)):
            down += 1
            if content[x][c] >= content[r][c]: break
        res = max(res, up * down * left * right)

print(res)
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")