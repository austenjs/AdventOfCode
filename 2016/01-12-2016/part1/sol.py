with open('input.txt', 'r') as f:
    instructions = f.read().split(', ')

x, y = 0, 0
direction = (-1, 0) # north

transition = {
    (0, -1): {'L': (1, 0), 'R': (-1, 0)},
    (0, 1): {'L': (-1, 0), 'R': (1, 0)},
    (1, 0): {'L': (0, 1), 'R': (0, -1)},
    (-1, 0): {'L': (0, -1), 'R': (0, 1)}
}

for instruction in instructions:
    toggle = instruction[0]
    steps = int(instruction[1:])
    direction = transition[direction][toggle]
    x += steps * direction[0]
    y += steps * direction[1]
print(abs(x) + abs(y))
