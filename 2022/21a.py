import time

#Binary tree
class Monkey:
    def __init__(self, 
                    left: str = None, 
                    right: str = None, 
                    val: int = None, 
                    op: str = None) -> None:
        self.left = left
        self.right = right
        self.val = val
        self.op = op

def traverse(name: str):
    global mp
    curr_monkey = mp[name]
    if curr_monkey.val != None:
        return curr_monkey.val
    else:
        left, right, op = curr_monkey.left, curr_monkey.right, curr_monkey.op
        if op == '+':
            return traverse(left) + traverse(right)
        elif curr_monkey.op == '-':
            return traverse(left) - traverse(right)
        elif curr_monkey.op == '*':
            return traverse(left) * traverse(right)
        else:
            return traverse(left) // traverse(right)

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

print(traverse("root"))

elapsed_time = (time.process_time() - start_time)
print(f"Elapsed time: {elapsed_time * 1000} ms, {elapsed_time} seconds")
