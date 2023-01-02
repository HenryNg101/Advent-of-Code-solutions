import time

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline

total = 0
for line in content:
    multiplier = 1
    base_10 = 0
    for i in range(len(line)-1, -1, -1):
        val = 0
        if line[i] == '-':
            val = -1
        elif line[i] == '=':
            val = -2
        else:
            val = int(line[i])
        base_10 += val * multiplier
        multiplier *= 5
    total += base_10

#Convert decimal to base 5
base_5 = []
while total > 0:
    base_5.insert(0, str(total % 5))
    total //= 5

#Convert standard base 5 numbers to SNAFU number
spare = 0
for i in range(len(base_5) - 1, -1, -1):
    new_val = int(base_5[i]) + spare
    spare = new_val // 5
    new_val -= spare * 5
    if new_val > 2:
        spare += 1
        if new_val == 3:
            base_5[i] = '='
        else:
            base_5[i] = '-'
    else:
        base_5[i] = str(new_val)
if spare > 0:
    base_5.insert(0, str(spare))

#Get the result
print(*base_5, sep='')

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
