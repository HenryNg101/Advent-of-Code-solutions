from inputGetter import get_input

content = get_input(2015, 6).split('\n')[:-1]
grid_a = [[False for _ in range(1000)] for _ in range(1000)]
grid_b = [[0 for _ in range(1000)] for _ in range(1000)]
counter_a, counter_b = 0, 0

for line in content:
    line = line.split()
    inst, start_co, stop_co = line[0], line[1], line[3]
    if line[0] == 'turn':
        inst, start_co, stop_co = line[1], line[2], line[4]

    start_c, start_r = [int(x) for x in start_co.split(',')]
    stop_c, stop_r = [int(x) for x in stop_co.split(',')]
    
    for r in range(start_r, stop_r + 1):
        for c in range(start_c, stop_c + 1):
            if inst == 'toggle':
                grid_a[r][c] = not grid_a[r][c]
                grid_b[r][c] += 2
            else:
                grid_a[r][c] = (inst == 'on')
                if grid_a[r][c]:
                    grid_b[r][c] += 1
                else:
                    grid_b[r][c] -= 1 if grid_b[r][c] > 0 else 0

for r in range(1000):
    for c in range(1000):
        counter_a += grid_a[r][c]
        counter_b += grid_b[r][c]
        
print(f"Part A: {counter_a}")
print(f"Part B: {counter_b}")