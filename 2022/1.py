# Template
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