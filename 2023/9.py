import time

# Start the timer
start_time = time.time()
input = [line.strip() for line in open("input").readlines()]
res_a, res_b = 0, 0

for line in input:
    nums = [int(num) for num in line.split()]
    history_sequences = [nums]

    while len(history_sequences[-1]) > 1:
        history_sequences.append([])
        val = None
        same_values = True

        for i in range(1, len(history_sequences[-2])):
            diff = history_sequences[-2][i] - history_sequences[-2][i-1]
            history_sequences[-1].append(diff)
            if val:
                same_values &= (val == diff)
            else:
                val = diff

        if same_values:
            break
    
    for sequence_id, sequence in enumerate(history_sequences):
        res_a += sequence[-1]
        # Part 2 algorithm, add values in even id lines, remove values in odd id lines
        res_b += sequence[0] if sequence_id % 2 == 0 else (0 - sequence[0])

print(f'Part 1: {res_a}')
print(f'Part 2: {res_b}')
print(f'Elapsed time: {time.time() - start_time} seconds')