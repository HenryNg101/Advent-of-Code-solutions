# Only applicable for this part, not for next part
# Need to optimize later for next part
content = open("input").read().split('\n')
content.pop()

def main(knots_count: int):
    visited = [[False for _ in range(1000)] for _ in range(1000)]
    knots = [[500, 500] for _ in range(knots_count)]
    count = 0

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
        
            #Update new location of the tail (Will be extended for every positions)
            for i in range(knots_count - 1):
                cmp_r, cmp_c = knots[i][0] - knots[i+1][0], knots[i][1] - knots[i+1][1]

                if abs(cmp_r) >= 2 or abs(cmp_c) >= 2:
                    if cmp_r != 0:
                        cmp_r //= abs(cmp_r)
                    if cmp_c != 0:
                        cmp_c //= abs(cmp_c)
                    knots[i+1][0] += cmp_r
                    knots[i+1][1] += cmp_c

            #Check visited
            if not visited[knots[-1][0]][knots[-1][1]]:
                count += 1
                visited[knots[-1][0]][knots[-1][1]] = True

    return count

print(f'Part a answer is: {main(2)}')
print(f'Part b answer is: {main(10)}')

""" . H H H .
H . . . H
H . T . H
H . . . H
. H H H .

For diagonal moves, need to find out which quarter the new head is in

a = rH - rT, b = cH - cT

a /= abs(a)
b /= abs(b)

top left => -1, -2 or -2, -1 => rT + (-1), cT + (-1)
top right => -1, 2 or -2, 1 => rT + (-1), cT + 1 
bot left => 1, -2 or 2, -1 => rT + 1, cT + (-1)
bot right => 1, 2 or 2, 1 => rT + 1, cT + 1

left => 0, -2 => rT + 0, cT + (-1)
right => 0, 2 => rT + 0, cT + 1
top => -2, 0 => rT + (-1), cT + 0
bot => 2, 0 => rT + 1, cT + 0 """