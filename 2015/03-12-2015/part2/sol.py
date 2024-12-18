with open('input.txt', 'r') as f:
    string = f.read()

coords = [(0, 0), (0, 0)]
mapping = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

visited = set()
for i, char in enumerate(string):
    coord = coords[i % 2]
    visited.add(coord)
    x, y = coord
    dx, dy = mapping[char]
    coords[i % 2] = (x + dx, y + dy)
print(len(visited))
