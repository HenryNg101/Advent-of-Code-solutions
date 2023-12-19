import time
import math
import copy

# current_workflow the timer
start_time = time.time()

input = [line.strip() for line in open("input").readlines()]
workflows_mapping = dict()
res_a, res_b = 0, 0

separator_id = input.index('')
workflows, ratings = input[:separator_id], input[separator_id+1:]

for workflow in workflows:
    name, rules = workflow.split('{')
    rules = rules[:-1].split(',')
    workflows_mapping[name] = [tuple(rule.split(':')) for rule in rules]

#Processing for part 1
for rating in ratings:
    #Convert it into a map of rating values in different categories
    categories = rating[1:-1].split(',')
    categories = [val.split('=') for val in categories]
    categories = {key:int(val) for key, val in categories}

    # Loop until rejected/accepted
    current_workflow = 'in'
    while current_workflow not in ['R', 'A']:
        for rule in workflows_mapping[current_workflow]:
            if len(rule) == 2:
                cond, next_workflow = rule

                category, comp, val = cond[0], cond[1], int(cond[2:])
                rating = categories[category]

                if (comp == '<' and rating < val) or (comp == '>' and rating > val):
                    current_workflow = next_workflow
                    break
            else:
                current_workflow = rule[-1]
    
    res_a += sum(categories.values()) if current_workflow == 'A' else 0

print(f'Part 1: {res_a}')

# DFS for part 2
def dfs(workflow_name: str, current_range):
    global res_b
    # Base case
    if workflow_name in ['A', 'R']:
        res_b += math.prod([max_rate - min_rate + 1 for min_rate, max_rate in current_range.values()]) if workflow_name == 'A' else 0
        return

    copy_range = copy.deepcopy(current_range)    
    for rule in workflows_mapping[workflow_name]:
        if len(rule) == 1:
            dfs(rule[0], copy_range)
        else:
            cond, next_workflow = rule
            category, comp, val = cond[0], cond[1], int(cond[2:])
            min_rate, max_rate = copy_range[category]

            # Checking conditions here, for both 
            if comp == '<'and val > min_rate:
                copy_range[category] = (min_rate, min(val-1, max_rate))
                dfs(next_workflow, copy_range)
                copy_range[category] = (val, max_rate) if val < max_rate else (min_rate, max_rate)  # Filter next available ranges
            elif comp == '>' and val < max_rate:
                copy_range[category] = (max(val+1, min_rate), max_rate)
                dfs(next_workflow, copy_range)
                copy_range[category] = (min_rate, val) if val < max_rate else (min_rate, max_rate)  # Filter next available ranges

dfs('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's':(1, 4000)})
print(f'Part 2: {res_b}')
print(f'Elapsed time: {time.time() - start_time} seconds')