import time

# Start the timer
start_time = time.time()

def calculate_hash(orginal_str: str):
    hash_val = 0
    for char in orginal_str:
        hash_val += ord(char)
        hash_val *= 17
        hash_val %= 256
    return hash_val

input = open("input").readline().strip().split(',')
res_a, res_b = 0, 0
boxes = [[] for _ in range(256)]

for org in input:
    # Get result for part 1
    res_a += calculate_hash(org)

    operation_id = org.find('=') if '=' in org else org.find('-')
    label = org[:operation_id]
    boxes_id = calculate_hash(label)

    # Adding or changing
    if org[operation_id] == '=':
        focal_length = int(org[operation_id+1:])
        
        replace_id = 0
        while replace_id < len(boxes[boxes_id]) and boxes[boxes_id][replace_id][0] != label:
            replace_id += 1
        
        if replace_id == len(boxes[boxes_id]):
            boxes[boxes_id].append((label, focal_length))
        else:
            boxes[boxes_id][replace_id] = (label, focal_length)
    
    # Deleting operation
    else:
        delete_id = 0
        while delete_id < len(boxes[boxes_id]) and boxes[boxes_id][delete_id][0] != label:
            delete_id += 1
        
        if delete_id < len(boxes[boxes_id]):
            boxes[boxes_id].pop(delete_id)

for operation_id, box in enumerate(boxes):
    for item_id, item in enumerate(box):
        res_b += (operation_id + 1) * (item_id + 1) * item[1]

print(f'Part 1: {res_a}')
print(f'Part 2: {res_b}')
print(f'Elapsed time: {time.time() - start_time} seconds')