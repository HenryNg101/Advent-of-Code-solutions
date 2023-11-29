content = open("input").read().split("\n")
rows_count = len(content)
cols_count = len(content[0])
total_risk_level = 0

for current_row in range(rows_count):
    for current_column in range(cols_count):
        valid_low_point = True

        next_locations = (
            (current_row - 1, current_column), 
            (current_row + 1, current_column), 
            (current_row, current_column - 1), 
            (current_row, current_column + 1)
        )

        for next_row, next_column in next_locations:
            if next_row < 0 or next_row >= rows_count or next_column < 0 or next_column >= cols_count:
                continue

            valid_low_point &= content[next_row][next_column] > content[current_row][current_column]
        
        if valid_low_point:
            total_risk_level += 1 + int(content[current_row][current_column])

print(total_risk_level)