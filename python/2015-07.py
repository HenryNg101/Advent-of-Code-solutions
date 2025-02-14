from ast import List
from inputGetter import get_input

'''Part A'''
content = get_input(2015, 7).split('\n')

mp = dict()     #The dependency graph
indegrees = dict()
q = []
val_mp = dict()

def check_exp(exp: List, variables: List):
    global mp
    level = 0
    for i in variables:
        if not exp[i].isnumeric():
            if exp[i] not in mp:
                mp[exp[i]] = []
            level += 1
            mp[exp[i]].append(var)
        else:
            exp[i] = int(exp[i])
    return exp, level

for line in content:
    line = line.split()
    var = line[-1]
    exp = line[:-2]
    level = 0
    
    if len(exp) == 1:
        exp, level = check_exp(exp, [0])
    
    elif len(exp) == 2:
        exp, level = check_exp(exp, [1])
    
    else:
        exp, level = check_exp(exp, [0, 2])
        
    #Put nodes into stack, ready for Kahn algorithm
    indegrees[var] = level
    if indegrees[var] == 0:
        q.append(var)
    val_mp[var] = exp

while len(q) > 0:
    curr = q[-1]
    q.pop()
    
    if curr in mp:
        for child in mp[curr]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                q.append(child)
    
    exp = val_mp[curr]
    cal_res = -1
    if len(exp) == 1:
        cal_res = exp[0]
        if str(type(cal_res))[-5:-2] == 'str':
            cal_res = val_mp[cal_res]
    
    elif len(exp) == 2:
        cal_res = exp[1]
        if str(type(cal_res))[-5:-2] == 'str':
            cal_res = val_mp[cal_res]
        cal_res ^= 65535
    
    else:
        cal_res = exp[0]
        if str(type(cal_res))[-5:-2] == 'str':
            cal_res = val_mp[cal_res]
        if str(type(exp[2]))[-5:-2] == 'str':
            exp[2] = val_mp[exp[2]]
        
        if exp[1] == 'AND':
            cal_res &= exp[2]
        elif exp[1] == 'OR':
            cal_res |= exp[2]
        elif exp[1] == 'LSHIFT':
            cal_res <<= exp[2]
        else:
            cal_res >>= exp[2]
    
    val_mp[curr] = cal_res

starter_b = val_mp['a']
print(f"Part A: {val_mp['a']}")


'''Part B'''
content = get_input(2015, 7).split('\n')

mp = dict()     #The dependency graph
indegrees = dict()
q = []
val_mp = dict()

for line in content:
    line = line.split()
    var = line[-1]
    exp = line[:-2]
    level = 0
    
    if len(exp) == 1:
        exp, level = check_exp(exp, [0])
    
    elif len(exp) == 2:
        exp, level = check_exp(exp, [1])
    
    else:
        exp, level = check_exp(exp, [0, 2])
        
    #Put nodes into stack, ready for Kahn algorithm
    indegrees[var] = level
    if indegrees[var] == 0:
        q.append(var)
    val_mp[var] = exp

val_mp['b'] = [starter_b]

#Kahn algorithm
while len(q) > 0:
    curr = q[-1]
    q.pop()
    
    if curr in mp:
        for child in mp[curr]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                q.append(child)
    
    exp = val_mp[curr]
    cal_res = -1
    if len(exp) == 1:
        cal_res = exp[0]
        if str(type(cal_res))[-5:-2] == 'str':
            cal_res = val_mp[cal_res]
    
    elif len(exp) == 2:
        cal_res = exp[1]
        if str(type(cal_res))[-5:-2] == 'str':
            cal_res = val_mp[cal_res]
        cal_res ^= 65535
    
    else:
        cal_res = exp[0]
        if str(type(cal_res))[-5:-2] == 'str':
            cal_res = val_mp[cal_res]
        if str(type(exp[2]))[-5:-2] == 'str':
            exp[2] = val_mp[exp[2]]
        
        if exp[1] == 'AND':
            cal_res &= exp[2]
        elif exp[1] == 'OR':
            cal_res |= exp[2]
        elif exp[1] == 'LSHIFT':
            cal_res <<= exp[2]
        else:
            cal_res >>= exp[2]
    
    val_mp[curr] = cal_res

print(f"Part B: {val_mp['a']}")