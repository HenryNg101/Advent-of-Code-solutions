import time

start_time = time.process_time()
content = open("input").read().split('\n')
content.pop()

def main(knots_count: int):
    visited = set()
    knots = [[0, 0] for _ in range(knots_count)]

    for line in content:
        direction, moves = line.split(' ')
        moves = int(moves)

        for _ in range(moves):
            if direction == 'U':
                knots[0][0] -= 1
            elif direction == 'D':
                knots[0][0] += 1
            elif direction == 'L':
                knots[0][1] -= 1
            else:
                knots[0][1] += 1
        
            #Update new location of the following knots, one by one
            for i in range(knots_count - 1):
                cmp_r, cmp_c = knots[i][0] - knots[i+1][0], knots[i][1] - knots[i+1][1]

                if abs(cmp_r) >= 2 or abs(cmp_c) >= 2:
                    if cmp_r != 0:
                        cmp_r //= abs(cmp_r)
                    if cmp_c != 0:
                        cmp_c //= abs(cmp_c)
                    knots[i+1][0] += cmp_r
                    knots[i+1][1] += cmp_c

            visited.add(tuple(knots[-1]))

    return len(visited)

print(f'Part A answer is: {main(2)}')
print(f'Part B answer is: {main(10)}')
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")

""" 
a = rH - rT, b = cH - cT (H is head, T is tail)

All the cases when a knot need to move:
    top left => -1, -2 or -2, -1 => rT + (-1), cT + (-1)
    top right => -1, 2 or -2, 1 => rT + (-1), cT + 1 
    bot left => 1, -2 or 2, -1 => rT + 1, cT + (-1)
    bot right => 1, 2 or 2, 1 => rT + 1, cT + 1
    left => 0, -2 => rT + 0, cT + (-1)
    right => 0, 2 => rT + 0, cT + 1
    top => -2, 0 => rT + (-1), cT + 0
    bot => 2, 0 => rT + 1, cT + 0 

From above pattern, we can see that, the formula to calculate where to move is:
row = a // abs(a)
col = b // abs(b)
"""