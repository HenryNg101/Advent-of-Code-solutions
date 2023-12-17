import time

# Start the timer
start_time = time.time()
input = open("input").readlines()

# Store seeds for part 1
seeds = [int(num) for num in input[0].split()[1:]]

# Store ranges for part 2
seed_ranges = [( seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]

id = 3
sz = len(input)
while id < sz:
    changed_arr = [False] * len(seeds)  #Helper list for part 1
    new_ranges = []    #Helper list for part 2

    while id < sz and input[id] != '\n':
        dest, src, r = [int(num) for num in input[id].split()]

        #Part 1 algorithm
        for source_id, number in enumerate(seeds):
            if number >= src and number <= src + r and not changed_arr[source_id]:
                seeds[source_id] = dest + (seeds[source_id] - src)
                changed_arr[source_id] = True

        # Part 2 algorithm
        max_dest, max_src = dest + r - 1, src + r - 1   # Maximum value of destination change, and possible source value
        dist = dest - src  # Distance between source and destination numbers
        sources_cnt = len(seed_ranges)  # Keep the initial size of current ranges, as this list will change

        for _ in range(sources_cnt):
            r_start, r_end = seed_ranges.pop(0)

            # When the init range is completely covered in the conversion range
            if r_start >= src and r_end <= max_src:
                new_ranges.append((r_start + dist, r_end + dist))

            # When the init range completely covers the conversion range
            elif r_start < src and r_end > max_src:
                new_ranges.append((dest, max_dest))
                seed_ranges += [(r_start, src-1), (max_src + 1, r_end)]

            # When two ranges overlap, but only a partial
            elif r_start < src and r_end <= max_src and r_end >= src:
                new_ranges.append((dest, r_end + dist))
                seed_ranges.append((r_start, src - 1))
            
            elif r_start <= max_src and r_start >= src and r_end > max_src:
                new_ranges.append((r_start + dist, max_dest))
                seed_ranges.append((max_src + 1, r_end))

            # When none of the ranges overlap
            else:
                seed_ranges.append((r_start, r_end))

        id += 1

    # Add all of converted ranges, keep the unchange ones unchange (as stated in the question)
    seed_ranges += new_ranges[:]
    id += 2

print(f'Part 1: {min(seeds)}')
print(f'Part 2: {min(seed_ranges)[0]}')
print(f'Elapsed time: {time.time() - start_time} seconds')