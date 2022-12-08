def eval_char(ch):
    return ord(ch) - ord('A') + 27 if ch.isupper() else ord(ch) - ord('a') + 1

content = open("input").read().split('\n')
content.pop()
#Part A
res_A = 0
for line in content:
    mid = len(line)//2
    for ch in set(line[:mid]) & set(line[mid:]):
        res_A += eval_char(ch)

#Part B
res_B = 0
for i in range(0, len(content), 3):
    for ch in set(content[i]) & set(content[i+1]) & set(content[i+2]):
        res_B += eval_char(ch)

print(f'Part A solution is: {res_A}')
print(f'Part B solution is: {res_B}')