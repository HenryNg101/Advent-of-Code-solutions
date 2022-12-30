from ast import List
import time

#Binary tree
class Monkey:
    def __init__(self, 
                    left: str = None, 
                    right: str = None, 
                    val: int = None, 
                    op: str = None,
                    prev: str = None) -> None:
        self.left = left
        self.right = right
        self.val = val
        self.op = op
        self.prev = prev

def traverse(name: str):
    global mp, dependencies
    curr = mp[name]
    val = curr.val
    if val == None:
        left, right, op = curr.left, curr.right, curr.op
        if op == '+':
            val = traverse(left) + traverse(right)
        elif curr.op == '-':
            val = traverse(left) - traverse(right)
        elif curr.op == '*':
            val = traverse(left) * traverse(right)
        else:
            val = traverse(left) // traverse(right)
    if name not in dependencies:
        curr.val = val
    return val

def backtrack(name: str):
    global mp, dependencies
    curr = mp[name]
    if curr.val != None:
        return name == 'humn'
    for node in [curr.left, curr.right]:
        dependencies.append(node)
        if backtrack(node):
            return True
        dependencies.pop()

start_time = time.process_time()
content = open("input").read().split('\n')[:-1]     #Exclude the newline

mp = dict()
for line in content:
    name, op = line.split(': ')
    op = op.split()
    monkey = Monkey()
    if len(op) == 1:
        monkey.val = int(op[0])
    else:
        monkey.left, monkey.op, monkey.right = op
    mp[name] = monkey

dependencies = []   #List from start to end, which is "humn"
backtrack("root")
#print(dependencies)
traverse("root")

root_node = mp['root']
expected_val = mp[root_node.right].val if root_node.left == dependencies[0] else mp[root_node.left].val

for node in dependencies[:-1]:
    node = mp[node]
    left = mp[node.left]
    right = mp[node.right]
    if right.val == None:
        if node.op == '+':
            expected_val -= left.val
        elif node.op == '-':
            expected_val = left.val - expected_val
        elif node.op == '*':
            expected_val //= left.val
        else:
            expected_val = left.val // expected_val
    else:
        if node.op == '+':
            expected_val -= right.val
        elif node.op == '-':
            expected_val += right.val
        elif node.op == '*':
            expected_val //= right.val
        else:
            expected_val *= right.val
print(expected_val)

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
