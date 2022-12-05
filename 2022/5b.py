# The number of spaces for each element in stacks's row (except last stack elements)
n = 4
content = open("input").read().split('\n')

# Stack simulation using 2d list, using list comprehension to avoid references inside elements
st = [[] for _ in range(len(content[0]) // n + 1)]

continue_id = -1
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
for id in range(continue_id, len(content)):
    # Split a line by words, and only take the numbers
    arr = [int(x) for x in content[id].split(' ') if x.isdecimal()]
    if (len(arr) != 3):
        continue

    # 2 stacks trick, to simulate a queue (kinda?? Because we don't always take element from bottom)
    alt_arr = []
    for _ in range(arr[0]):
        alt_arr.append(st[arr[1]-1].pop())
    while len(alt_arr) > 0:
        st[arr[2]-1].append(alt_arr.pop())

res = ""
for e in st:
    res += e[-1]
print(res)
