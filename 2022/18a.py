import time

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline
cubes = []
counter = 0

for line in content:
    line = tuple([int(n) for n in line.split(',')])
    cubes.append(line)
    counter += 6

#print(counter)
for i in range(len(cubes)):
    for j in range(i+1, len(cubes)):
        if cubes[i][0] == cubes[j][0] and cubes[i][1] == cubes[j][1]:
            if abs(cubes[i][2] - cubes[j][2]) == 1:
                print(f'{cubes[i]} {cubes[j]}')
                counter -= 2 
        elif cubes[i][0] == cubes[j][0] and cubes[i][2] == cubes[j][2]:
            if abs(cubes[i][1] - cubes[j][1]) == 1:
                print(f'{cubes[i]} {cubes[j]}')
                counter -= 2 
        elif cubes[i][1] == cubes[j][1] and cubes[i][2] == cubes[j][2]:
            if abs(cubes[i][0] - cubes[j][0]) == 1:
                print(f'{cubes[i]} {cubes[j]}')
                counter -= 2 

print(counter)
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
