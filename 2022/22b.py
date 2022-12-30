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

'''
start row and start col only
end_r = start_r * 50 + n -1 
end_c = start_c * 50 + n -1 
'''
faces = [
    (0, 1),
    (0, 2),
    (1, 1),
    (2, 1),
    (2, 0),
    (3, 0),
]
face_id = 0
n = 50      #The length of the side of each face 


'''
Contains new faces that a face can go to if follow a specific direction (in the order of right, down, left, up)
Also, followed by new direction too
When u apply lambda expressions, have to use relative locations of the points
 E.g: row = 10, column = 30 in face 1, when go up, to face 6, row = 30, column = 0 
After that, to calculate actual location, will use the actual locations above ("faces" variable) to add in
'''
next_faces = [
    [
        (1, 0, lambda r, c: (r, 0)), 
        (2, 1, lambda r, c: (0, c)), 
        (4, 0, lambda r, c: (n - 1 - r, 0)), 
        (5, 0, lambda r, c: (c, 0))
    ],
    [
        (3, 2, lambda r, c: (n -1  - r, n -1 )), 
        (2, 2, lambda r, c: (c, n -1 )), 
        (0, 2, lambda r, c: (r, n -1 )), 
        (5, 3, lambda r, c: (n -1 , c))
    ],
    [
        (1, 3, lambda r, c: (n -1 , r)), 
        (3, 1, lambda r, c: (0, c)), 
        (4, 1, lambda r, c: (0, r)), 
        (0, 3, lambda r, c: (n -1 , c))
    ],
    [
        (1, 2, lambda r, c: (n -1  - r, n -1 )), 
        (5, 2, lambda r, c: (c, n -1 )), 
        (4, 2, lambda r, c: (r, n -1 )), 
        (2, 3, lambda r, c: (n -1 , c))
    ],
    [
        (3, 0, lambda r, c: (r, 0)), 
        (5, 1, lambda r, c: (0, c)), 
        (0, 0, lambda r, c: (n -1  - r, 0)), 
        (2, 0, lambda r, c: (c, 0))
    ],
    [
        (3, 3, lambda r, c: (n -1 , r)), 
        (1, 1, lambda r, c: (0, c)), 
        (0, 1, lambda r, c: (0, r)), 
        (4, 3, lambda r, c: (n -1 , c))
    ],
]

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
            relative_r = new_r - faces[face_id][0] * n 
            relative_c = new_c - faces[face_id][1] * n 

            #Relocation
            old_face_id, old_dir_id = face_id, dir_id
            if (not (0 <= relative_r < n)) or (not (0 <= relative_c < n)):
                face_id, dir_id, convert_func = next_faces[face_id][dir_id]
                
                new_r, new_c = convert_func(relative_r, relative_c)
                new_r += faces[face_id][0] * n 
                new_c += faces[face_id][1] * n 

            if mp[new_r][new_c] == '#':
                face_id, dir_id = old_face_id, old_dir_id
                break
            else:
                start_r, start_c = new_r, new_c

res = 1000 * (start_r + 1) + 4 * (start_c + 1) + dir_id
print(res)

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
