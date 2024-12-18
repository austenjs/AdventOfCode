with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


lights = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in lines:
    *command, start_coord, _, end_coord = instruction.split()
    x1, y1 = list(map(eval, start_coord.split(',')))
    x2, y2 = list(map(eval, end_coord.split(',')))

    if len(command) == 1:
        f = lambda x: 1 - x
    elif len(command) == 2 and command[1] == 'on':
        f = lambda x: 1
    elif len(command) == 2 and command[1] == 'off':
        f = lambda x: 0
    
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            lights[i][j] = f(lights[i][j])

print(sum(map(sum, lights)))