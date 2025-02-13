from inputGetter import get_input

content = get_input(2015, 1)

floor = 0
check = True
res_b = -1

for id in range(len(content)):
    floor += 1 if content[id] == '(' else -1
    if check:
        if floor < 0:
            check = False
            res_b = id

print(f'Part A: {floor}')
print(f'Part B: {res_b}')