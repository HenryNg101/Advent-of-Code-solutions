# Template
content = open("input").read().split('\n')
content.pop()

def check_position(row_H: int, col_H: int, row_T: int, col_T: int):
    global visited
    pass

visited = [[False for _ in range(1000)] for _ in range(1000)]
row_H = 500
col_H = 500
row_T = 500
col_T = 500

for line in content:
    direction, moves = line.split(' ')
    moves = int(moves)

    if direction == 'U':
        for _ in range(moves):
            row_H -= 1

    elif direction == 'D':
        for _ in range(moves):
            row_H += 1

    elif direction == 'L':
        for _ in range(moves):
            col_H -= 1

    elif direction == 'R':
        for _ in range(moves):
            col_H += 1