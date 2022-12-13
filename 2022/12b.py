from queue import Queue

def is_valid(curr_r, curr_c, new_r, new_c, visited, content):
    if new_r < 0 or new_r >= len(content) or new_c < 0 or new_c >= len(content[0]):
        return False
    if visited[new_r][new_c]:
        return False
    return ord(content[new_r][new_c]) - ord(content[curr_r][curr_c]) <= 1

def bfs(start_r, start_c, end_r, end_c, content):
    q = Queue()
    q.put((start_r, start_c))
    lv = 0
    visited = [[False for _ in range(len(content[0]))] for _ in range(len(content))]

    while not q.empty():
        sz = q.qsize()
        #print(sz)
        for _ in range(sz):
            curr_r, curr_c = q.get()
            visited[curr_r][curr_c] = True

            if (curr_r, curr_c) == (end_r, end_c):
                return lv

            for i in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                new_r, new_c = curr_r + i[0], curr_c + i[1]
                if is_valid(curr_r, curr_c, new_r, new_c, visited, content):
                    q.put((new_r, new_c))
                    visited[new_r][new_c] = True 
        lv += 1

    return -1

content = open("input").read().split('\n')
content.pop()
content = [list(i) for i in content]

start_r, start_c, end_r, end_c = -1, -1

for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'S':
            start_r, start_c = i, j
            content[i][j] = 'a'
        if content[i][j] == 'E':
            end_r, end_c = i, j
            content[i][j] = 'z'

#Part A
print(bfs(start_r, start_c, end_r, end_c, content))

#Part B
res = 9999999999999999
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'a':
            temp = bfs(i, j, end_r, end_c, content)
            if temp != -1:
                res = min(res, temp)

print(res)