# Aoc 2023 solutions

Here is a quick overview of approaches to the problems (To learn more, go to the files and have a look):
- Day 1: Some simple processing, with the use of hashmap and substring
- Day 2: Still some relatively simple logics.
- Day 3: Use a set to remember visited locations of area near each valid symbol based on the question.
- Day 4: Just a simulation problem
- Day 5: Normal conversion (part 1). Merge intervals (part 2)
- Day 6: Math question. Just need to solve the **quadratic inequality equation x ^ 2 - bx + c < 0** to find out max and min x
- Day 7: Sorting with custom sorting rule
- Day 8: Use **LCM**, as we need to start at multiple starts at the same time.
- Day 9: Just a simulation problem
- Day 10: BFS for part 1. Part 2 needs some smart zooming/shrinking techniques to helping with the case of "squeezing between pipes"
- Day 11: Saving coordinates as pairs, and empty columns and rows ids for future expansion. Better than actually simulates the whole thing.
- Day 12: **2D Dynamic Programming**, with one dimension is the springs string ID, and the other dimension is the id of the number list. Knapsack 0/1 type of problem (Either choose or not in some places)
- Day 13: **Palindromic string**. Find the common middle ids in horizontal and vertical of the map to find reflection. Second part is just simply backtracking on the map and do the same.
- Day 14: The first problem that involves finding pattern in an infinite/very large simulation. Each cycle produce a result, and by some way, after some cycles iterations, there's a loop, similar to **"Linked List cycle"** problem. Just find out the start of the loop, and calculate on that.
- Day 15: Simple simulation
- Day 16: Simple **BFS/DFS**. Even second part can brute force by BFS/DFS on every valid starting points and every directions (It's not the whole map, so it's not too large)
- Day 17: **Dijkstra algorithm**. But with a limit on the minimum traveled blocks to turn, and maximum traveled blocks before a force turn.
- Day 18: BFS/DFS (Only works with part 1, on small size input). **Shoelace formula** fits perfectly with the problem. I also heard about sweeping line algorithm, will try it in the future.
- Day 19: DFS on second part, to find min and max possible values of all four ratings. Then do a product on these four rating ranges.
- Day 20: Simple simulation on first part. Second part needs to use LCM on the modules that are related very closely to the final goal. Read more on the code file to understand.
- Day 21: Straightforward BFS on part 1. Highly complex finding pattern and optimization problem on part 2. Read more on the code file to find out.
- Day 22: A bit of simulation of bricks falling, then, use **Kahn algorithm** (as these bricks relationships can be formed as DAG) to find out the amount of falling bricks when one brick is disintegrated.
- Day 23: Optimization problem again. Since longest path is NP-hard problem, we only take the starting, ending position, and positions where there can be multiple turns into consideration. Then, backtrack on these positions to find out longest path.
- Day 24: 
    - First part is just finding the line equations **y = ax + b** on these lines, and check condition to see if this is counted. 
    - Second part can be fit into a **SMT (Satisfiability modulo theories)** problem, with multiple variables and conditions. Just need to use a solver, like Z3 Theorem prover, to solve it.
- Day 25: A **graph minimum cut** problem (min cut to separate a connected graph into 2 separate connected sets). Can use **Stoer-Wagner algorithm** or **max-flow min-cut theorem** to solve the problem.