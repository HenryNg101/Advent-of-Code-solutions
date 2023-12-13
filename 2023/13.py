from typing import List, Tuple

def process_map(mp: List[List[str]], old_res: Tuple[int, int] = None) -> Tuple[int, int] | None:
    sz_r, sz_c = len(mp), len(mp[0])
    # Contains common middle ids of palindromes in all rows and cols
    palindrome_mids_horizontal, palindrome_mids_vertical = set(), set()

    # Horizontal processing
    for row_id, line in enumerate(mp):
        row_palindrome_mids = set()   # Contains the middle ids of palindromes in a line

        # Check and get all valid middle ids for palindromes
        for palindrome_mid in range(1, sz_c):
            palindrome_start, palindrome_end = palindrome_mid - 1, palindrome_mid

            while palindrome_start >= 0 and palindrome_end < sz_c and line[palindrome_start] == line[palindrome_end]:
                palindrome_start -= 1
                palindrome_end += 1

            if palindrome_end - palindrome_start > 1 and (palindrome_start == -1 or palindrome_end == sz_c):
                row_palindrome_mids.add(palindrome_mid)
    
        palindrome_mids_horizontal = row_palindrome_mids if row_id == 0 else palindrome_mids_horizontal.intersection(row_palindrome_mids)

    # Checking for horizontal split, the point that is the mid of palindrome(s) in all rows
    for palindrome_mid in palindrome_mids_horizontal:
        if not old_res or (1, palindrome_mid) != old_res:
            return (1, palindrome_mid)

    #Vertical processing
    for c in range(sz_c):
        col_palindrome_mids = set()
        for palindrome_mid in range(1, sz_r):
            palindrome_start, palindrome_end = palindrome_mid - 1, palindrome_mid
            while palindrome_start >= 0 and palindrome_end < sz_r and mp[palindrome_start][c] == mp[palindrome_end][c]:
                palindrome_start -= 1
                palindrome_end += 1

            if palindrome_end - palindrome_start > 1 and (palindrome_start == -1 or palindrome_end == sz_r):
                col_palindrome_mids.add(palindrome_mid)

        palindrome_mids_vertical = col_palindrome_mids if c == 0 else palindrome_mids_vertical.intersection(col_palindrome_mids)

    for palindrome_mid in palindrome_mids_vertical:
        if not old_res or (100, palindrome_mid) != old_res:
            return (100, palindrome_mid)


input = [line.strip() for line in open("input").readlines()]
line_id = 0
res_a, res_b = 0, 0

while line_id < len(input):
    mp = []
    while line_id < len(input) and len(input[line_id]) > 0:
        mp.append(list(input[line_id]))
        line_id += 1

    mul, val = process_map(mp)
    res_a += mul * val

    # Backtracking for part 2
    copy_mul, copy_val = (mul, val)
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            mp[i][j] = '.' if mp[i][j] == '#' else '#'
            
            new_res = process_map(mp, (mul, val))

            mp[i][j] = '.' if mp[i][j] == '#' else '#'

            if new_res != None:
                mul, val = new_res
                break
        
        if (copy_mul, copy_val) != (mul, val):
            break

    res_b += mul * val
    line_id += 1

print(f'Part 1: {res_a}')
print(f'Part 2: {res_b}')