import time

start_time = time.process_time()
content = open("input").read().split('\n')
content.pop()
counter_A = 0   #Inclusion check
counter_B = 0   #Overlap check

for line in content:
    left, right = line.split(',')
    s1, e1 = [int(x) for x in left.split('-')]
    s2, e2 = [int(x) for x in right.split('-')]

    counter_A += int((s2 <= s1 and e2 >= e1) or (s1 <= s2 and e1 >= e2))
    counter_B += int((s1 >= s2 and s1 <= e2) or (e1 >= s1 and s2 <= e1))

print(f'Part A solution is: {counter_A}')
print(f'Part B solution is: {counter_B}')
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
