from queue import Queue

def is_valid(curr_r, curr_c, new_r, new_c, visited, content):
    if new_r < 0 or new_r >= len(content) or new_c < 0 or new_c >= len(content[0]):
        return False
    if visited[new_r][new_c]:
        return False
    return ord(content[new_r][new_c]) - ord(content[curr_r][curr_c]) >= -1

#The trick here is to start tracking from end point to start, as there will be multiple starting points in task B
def bfs(start_r, start_c, end_r, end_c, content):
    q = Queue()
    q.put((end_r, end_c))
    res_A = 0
    res_B = 9999999999999999
    visited = [[False for _ in range(len(content[0]))] for _ in range(len(content))]

    while not q.empty():
        sz = q.qsize()
        for _ in range(sz):
            curr_r, curr_c = q.get()
            visited[curr_r][curr_c] = True

            if (curr_r, curr_c) == (start_r, start_c):
                return res_A, res_B
            
            #As soon as it meets an a, which is a possible start point (for task B), 
            if content[curr_r][curr_c] == 'a':
                res_B = min(res_B, res_A)

            for i in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                new_r, new_c = curr_r + i[0], curr_c + i[1]
                if is_valid(curr_r, curr_c, new_r, new_c, visited, content):
                    q.put((new_r, new_c))
                    visited[new_r][new_c] = True 
        res_A += 1
    #If nothing is found
    return -1, -1

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

print(f'Part A and B answers are: {bfs(start_r, start_c, end_r, end_c, content)}, consecutively')