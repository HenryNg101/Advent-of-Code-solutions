from typing import List
import functools as ft
import time

# Start the timer
start_time = time.time()

# Knapsack DP style
# With each '?', you can choose to skip or count in. For the case of '.'/'#', it's already obvious to skip/proceed
@ft.cache
def knapsack(springs: str, nums: List[int], num_id: int, spring_id: int) -> int:
    # Base case
    if spring_id >= len(springs):
        return int(num_id >= len(nums))

    ways = 0

    # Skipping
    if springs[spring_id] in ['.', '?']:
        ways += knapsack(springs, nums, num_id, spring_id + 1)

    # Counting this in
    if num_id < len(nums) and springs[spring_id] in ['#', '?']:
        end_id = spring_id + nums[num_id]
        
        # Must have enough capacity to has the valid length of the current number
        if end_id <= len(springs):
            sub_str = springs[spring_id: end_id]

            # And of course, the character following that must not be '#', otherwise, they are not separated
            if '.' not in sub_str and (end_id == len(springs) or springs[end_id] != '#'):
                ways += knapsack(springs, nums, num_id+1, spring_id + nums[num_id] + 1)
    
    return ways

# Iterative version
@ft.cache
def knapsack_iterative(springs: str, nums: List[int]) -> int:
    sz_c, sz_r = len(springs), len(nums)

    # Create a 2D array to store results
    # Extra column for the case of empty springs string, and row for empty number list
    dp = [[0] * (sz_c + 1) for _ in range(sz_r + 1)]
    dp[-1][-1] = 1  # Base case

    # Iterate from the end. If springs value empty, it can't be compared against number(s) in the number list
    # That's why, we start from last row, where there's no number, and start from last column - 1, where there's at least one character
    for r in range(sz_r, -1, -1):
        for c in range(sz_c - 1, -1, -1):
            # Skipping
            if springs[c] in ['.', '?']:
                dp[r][c] += dp[r][c + 1]

            # If there's no number, def can't use the case of counting in, because there's nothing to be compared against
            if r >= sz_r: 
                continue

            end_id = c + nums[r]
            if end_id > sz_c:
                continue    # Skipping this for not enough length, as required

            # Counting this in
            if springs[c] in ['#', '?']:
                # The character following that must not be '#', otherwise, they are not separated
                if '.' not in springs[c: end_id] and (end_id == sz_c or springs[end_id] != '#'):
                    dp[r][c] += dp[r + 1][end_id + 1] if end_id + 1 <= sz_c else dp[r+1][end_id]

    return dp[0][0]

input = [line.strip() for line in open("input").readlines()]
res_a, res_b = 0, 0

for id, line in enumerate(input):
    springs, nums = line.split()
    nums = tuple([int(num) for num in nums.split(',')])

    # Either of these works similarly
    # res_a += knapsack(springs, nums, 0, 0)
    # res_b += knapsack('?'.join([springs] * 5), nums * 5, 0, 0)

    res_a += knapsack_iterative(springs, nums)
    res_b += knapsack_iterative('?'.join([springs] * 5), nums * 5)

print(f'Part 1: {res_a}')
print(f'Part 2: {res_b}')
print(f'Elapsed time: {time.time() - start_time} seconds')