with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

constraint = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for line in lines:
    _, components = line.split(': ', maxsplit=1)

    components = components.split(', ')
    valid = True
    for component in components:
        key, value = component.split(': ')
        value = int(value)
        if constraint[key] != value:
            valid = False
            break

    if valid:
        print(line)
