import time
import re

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline

register = 0
current_cycle = 0
row, col = 0, 0

crt = [['.'] * 40 for _ in range(6)]

for line in content:
    line = line.split()
    if line[0] == 'noop':
        #print(register)
        if col in range(register, register + 3):
            crt[row][col] = '#'
        current_cycle += 1
        col += 1
        if col >= len(crt[0]):
            row, col = row + 1, 0
    else:
        for _ in range(2):
            #print(register)
            if col in range(register, register + 3):
                crt[row][col] = '#'
            current_cycle += 1
            col += 1
            if col >= len(crt[0]):
                row, col = row + 1, 0
        register += int(line[1])

for line in crt:
    for char in line:
        print(char, end='')
    print()

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")

'''
X register controls horizontal pos of sprite
The sprite is 3 pixels wide ??
'''