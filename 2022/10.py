import time

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline

#General register, start off from position 0 in part B, but value 1 in part A
register = 0

#Part A variables
res = 0
special = [20, 60, 100, 140, 180, 220]
current_cycle = 1

#Part B variables
row, col = 0, 0
crt = [['.'] * 40 for _ in range(6)]

for line in content:
    line = line.split()

    '''
    Because addx instructions has 2 words and need 2 cycles, and noop has one word and need one cycle only
    => Only need to use the size of line to make loop
    '''
    for _ in range(len(line)):
        #Handle part A
        if current_cycle in special:
            res += current_cycle * (register + 1)
        current_cycle += 1

        #Handle part B
        if col in range(register, register + 3):
            crt[row][col] = '#'
        col += 1
        if col >= len(crt[0]):
            row, col = row + 1, 0
    
    if len(line) == 2:
        register += int(line[1])

print(f'Part A result is: {res}')
print(f'Part B result is: ')
for line in crt:
    for char in line:
        print(char, end='')
    print()
print()

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
