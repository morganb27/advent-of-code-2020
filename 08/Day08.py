import fileinput

INSTRUCTIONS = [line.strip() for line in fileinput.input()]

def accumulator(data):
    res, i = 0, 0
    indices = set()
    while i < len(data):
        if i in indices:
            return res
        indices.add(i)
        a, b = data[i].split(' ')
        if a == 'nop':
            i+=1
        elif a == 'acc':
            res += int(b)
            i+=1
        elif a == 'jmp':
            i +=int(b)
    return res

def run_script(data):
    res, i = 0, 0
    indices = set()
    while i < len(data):
        if i in indices:
            return None
        indices.add(i)
        a, b = data[i].split(' ')
        if a == 'nop':
            i+=1
        elif a == 'acc':
            res += int(b)
            i+=1
        elif a == 'jmp':
            i +=int(b)
    return res

def fix_script(data):
    res, i = 0, 0
    indices = set()
    while i < len(data):
        if i in indices:
            a, b = data[i].split(' ')
            modified_data = data[:]
            if a == 'nop':
                modified_data[i] = 'jmp' + ' ' + b
            elif a == 'jmp':
                modified_data[i] = 'nop' + ' ' + b
            result = run_script(modified_data)
            if result:
                return result
        indices.add(i)
        a, b = data[i].split(' ')
        if a == 'nop':
            i+=1
        elif a == 'acc':
            res += int(b)
            i+=1
        elif a == 'jmp':
            i +=int(b)
    return -1




print(accumulator(INSTRUCTIONS))
print(fix_script(INSTRUCTIONS))