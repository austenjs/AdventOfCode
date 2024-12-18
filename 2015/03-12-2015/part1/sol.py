with open('input.txt', 'r') as f:
    string = f.read()

coord = (0, 0)
mapping = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

visited = set()
for char in string:
    visited.add(coord)
    x, y = coord
    dx, dy = mapping[char]
    coord = (x + dx, y + dy)
print(len(visited))
