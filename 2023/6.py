import math

'''
Math works for this code:
Assuming that:
- Time for holding to increase speed is x
- Time for the boat to move: y
- Amount of given time we have: b
- Amount of required distance: c

Then, this is what we have:
x + y = b, x * y > c
=> x * (b - x) > c
=> x ** 2 - bx + c < 0

To solve the above equation, solve this first:
x ** 2 - bx + c = 0
=> x = (b +/- sqrt(b ** 2 - 4c)) / 2
=> 2 values for upper and lower bound, just need to adjust (lower the max value, and upper the min value)
=> Done !!!
'''

def count_winning_ways(time: int, distance: int) -> int:
    delta_sqrt = math.sqrt(time ** 2 - 4 * distance)
    
    # Find upper/lower bounds of the time needed for winning
    upper_bound, lower_bound = math.floor((time + delta_sqrt) / 2), math.ceil((time - delta_sqrt) / 2)
    upper_bound -= upper_bound * (time - upper_bound) == distance
    lower_bound += lower_bound * (time - lower_bound) == distance
    
    return upper_bound - lower_bound + 1

input = open("input").readlines()

#Part 1 code
times, distances = [[int(val) for val in line.split()[1:]] for line in input]
res_a = math.prod([count_winning_ways(times[i], distances[i]) for i in range(len(times))])
print(f"Part 1: {res_a}")

#Join numbers to get the time and distance for part 2
time, distance = [int(''.join(line.split()[1:])) for line in input]
print(f"Part 2: {count_winning_ways(time, distance)}")
