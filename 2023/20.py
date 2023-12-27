import math, sys, time
from collections import defaultdict

# Start the timer
start_time = time.time()

input = [line.strip() for line in open("input").readlines()]

output_mapping = defaultdict(list)  # Output modules
conjunctions_inputs = dict()    # Input modules of a conjunction module
flipflop_modules_status = dict()    # Status of flipflop modules (on or off)

# Processing input
for line in input:
    module_name, next_modules = line.split(' -> ')
    next_modules = next_modules.split(', ')

    if module_name[0] in ['%', '&']:
        type = module_name[0]
        module_name = module_name[1:]
        if type == '&':
            conjunctions_inputs[module_name] = dict()
        if type == '%':
            flipflop_modules_status[module_name] = 0    # 0 represents off, 1 represents on

    output_mapping[module_name] = next_modules

# Mapping inputs of conjuntion modules in
for inp, outs in output_mapping.items():
    # This is the final module before the rx module.
    # It's seen in the pattern of the input that, this is a conjuntion module
    if 'rx' in outs:
        final_module = inp

    for out in outs:
        if out in conjunctions_inputs:
            conjunctions_inputs[out][inp] = 0   # 0 represents low, 1 represents high.

final_inputs_count = []
low_pulses_cnt, high_pulses_cnt = 0, 0

# Actual processing
for cycle in range(1, 10 ** 8):
    q = [('button', 'broadcaster', 0)]  #Contains information of received pulse, and receiver name
    while q:
        input_name, module_name, pulse = q.pop(0)

        '''
        Part 2 algorithm. The reasoning here is that, through observation in the input, we can see that, there is always 
        one conjuntion module sends output to the rx module, and, all of the input modules for this conjuntion module 
        also all are conjuntion modules.
        
        Since the conjuntion module connects directly to rx needs all high pulses input sent to this module at the same time,
        because, even though conjuntion module remembers the latest input pulse for each input, there will always be pulses 
        sent to this conjuntion module from every input, since all inputs are conjuntion modules too. This means that, just 
        find the amount of cycles it takes for each of these input get a low pulse from one of their inputs.

        This means that, it seems to be, there's a pattern that's cycling around to this, but I couldn't prove this yet. But 
        if it works, it works.
        '''
        if pulse == 0 and module_name in conjunctions_inputs[final_module]:
            final_inputs_count.append(cycle)

            if len(final_inputs_count) == len(conjunctions_inputs[final_module]):
                print(f'Part 2: {math.lcm(*final_inputs_count)}')
                print(f'Elapsed time: {time.time() - start_time} seconds')
                sys.exit(0)

        # The actual logic of updating and sending pulses.
        # This logics decide whether to send pulse or not, and if send pulse, what pulse
        if module_name in flipflop_modules_status:
            if pulse == 1:
                continue
        
            pulse = int(not flipflop_modules_status[module_name])
            flipflop_modules_status[module_name] = pulse

        elif module_name in conjunctions_inputs:
            conjunctions_inputs[module_name][input_name] = pulse
            inputs_status = list(conjunctions_inputs[module_name].values())
            # Decide low or high pulse when all input are low or high pulse
            pulse = inputs_status.count(1) != len(inputs_status)

        for module in output_mapping[module_name]:
            q.append((module_name, module, pulse))
        
        # Part 1 algorithm
        low_pulses_cnt += (pulse == 0)
        high_pulses_cnt += int(pulse == 1)

    if cycle == 1000:
        print(f'Part 1: {low_pulses_cnt * high_pulses_cnt}')