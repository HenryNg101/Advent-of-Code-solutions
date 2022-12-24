import time

start_time = time.process_time()
content = open("input").read().split('\n')
content.pop()

total = 0
min_x = 99999999999999999999
max_x = -99999999999999999999
target_y = 2000000
excluded_xs = set()

for line in content:
    line = line.split()
    locs = [loc[2:] for loc in line if any(map(str.isdigit, loc))]   #Only take integer coordinates
    
    for i in range(len(locs)):
        if not locs[i][-1].isdigit():
            locs[i] = locs[i][:-1]
    
    locs = [int(loc) for loc in locs]

    dis = abs(locs[0] - locs[2]) + abs(locs[1] - locs[3])
    #print(f'{locs} {dis}')

    abs_val = dis - abs(locs[1] - target_y)
    if abs_val >= 0:
        max_val, min_val = locs[0] + abs_val, locs[0] - abs_val
        min_x = min(min_x, min_val)
        max_x = max(max_x, max_val)

    if locs[1] == target_y:
        excluded_xs.add(locs[0])
    if locs[3] == target_y:
        excluded_xs.add(locs[2])

total += abs(min_x - max_x) + 1
for val in excluded_xs:
    if min_x <= val <= max_x:
        total -= 1
print(total)
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
