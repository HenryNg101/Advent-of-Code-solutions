import time

#TODO: Need to optimize later on, this program runs for almost 2 mins
content = open("input").read().split('\n')
content.pop()

start_time = time.process_time()

coordinates = []
for line in content:
    line = line.split()
    locs = [loc[2:] for loc in line if any(map(str.isdigit, loc))]   #Only take integer coordinates
    
    for i in range(len(locs)):
        if not locs[i][-1].isdigit():
            locs[i] = locs[i][:-1]
    
    coordinates.append([int(loc) for loc in locs]) 

for target_y in range(0, 4000001):
    intervals = []
    for locs in coordinates:
        dis = abs(locs[0] - locs[2]) + abs(locs[1] - locs[3])
        abs_val = dis - abs(locs[1] - target_y)

        if abs_val >= 0:
            max_x, min_x = locs[0] + abs_val, locs[0] - abs_val
            min_x = max(min_x, 0)
            max_x = min(max_x, 4000000)
            intervals.append((min_x, max_x))
    intervals.sort(key=lambda x: x[0])
    min_x, max_x = intervals[0]
    
    max_point = intervals[0][1]
    found = False
    for i in range(1, len(intervals)):
        if intervals[i][0] - max_point == 2:
            print(f'{(intervals[i][0] - 1) * 4000000 + target_y}')
            found = True
            break
        max_point = max(intervals[i][1], max_point)
    if found:
        break

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")