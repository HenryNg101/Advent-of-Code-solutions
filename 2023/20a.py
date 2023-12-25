import time

# Start the timer
start_time = time.time()

input = [line.strip() for line in open("input").readlines()]

'''In this one, let's consider low pulse's value is 0, and high pulse's value is 1'''

low_pulses_cnt, high_pulses_cnt = 0, 0

broadcast = []
flipflops_nexts = dict()
conjunctions_nexts = dict()
conjunctions_inputs = dict()
flipflop_modules_status = dict()

for line in input:
    module_name, next_modules = line.split(' -> ')
    next_modules = next_modules.split(', ')

    if module_name == 'broadcaster':
        broadcast = next_modules
    else:
        type = module_name[0]
        module_name = module_name[1:]
        if type == '%':
            flipflops_nexts[module_name] = next_modules
            flipflop_modules_status[module_name] = 0
        else:
            conjunctions_nexts[module_name] = next_modules
            conjunctions_inputs[module_name] = dict()

for line in input:
    module_name, next_modules = line.split(' -> ')
    next_modules = next_modules.split(', ')
    module_name = module_name[1:] if module_name != 'broadcaster' else module_name

    for conjunction in conjunctions_nexts.keys():
        if conjunction in next_modules:
            conjunctions_inputs[conjunction][module_name] = 0

for _ in range(1000):
    q = []
    q.append(('button', 'broadcaster', 0))    #Contains information of received pulse, and receiver name

    while len(q) > 0:
        input_name, module_name, pulse = q.pop(0)
        # print(f'{input_name}-{pulse}->{module_name}')
        if pulse == 0:
            low_pulses_cnt += 1
        else:
            high_pulses_cnt += 1


        if module_name == 'broadcaster':
            for module in broadcast:
                if module in flipflops_nexts:
                    q.append((module_name, module, pulse))

        elif module_name in flipflops_nexts:
            if pulse == 1:
                continue

            flipflop_modules_status[module_name] = int(not flipflop_modules_status[module_name])
            for module in flipflops_nexts[module_name]:
                q.append((module_name, module, flipflop_modules_status[module_name]))

        elif module_name in conjunctions_nexts:
            conjunctions_inputs[module_name][input_name] = pulse
            inputs_status = list(conjunctions_inputs[module_name].values())

            if inputs_status.count(1) == len(inputs_status):
                for module in conjunctions_nexts[module_name]:
                    q.append((module_name, module, 0))
            else:
                for module in conjunctions_nexts[module_name]:
                    q.append((module_name, module, 1))

print(f'Part 1: {low_pulses_cnt * high_pulses_cnt}')
print(f'Elapsed time: {time.time() - start_time} seconds')