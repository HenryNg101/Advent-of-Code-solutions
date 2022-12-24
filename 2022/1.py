# Template
import time

start_time = time.process_time()
content = open("input").read().split('\n')
count = 0

ls = []

for line in content:
    if not len(line):
        ls.append(count)
        count = 0
    else:
        count += int(line)

ls.sort()
print(f'Part A solution is: {ls[-1]}')
print(f'Part B solution is: {sum(ls[-3:])}')
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")