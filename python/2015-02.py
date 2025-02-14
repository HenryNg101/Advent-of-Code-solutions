from inputGetter import get_input

content = get_input(2015, 2).split('\n')

total_a = 0
total_b = 0

for line in content:
    a, b, c = [int(i) for i in line.split('x')]
    s1, s2, s3 = a * b, b * c, a * c
    
    total_a += 2 * (s1 + s2 + s3) + min(s1, s2, s3)
    total_b += 2 * (a + b + c - max(a, b, c)) + a * b * c

print(f'Part A: {total_a}')
print(f'Part B: {total_b}')