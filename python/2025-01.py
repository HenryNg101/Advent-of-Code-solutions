from inputGetter import get_input

content = get_input(2025, 1).split('\n')

pos = 50
res_a, res_b = 0, 0
for line in content:
    move = int(line[1:])
    res_b += int(move / 100)
    
    move %= 100
    new_pos = pos
    if line[0] == 'L':
        new_pos -= move
    else:
        new_pos += move
        
    if pos > 0 and (new_pos <= 0 or new_pos >= 100):
        res_b += 1
    
    pos = new_pos % 100
    if pos == 0:
        res_a += 1

print(f"Part A: {res_a}")
print(f"Part B: {res_b}")