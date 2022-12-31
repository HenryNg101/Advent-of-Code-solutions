import time
import re

def bfs(robots):
    pass

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline

for line in content:
    robots = dict()
    for robot_line in line.split('Each')[1:]:
        requirements = robot_line.strip()[:-1].split()
        costs = dict()
        for i in range(3, len(requirements), 3):
            costs[requirements[i+1]] = int(requirements[i])
        robots[requirements[0]] = costs
    bfs(robots)

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")

'''
need to collect obsidian from the pond => need obsidian-collecting robots
there are clay nearby, used to make them (robots???) waterproof => need special-purpose clay-collecting robots.
make robot => need ore => need ore-collecting robots (We only have one)

Only have 24 mins to open max geodes

Sample input:
Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
'''