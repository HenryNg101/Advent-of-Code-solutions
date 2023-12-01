input = open("input").readlines()
res = 0

dic = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
    "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def find_number(first: int, last: int, step: int = 1) -> int:
    for i in range(first, last, step):
        if line[i].isdigit():
            return int(line[i])
        
        for digit in [line[i: i+3], line[i: i+4], line[i: i+5]]:
            if digit in dic:
                return dic[digit]
    return -1

for line in input:
    res += find_number(0, len(line)) * 10 + find_number(len(line) - 1, -1, -1)

print(res)