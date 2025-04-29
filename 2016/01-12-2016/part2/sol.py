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

visited = set()
found = False
for instruction in instructions:
    visited.add((x, y))
    toggle = instruction[0]
    steps = int(instruction[1:])

    direction = transition[direction][toggle]
    dx, dy = direction
    for _ in range(steps):
        x += dx
        y += dy
        if (x, y) in visited:
            found = True
            break
        visited.add((x, y))
    if found:
        break
print(abs(x) + abs(y))
