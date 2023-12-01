input = open("input").readlines()
res = 0

def find_first_number(line) -> int:
    for c in line:
        if c.isdigit():
            return int(c)
    return -1

for line in input:
    res += find_first_number(line) * 10 + find_first_number(line[::-1])

print(res)