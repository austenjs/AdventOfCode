with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

with open('keyboard.txt', 'r') as f:
    keyboard = list(map(lambda line: line.split(','), f.read().splitlines()))

codes = []
x, y = 2, 0

dxdy = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

for line in lines:
    for instruct in line:
        dx, dy = dxdy[instruct]
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_x >= 5: continue
        if new_y < 0 or new_y >= 5: continue
        if keyboard[new_x][new_y] == ' ': continue
        x, y = new_x, new_y
    codes.append(keyboard[x][y])
print(''.join(map(str, codes)))
