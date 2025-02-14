from inputGetter import get_input

content = get_input(2015, 3)

start_loc = [0, 0]
res_a = set()
res_a.add(tuple(start_loc))

for char in content:
    if char == '^':
        start_loc[0] -= 1
    elif char == 'v':
        start_loc[0] += 1
    elif char == '<':
        start_loc[1] -= 1
    else:
        start_loc[1] += 1
    res_a.add(tuple(start_loc))

print(f'Part A: {len(res_a)}')

start_loc = [[0, 0], [0, 0]]
res_b = [set(), set()]
res_b[0].add(tuple(start_loc[0]))

for i in range(0, len(content), 2):
    for j in range(2):
        char = content[i+j]
        if char == '^':
            start_loc[j][0] -= 1
        elif char == 'v':
            start_loc[j][0] += 1
        elif char == '<':
            start_loc[j][1] -= 1
        else:
            start_loc[j][1] += 1
        res_b[j].add(tuple(start_loc[j]))

print(f'Part B: {len(res_b[0] | res_b[1])}')