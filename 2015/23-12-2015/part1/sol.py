with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

pointer = 0
values = {'a': 0, 'b': 0}
N = len(lines)
while pointer < N:
    command, others = lines[pointer].split(maxsplit=1)
    if command == 'inc':
        values[others] += 1
        pointer += 1
    elif command == 'hlf':
        values[others] /= 2
        pointer += 1
    elif command == 'tpl':
        values[others] *= 3
        pointer += 1
    elif command == 'jmp':
        pointer += int(others)
    elif command == 'jio':
        register, offset = others.split(', ')
        if values[register] !=  1: pointer += 1
        else: pointer += int(offset)
    elif command == 'jie':
        register, offset = others.split(', ')
        if values[register] % 2 != 0: pointer += 1
        else: pointer += int(offset)
print(values)
