from typing import List
import functools as ft

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
        end_spring_id = spring_id + nums[num_id]
        
        # Must have enough capacity to has the valid length of the current number
        if end_spring_id <= len(springs):
            sub_str = springs[spring_id: end_spring_id]

            # And of course, the character following that must not be '#', otherwise, they are not separated
            if '.' not in sub_str and (end_spring_id == len(springs) or springs[end_spring_id] != '#'):
                ways += knapsack(springs, nums, num_id+1, end_spring_id + 1)
    
    return ways

input = [line.strip() for line in open("input").readlines()]
res_a, res_b = 0, 0

for id, line in enumerate(input):
    springs, nums = line.split()
    nums = tuple([int(num) for num in nums.split(',')])

    res_a += knapsack(springs, nums, 0, 0)
    res_b += knapsack('?'.join([springs] * 5), nums * 5, 0, 0)

print(f'Part 1: {res_a}')
print(f'Part 2: {res_b}')