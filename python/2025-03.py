from inputGetter import get_input

content = get_input(2025, 3).split('\n')

def max_voltage_output(required_len):
    res = 0
    for line in content:
        max_volt = []       # Basically a monotonic stack, with decreasing order
        for i in range(0, len(line)):
            while max_volt and line[i] > max_volt[-1] and len(max_volt) + len(line) - i > required_len:
                max_volt.pop()
            if len(max_volt) < required_len:
                max_volt.append(line[i])
        
        for j in range(required_len):
            res += (10 ** (required_len - j - 1)) * (ord(max_volt[j]) - ord('0'))
    return res
    
print(f"Part A: {max_voltage_output(2)}")
print(f"Part B: {max_voltage_output(12)}")