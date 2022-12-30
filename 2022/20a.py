import time

start_time = time.process_time()
content = open("input").read().split()[:-1]     #Exclude the newline

count = 0
ls = [int(line) for line in content]
new_ls = [0] * len(ls)
for elem in ls:
    pass

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
