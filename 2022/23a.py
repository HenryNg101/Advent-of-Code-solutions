import time

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline

elves = []

directions = [
    (-1, -1), 
    (-1, 0), 
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1)
]

checks = {
    (0, 1, 2): 1,
    (4, 5, 6): 5,
    (0, 6, 7): 7,
    (2, 3, 4): 3,
}

for r in range(len(content)):
    for c in range(len(content[0])):
        if content[r][c] == '#':
            elves.append((r, c))

for _ in range(10):

    #Step 1: Decide where to go
    new_elves = []
    pos_counts = dict()
    for id in range(len(elves)):
        print(elves[id])
        r, c = elves[id]
        new_positions = [(r + dir[0], c + dir[1]) for dir in directions]
        
        #Check the whole thing
        move = False
        for position in new_positions:
            move |= position in elves
        if not move:
            new_elves.append((r, c))
            continue

        #Check each direction
        for pos_set in checks:
            moving = True
            for index in pos_set:
                if new_positions[index] in elves:
                    moving = False
                    break
            if moving:
                move_pos = new_positions[checks[pos_set]]

                new_elves.append(move_pos)
                if move_pos not in pos_counts:
                    pos_counts[move_pos] = 0
                pos_counts[move_pos] += 1
                break
        if len(new_elves) <= id:
            new_elves.append((r, c))

    #Step 2: Moving
    for id in range(len(elves)):
        if elves[id] != new_elves[id]:
            if pos_counts[new_elves[id]] <= 1:
                elves[id] = new_elves[id]
    
    #directions.append(directions.pop(0))
    #checks.pop()
    key = list(checks.keys()).pop(0)
    val = checks.pop(key)
    checks[key] = val

max_r = -99999999999
max_c = -99999999999
min_r, min_c = 99999999999, 99999999999

for elve in elves:
    r, c = elve
    max_r = max(max_r, r)
    min_r = min(min_r, r)
    max_c = max(max_c, c)
    min_c = min(min_c, c)

print(f'{min_r} {max_r} {min_c} {max_c}')
print((max_r - min_r + 1) * (max_c - min_c + 1) - len(elves))

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")

'''
Input: The grove with Elves's positions (marked with "#")
Outside of existing scan, empty grounds extend every direction

Directions: N, S, W, E, NE, NW, SE, SW

Sample input:
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..

Will have some rounds, each round consist of the process:
1. Decide where to go:
    - If no any Elves in one of eight positions => no moving.
    - Otherwise:
        - if no one in N, NE, NW => North
        - elif no one in S, SE, SW => South
        - elif no one in W, NW, SW => West
        - elif no one in E, SE, NE => East
2. Moving:
    - Each Elve move to proposed position only when it would be occupied by only one Elve, otherwise none of those Elve moves
    - After this, the priority change (like a queue) .E.g: Round 1: N, S, W, E => Round 2: S, W, E, N and so on.

'''