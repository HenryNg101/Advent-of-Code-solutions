from inputGetter import get_input

content = get_input(2025, 2).split(',')

max_len = 0
for i in range(len(content)):
    content[i] = content[i].split('-')
    max_len = max(max_len, len(content[i][1]))
    content[i] = [int(num) for num in content[i]]

res_a, res_b = 0, 0
visited_nums = set()
for sz in range(2, max_len + 1, 1):
    for parts_cnt in range(2, sz+1):    # part_cnt is the number of time a number is repeated
        if sz % parts_cnt == 0:
            part_len = int(sz / parts_cnt)
            
            # Iterate through all values. 
            # For example, with a number that has 2 repeated sequence, each sequence has length of 3
            # Then it could go from 100100 to 999999
            for num in range(10 ** (part_len - 1), 10 ** part_len):
                val = 0
                for i in range(0, parts_cnt):
                    val += num * (10 ** (i * part_len))
                    
                if val not in visited_nums:
                    for line in content:
                        if val >= line[0] and val <= line[1]:
                            if parts_cnt == 2:
                                res_a += val
                            res_b += val
                            visited_nums.add(val)
                            break

print(f"Part A: {res_a}")
print(f"Part B: {res_b}")