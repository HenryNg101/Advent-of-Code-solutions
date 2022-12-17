from functools import cmp_to_key

"""
Create a list from string
"""
def create_list(ls: str, id: int = 0):
    new_ls = []
    if len(ls) == 0:
        return new_ls, id
    val = 0
    while id < len(ls):
        if ls[id] == '[':
            child_ls, new_id = create_list(ls, id + 1)
            new_ls.append(child_ls)
            id = new_id

        elif ls[id] == ']':
            if ls[id-1].isnumeric():
                new_ls.append(val)
            return new_ls, id

        elif ls[id] == ',':
            if ls[id-1].isnumeric():
                new_ls.append(val)
            val = 0

        else:
            val = val * 10 + int(ls[id])

        id += 1

    if ls[-1].isnumeric():
        new_ls.append(val)
        val = 0
    return new_ls, id


"""
A comparator for 2 lists
Returns:
    -1 if left list is greater than right list
    1 if right list is greater than left list
    0 if both are equal
"""
def compare_ls(left, right):
    id = 0
    while (True):
        if id >= len(left) or id >= len(right):
            if len(left) > len(right):
                return -1
            return int(len(left) < len(right))

        # Type checking
        type_l = str(type(left[id]))
        type_r = str(type(right[id]))

        if type_l == type_r:
            if type_l == "<class 'int'>":
                if left[id] > right[id]:
                    return -1
                elif left[id] < right[id]:
                    return 1
            else:
                check_val = compare_ls(left[id], right[id])
                if check_val != 0:
                    return check_val

        else:
            child_l = list([left[id]]) if type_l == "<class 'int'>" else list(left[id])
            child_r = list([right[id]]) if type_r == "<class 'int'>" else list(right[id])

            check_val = compare_ls(child_l, child_r)
            if check_val != 0:
                return check_val

        id += 1


content = open("input").read().split('\n')
res_A = 0
res_B = [[[2]], [[6]]]

for i in range(0, len(content), 3):
    left = create_list(content[i][1:-1])[0]
    right = create_list(content[i+1][1:-1])[0]
    res_B.extend([left, right])

    if compare_ls(left, right) == 1:
        res_A += i // 3 + 1

res_B.sort(key=cmp_to_key(compare_ls), reverse=True)

print(f'Part A answer is: {res_A}')
print(f'Part B answer is: {(res_B.index([[2]]) + 1) * (res_B.index([[6]]) + 1)}')
