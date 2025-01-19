import time
from collections import defaultdict, deque
import math
import queue
from functools import lru_cache
import sys
sys.setrecursionlimit(100000000)

start_time = time.time()
content = open('input.txt', 'r').read()
content = content.split('\n')

line_id = 0

gates_val = dict()
mp = defaultdict(list)
q = queue.Queue()
gates_ops = dict()
indegree = defaultdict(int)

while len(content[line_id]) > 0:
    gate, val = content[line_id].split(': ')
    gates_val[gate] = val == '1'
    line_id += 1

for line in content[line_id+1:]:
    line = line.split()
    mp[line[0]].append(line[-1])
    mp[line[2]].append(line[-1])
    indegree[line[0]] += 0
    indegree[line[2]] += 0
    indegree[line[-1]] += 2
    gates_ops[line[-1]] = line[0:3]

for gate, degree in indegree.items():
    if degree == 0:
        q.put(gate)

while not q.empty():
    q_sz = q.qsize()
    for _ in range(q_sz):
        curr = q.get()
        print(curr, end=' ')
        
        if curr not in gates_val:
            gate1, op, gate2 = gates_ops[curr]
            if op == 'AND':
                gates_val[curr] = gates_val[gate1] and gates_val[gate2]
            elif op == 'OR':
                gates_val[curr] = gates_val[gate1] or gates_val[gate2]
            else:
                gates_val[curr] = gates_val[gate1] ^ gates_val[gate2]
        
        for child_gate in mp[curr]:
            indegree[child_gate] -= 1
            if indegree[child_gate] == 0:
                q.put(child_gate)
        
        # for other_gate, op, res_gate in mp[curr]:
        #     if res_gate not in gates_val:
        #         if op == 'AND':
        #             gates_val[res_gate] = gates_val[curr] and gates_val[other_gate]
        #         elif op == 'OR':
        #             gates_val[res_gate] = gates_val[curr] or gates_val[other_gate]
        #         else:
        #             gates_val[res_gate] = gates_val[curr] ^ gates_val[other_gate]
                
        #         q.put(res_gate)
    print()


z_gate_id = 0
res_a = 0
while True:
    gate_name = str(z_gate_id)
    if len(gate_name) == 1:
        gate_name = '0' + gate_name
    gate_name = 'z' + gate_name
    
    if gate_name not in gates_val:
        break
    
    res_a += gates_val[gate_name] << z_gate_id
    z_gate_id += 1
    
print(res_a)
print(f'Runtime: {time.time() - start_time} seconds')