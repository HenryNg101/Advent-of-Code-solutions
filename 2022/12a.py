from queue import Queue

def is_valid(curr_r, curr_c, new_r, new_c):
    global visited, content
    if new_r < 0 or new_r >= len(content) or new_c < 0 or new_c >= len(content[0]):
        return False
    if (new_r, new_c) in visited:
        return False
    return ord(content[new_r][new_c]) - ord(content[curr_r][curr_c]) <= 1

def bfs():
    global start_r, start_c, end_r, end_c, visited
    q = Queue()
    q.put((start_r, start_c))
    lv = 1

    while not q.empty():
        sz = q.qsize()
        for _ in range(sz):
            curr_r, curr_c = q.get()
            visited.add((curr_r, curr_c))

            if (curr_r, curr_c) == (end_r, end_c):
                return lv

            for i in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                new_r, new_c = curr_r + i[0], curr_c + i[1]
                if is_valid(curr_r, curr_c, new_r, new_c):
                    q.put((new_r, new_c))     
        lv += 1

    return -1

content = open("input").read().split('\n')
content.pop()
content = [list(i) for i in content]

start_r, start_c, end_r, end_c = -1, -1, -1, -1

for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'S':
            start_r, start_c = i, j
            content[i][j] = 'a'
        if content[i][j] == 'E':
            end_r, end_c = i, j
            content[i][j] = 'z'

visited = set()
print(bfs())