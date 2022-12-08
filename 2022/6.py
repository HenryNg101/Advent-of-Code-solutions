def findStartOfPacket(sz: int):
    global content
    # Sliding window, until found the one that satisfy the condition
    for i in range(sz-1, len(content)):
        # Set to count unique chars in substring
        if len(set(content[ i-sz+1 : i+1 ])) == sz:
            return i + 1

content = open("input").read().rstrip('\n')
print(f'Part A solution is: {findStartOfPacket(4)}')
print(f'Part B solution is: {findStartOfPacket(14)}')