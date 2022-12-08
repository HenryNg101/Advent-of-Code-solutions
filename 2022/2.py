content = open("input").read().split('\n')
content.pop()

#Result for part A, and rules on what would makes right win left (ot can be used the other way too)
res_A = 0
win_A = [2, 0, 1]

#Result for part B, and what response should be placed to make sure that the outcome is same as expected
res_B = 0
win_B = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]

for line in content:
    s = line.split()
    left, right = ord(s[0]) - ord('A'), ord(s[1]) - ord('X')
    
    #Part A
    res_A += right + 1
    if left == right:
        res_A += 3
    else:
        res_A += 6 if win_A[right] == left else 0
    #Part B
    res_B += right * 3 + win_B[left][right]

print(f'Part A solution is: {res_A}')
print(f'Part B solution is: {res_B}')