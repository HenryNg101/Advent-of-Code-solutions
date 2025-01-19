import math
import time

# Start the timer
start_time = time.time()

input = open("input").readlines()
limits = {'red': 12, 'green': 13, 'blue': 14}
res_a, res_b = 0, 0

for line in input:
    #Separate records
    records = line.split('; ')
    
    valid_game = True
    game_id = -1
    min_colors = {'red': 0, 'green': 0, 'blue': 0}
    
    for record_id, record in enumerate(records):
        record = record.split(' ')
        
        #First record has game number too, has to filter it, keep color counts only
        #After this processing, a record might looks smt like this: ['3', 'green,', '3', 'blue,', '1', 'red\n']
        if record_id == 0:
            game_id = int(record[1][:-1])
            record = record[2:]
        
        for i in range(0, len(record), 2):
            color_cnt, color_name = record[i: i+2]
            color_cnt = int(color_cnt)
            
            #Remove trailing character, if there's any
            if not color_name[-1].isalpha():
                color_name = color_name[:-1]

            # Part A
            if limits[color_name] < color_cnt:
                valid_game = False
            
            # Part B
            min_colors[color_name] = max(color_cnt, min_colors[color_name])
    
    #Add result to both parts
    res_b += math.prod(min_colors.values())
    if valid_game:
        res_a += game_id

print(f"Part 1: {res_a}")
print(f"Part 2: {res_b}")
print(f'Elapsed time: {time.time() - start_time} seconds')