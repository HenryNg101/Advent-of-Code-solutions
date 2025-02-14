from inputGetter import get_input

content = get_input(2015, 5).split('\n')[:-1]
total_cnt = 0
forbidden = ['ab','cd','pq','xy']
vowels = ['a','o','i','u','e']

for line in content:
    mp = dict()
    check = True
    check2 = False
    for i in range(len(line)):
        if line[i:i+2] in forbidden:
            check = False
            break
        
        if i < len(line) - 1:
            if line[i] == line[i+1]:
                check2 = True
            
        if line[i] not in mp:
            mp[line[i]] = 0
        mp[line[i]] += 1
    if not (check and check2):
        continue
    
    vowel_cnt = 0
    for c in vowels:
        if c in mp:
            vowel_cnt += mp[c]
    if vowel_cnt < 3:
        continue
    
    total_cnt += 1
print(f'Part A: {total_cnt}')

total_cnt = 0
for line in content:
    check = False
    check2 = False
    mp = dict()

    for i in range(len(line) - 1):
        if line[i:i+2] not in mp:
            mp[line[i:i+2]] = i
        else:
            if i - mp[line[i:i+2]] > 1:
                check = True
        
        if i < len(line) - 2:
            if line[i] == line[i+2]:
                check2 = True

    if check and check2:
        total_cnt += 1

print(f'Part B: {total_cnt}')