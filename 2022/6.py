import time

start_time = time.process_time()
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
elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
