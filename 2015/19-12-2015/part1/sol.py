from collections import defaultdict

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

transformations = defaultdict(list)
for line in lines[:-2]:
    before, after = line.split(' => ')
    transformations[before].append(after)

new_molecules = set()
molecule = lines[-1]

for key, transformations in transformations.items():
    for index in find_all(molecule, key):
        for transformation in transformations:
            new_molecules.add(molecule[:index] + transformation + molecule[index + len(key):])

print(len(new_molecules))
