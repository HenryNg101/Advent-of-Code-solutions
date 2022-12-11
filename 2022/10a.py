# Template code
content = open("input").read().split('\n')
content.pop()

res = 0
register = 1
current_cycle = 1

special = [20, 60, 100, 140, 180, 220]

for line in content:
    line = line.split()
    if line[0] == 'noop':
        if current_cycle in special:
            res += current_cycle * register
        current_cycle += 1
    else:
        for _ in range(2):
            if current_cycle in special:
                res += current_cycle * register
            current_cycle += 1
        register += int(line[1])

print(res)