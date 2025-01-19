content = open('input.txt', 'r').read()
content = content.split('\n')

program = content[-1].split()[-1]
program = [int(val) for val in program.split(',')]

print("Steps")
for i in range(0, len(program), 2):
    opcode, literal = program[i: i+2]
    
    comb = literal
    if comb == 4:
        comb = 'register_a'
    elif comb == 5:
        comb = 'register_b'
    elif comb == 6:
        comb = 'register_c'

    print('- ', end='')
        
    if opcode == 0:
        print(f'register_a = register_a >> {comb}')
    elif opcode == 1:
        print(f'register_b = register_b ^ {literal}')
    elif opcode == 2:
        print(f'register_b = {comb} % 8')
    elif opcode == 3:
        print(f'Loop back if register_a > 0')
    elif opcode == 4:
        print(f'register_b = register_b ^ register_c')
    elif opcode == 5:
        print(f'Output the {comb} % 8')
    elif opcode == 6:
        print(f'register_b = register_a >> {comb}')
    else:
        print(f'register_c = register_a >> {comb}')