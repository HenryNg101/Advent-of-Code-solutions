import time
from collections import defaultdict, deque
import math
from functools import lru_cache
import sys
sys.setrecursionlimit(100000000)

start_time = time.time()
content = open('input.txt', 'r').read()
content = content.split('\n')

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

def traverse(prev_ch, curr_ch, keypad):
    start_r, start_c, end_r, end_c = -1, -1, -1, -1
    possible_moves = []
    
    for r in range(len(keypad)):
        for c in range(len(keypad[0])):
            if keypad[r][c] == prev_ch:
                start_r, start_c = r, c
            if keypad[r][c] == curr_ch:
                end_r, end_c = r, c
    
    valid_r_direction, valid_c_direction = '', ''
    if start_r < end_r:
        valid_r_direction = 'v'
    if start_r > end_r:
        valid_r_direction = '^'
    if start_c < end_c:
        valid_c_direction = '>'
    if start_c > end_c:
        valid_c_direction = '<'
        
    r_moves_cnt, c_moves_cnt = abs(start_r - end_r), abs(start_c - end_c)
    
    curr_moves = []
    def permutations(r, c, r_moves_cnt, c_moves_cnt):
        # Base cases
        if keypad[r][c] == None:
            return
        if r_moves_cnt == 0 and c_moves_cnt == 0:
            moves = ''.join(curr_moves) + 'A'
            possible_moves.append(moves)
            return

        if r_moves_cnt > 0:
            curr_moves.append(valid_r_direction)
            permutations(r + directions[valid_r_direction][0], c, r_moves_cnt-1, c_moves_cnt)
            curr_moves.pop()
        if c_moves_cnt > 0:
            curr_moves.append(valid_c_direction)
            permutations(r, c + directions[valid_c_direction][1], r_moves_cnt, c_moves_cnt-1)
            curr_moves.pop()
    
    permutations(start_r, start_c, r_moves_cnt, c_moves_cnt)
    return possible_moves

'''Based on the current keyboard'''
def get_code(code, keypad):
    result = traverse('A', code[0], keypad)
    for i in range(1, len(code)):
        possible_moves = traverse(code[i-1], code[i], keypad)
        new_res = []
        for move1 in result:
            for move2 in possible_moves:
                new_res.append(move1 + move2)
        result = new_res
    return result

keypad1 = (('7', '8', '9'), ('4', '5', '6'), ('1', '2', '3'), (None, '0', 'A'))
keypad2 = ((None, '^', 'A'), ('<', 'v', '>'))
res_a = 0
for line in content:
    numeric = int(line[:-1])
    
    result = get_code(line, keypad1)
    print(len(result))
    
    for _ in range(2):
        new_res = []
        for sequence in result:
            for val in get_code(sequence, keypad2):
                new_res.append(val)
        result = new_res
        print(len(result))
    
    print(f'Runtime: {time.time() - start_time} seconds')
    start_time = time.time()
    
    min_len = 10000000000
    for sequence in result:
        min_len = min(min_len, len(sequence))
    res_a += numeric * min_len
    
print(res_a)
print(f'Runtime: {time.time() - start_time} seconds')