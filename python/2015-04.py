from inputGetter import get_input
import hashlib

content = get_input(2015, 4)

def lowest_md5(n: int):
    global content
    i = 1
    while True:
        s = content + str(i)
        if hashlib.md5(s.encode()).hexdigest()[:n] == '0' * n:
            break
        i += 1
    return i  

print(f'Part A: {lowest_md5(5)}')
print(f'Part B: {lowest_md5(6)}')