class Monkey:
    def __init__(self) -> None:
        self.items = []
        self.div = 0        #Test divisible by n
        self.next = [-1, -1]    #Next moves, first one is true, second one is false
        self.count = 0      #Number of times a monkey inspect an item

        self.factor = -1
        self.sign = ''

    def calc(self):
        self.count += 1
        val = self.items[0]
        self.items.pop(0)
        if self.factor == 'old':
            val *= val
        elif self.sign == '*':
            val *= int(self.factor)
        else:
            val += int(self.factor)
        val //= 3
        return val

content = open("input").read().split('\n')

"""Input handling"""
id = 0
monkeys = []
while id < len(content):
    monkey = Monkey()
    id += 1     #Skip first line, which is the "Monkey n"

    """Handling items"""
    for it in content[id].split():
        if it.isnumeric():
            monkey.items.append(int(it))
        elif it[:-1].isnumeric(): 
            monkey.items.append(int(it[:-1]))
    id += 1

    """Handling operation"""
    monkey.sign, monkey.factor = content[id].split()[-2:]
    #print(f'{monkey.sign} {monkey.factor}')
    id += 1

    """Handling test"""
    monkey.div = int(content[id].split()[-1])
    monkey.next = [int(content[id].split()[-1]) for id in range(id+1, id+3)]
    monkeys.append(monkey)
    id += 4     #Skip last line, which is the white space and the prev 3 lines too

monkeys = [monkey for monkey in monkeys]

"""Actual calculation"""
for _ in range(20):
    for id in range(len(monkeys)):
        while len(monkeys[id].items) > 0:
            new_it = monkeys[id].calc()
            next_id = monkeys[id].next[0] if new_it % monkeys[id].div == 0 else monkeys[id].next[1]
            monkeys[next_id].items.append(new_it)

monkeys.sort(key=lambda x: x.count, reverse=True)
print(monkeys[0].count * monkeys[1].count)