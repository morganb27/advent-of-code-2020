import fileinput

SEEN = set()
SEATS = (line.strip() for line in fileinput.input())

def highest_seat(seat):
    row_instructions = seat[:-3]
    col_instructions = seat[-3:]
    row_range = [i for i in range(128)]
    col_range = [i for i in range(8)]
    
    for instr in row_instructions:
        if instr == 'F':
            row_range[:] = row_range[:(len(row_range) // 2)]
        elif instr == 'B':
            row_range[:] = row_range[(len(row_range) // 2):]
    
    for instr in col_instructions:
        if instr == 'R':
            col_range[:] = col_range[len(col_range) // 2:]
        elif instr == 'L':
            col_range[:] = col_range[:len(col_range) // 2]
    
    SEEN.add(row_range[0] * 8 + col_range[0])
    return row_range[0] * 8 + col_range[0]

def seat_id():
    sorted_seen = sorted(SEEN)
    for i in range(len(sorted_seen) - 1):
        if sorted_seen[i] + 1 != sorted_seen[i+1]:
            return sorted_seen[i] + 1
    


print(f"The highest seat is: {max(highest_seat(s) for s in SEATS)}")
print(f"Your seat id:", seat_id()) 