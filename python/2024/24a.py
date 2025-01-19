import time
from collections import defaultdict, deque
import math
from functools import lru_cache
import sys
sys.setrecursionlimit(100000000)

start_time = time.time()
content = open('input.txt', 'r').read()
content = content.split('\n')

line_id = 0

gates_val = dict()
mp = defaultdict(list)
gates_ops = dict()
gates = set()

while len(content[line_id]) > 0:
    gate, val = content[line_id].split(': ')
    gates_val[gate] = val == '1'
    line_id += 1

for line in content[line_id+1:]:
    line = line.split()
    gates.add(line[0])
    gates.add(line[2])
    gates.add(line[-1])
    # mp[line[0]].append(line[-1])
    # mp[line[2]].append(line[-1])
    gates_ops[line[-1]] = line[0:3]

def dfs(gate: str):
    global gates_val, gates_ops
    
    gate1, op, gate2 = gates_ops[gate]
    if gate1[0] == 'x' or gate1[0] == 'y':
        print(gate1, end= ' ')
    if gate2[0] == 'x' or gate2[0] == 'y':
        print(gate2, end= ' ')
    
    if gate1 not in gates_val:
        dfs(gate1)
    if gate2 not in gates_val:
        dfs(gate2)
        
    if op == 'AND':
        gates_val[gate] = gates_val[gate1] and gates_val[gate2]
    elif op == 'OR':
        gates_val[gate] = gates_val[gate1] or gates_val[gate2]
    else:
        gates_val[gate] = gates_val[gate1] ^ gates_val[gate2]

z_gate_id = 0
res_a = 0
while True:
    gate_name = str(z_gate_id)
    if len(gate_name) == 1:
        gate_name = '0' + gate_name
    gate_name = 'z' + gate_name
    
    if gate_name not in gates_ops:
        break
    
    print(f'{gate_name}:', end=' ')
    dfs(gate_name)
    print()
    
    res_a += gates_val[gate_name] << z_gate_id
    z_gate_id += 1

print(len(gates))
print(res_a)
print(gates_val['hnm'])
print(f'Runtime: {time.time() - start_time} seconds')