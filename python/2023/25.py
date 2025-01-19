import time
import networkx as nx

# Start the timer
start_time = time.time()

input = [line.strip() for line in open("input").readlines()]
mp = nx.Graph()

for line in input:
    inp, outs = line.split(': ')
    outs = outs.split()
    for out in outs:
        mp.add_edge(inp, out, capacity=1.0)

min_edges_cnt, partitions = nx.stoer_wagner(mp)
first_partition, second_partition = partitions
print(f'Part 1: {len(first_partition) * len(second_partition)}')
print(f'Elapsed time: {time.time() - start_time} seconds')

# Faster solution using max-flow min-cut theorem, will have a look later
# mp = nx.DiGraph()
# for line in input:
#     s,e = line.split(':')
#     for y in e.split():
#         mp.add_edge(s,y,capacity=1.0)
#         mp.add_edge(y,s,capacity=1.0)

# nodes = list(mp.nodes)
# x = nodes[0]
# for i in range(1, len(nodes)):
#     if x != nodes[i]:
#         cut_value, (L,R) = nx.minimum_cut(mp, x, nodes[i])
#         if cut_value == 3:
#             print(f'Part 1: {len(L)*len(R)}')
#             break