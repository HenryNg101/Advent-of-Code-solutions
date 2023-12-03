from typing import Dict, Tuple

input = open("input").readlines()
sz_r, sz_c = len(input), len(input[0])
res_a, res_b = 0, 0

'''Return adjacent positions of a position'''
def adjacent_map(r: int, c: int) -> Dict[Tuple[int, int], bool]:
    return { 
        (r-1, c-1): False, (r-1, c): False, (r-1, c+1): False, (r, c-1): False, 
        (r, c+1): False, (r+1, c-1): False, (r+1, c): False, (r+1, c+1): False
    }


'''Helper function, to find a number, given a position of a digit of that number'''
def find_number(r: int, c: int, visited) -> int:
    #Find start and end of the number
    start = end = c
    while start >= 0 and input[r][start].isnumeric():
        start -= 1
    while end < sz_c and input[r][end].isnumeric():
        end += 1
    
    #Fill these positions, so we don't find redundant numbers
    for other_c in range(c-2, c+3):
        if other_c > start and other_c < end and (r, other_c) in visited:
            visited[(r, other_c)] = True
    
    return int(input[r][start+1: end])


'''Part 1's function, to add all possible numbers surrounded by a symbol'''
def engine_numbers(r: int, c: int) -> int:
    visited = adjacent_map(r, c)
    global res_a
    
    for new_r, new_c in visited.keys():
        if new_r < 0 or new_r >= sz_r or new_c < 0 or new_c >= sz_c:
            continue
        
        if not visited[(new_r, new_c)] and input[new_r][new_c].isnumeric():
            res_a += find_number(new_r, new_c, visited)


'''Part 2's function, return the product of each star, if there's any'''
def valid_gears(r: int, c: int) -> int:
    visited = adjacent_map(r, c)
    global res_b
    gears_count, prod = 0, 1
    
    for new_r, new_c in visited.keys():
        if new_r < 0 or new_r >= sz_r or new_c < 0 or new_c >= sz_c:
            continue
        
        if not visited[(new_r, new_c)] and input[new_r][new_c].isnumeric():
            prod *= find_number(new_r, new_c, visited)
            gears_count += 1
    
    return prod if gears_count == 2 else 0


for r in range(sz_r):
    for c in range(sz_c):
        #Part 1
        if not input[r][c].isnumeric() and input[r][c] not in ['.', '\n']:
            engine_numbers(r, c)
        
        #Part 2
        if input[r][c] == '*':
            res_b += valid_gears(r, c)
            
print(f"Part 1: {res_a}")
print(f"Part 2: {res_b}")