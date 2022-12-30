import time
import re

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline

mp = []
max_sz = 0
for line in content:
    if len(line) == 0:
        break
    mp.append(line)
    max_sz = max(max_sz, len(line))

for i in range(len(mp)):
    mp[i] += ' ' * (max_sz - len(mp[i]))

instructions = re.split('(\d+)', content[-1])[1:-1]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_id = 0

#Find starting point
start_r, start_c = -1, -1
for i in range(len(mp)):
    start_c = mp[i].find('.')
    if start_c != -1:
        start_r = i
        break

for inst in instructions:
    if inst == 'R':
        dir_id += 1
        if dir_id >= len(directions):
            dir_id = 0
    elif inst == 'L':
        dir_id -= 1
        if dir_id < 0:
            dir_id = len(directions) - 1
    else:
        new_r, new_c = start_r, start_c
        for _ in range(int(inst)):
            new_r = start_r + directions[dir_id][0]
            new_c = start_c + directions[dir_id][1]
            if new_r < 0:
                new_r = len(mp) - 1
            if new_r >= len(mp):
                new_r = 0
            if new_c < 0:
                new_c = len(mp[0]) - 1
            if new_c >= len(mp[0]):
                new_c = 0
            
            while mp[new_r][new_c] == ' ':
                new_r += directions[dir_id][0]
                new_c += directions[dir_id][1]
                if new_r < 0:
                    new_r = len(mp) - 1
                if new_r >= len(mp):
                    new_r = 0
                if new_c < 0:
                    new_c = len(mp[0]) - 1
                if new_c >= len(mp[0]):
                    new_c = 0
            
            if mp[new_r][new_c] == '#':
                break
            else:
                start_r, start_c = new_r, new_c

res = 1000 * (start_r + 1) + 4 * (start_c + 1) + dir_id
print(res)

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
