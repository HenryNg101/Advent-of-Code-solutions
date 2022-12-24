import time

start_time = time.process_time()
# The number of spaces for each element in stacks's row (except last stack elements)
n = 4
content = open("input").read().split('\n')
content.pop()
continue_id = -1

# Stack simulation using 2d list, using list comprehension
st = [[] for _ in range(len(content[0]) // n + 1)]

# Process the stack input
for id, line in enumerate(content):
    # Breaks when see the part with number from 1 to n, which is the number of stack
    if '1' in line:
        continue_id = id + 1
        break

    # Breaks them down into chunks, then insert into stacks
    processed_line = [(line[i:i+n]).strip() for i in range(0, len(line), n)]
    for st_id, token in enumerate(processed_line):
        if len(token) > 0:
            st[st_id].insert(0, token[1])

# Process the rest
for id in range(continue_id+1, len(content)):
    # Split a line by words, and only take the numbers
    arr = [int(x) for x in content[id].split(' ') if x.isdecimal()]
    for _ in range(arr[0]):
        st[arr[2]-1].append(st[arr[1]-1].pop())

res = "".join([top[-1] for top in st])
print(res)
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")