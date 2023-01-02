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
print(len(elves))

round = 1
while True:
    test_start_time = time.process_time()

    #Step 1: Decide where to go
    new_elves = []
    pos_counts = dict()
    for id in range(len(elves)):
        r, c = elves[id]
        new_positions = [(r + dir[0], c + dir[1]) for dir in directions]
        
        '''
        #Check the whole thing
        move = False
        for position in new_positions:
            #One of the lines that makes the program slow, there're still other lines, I need to check
            move |= position in elves
        
        if not move:
            new_elves.append((r, c))
            continue
        '''

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

    print(f'Round {round} runs in {time.process_time() - test_start_time} seconds')
    if new_elves == elves:
        break
    round += 1

    #Step 2: Moving
    for id in range(len(elves)):
        if elves[id] != new_elves[id]:
            if pos_counts[new_elves[id]] <= 1:
                elves[id] = new_elves[id]

    key = list(checks.keys()).pop(0)
    val = checks.pop(key)
    checks[key] = val

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
