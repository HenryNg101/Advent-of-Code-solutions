import time

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline



elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
