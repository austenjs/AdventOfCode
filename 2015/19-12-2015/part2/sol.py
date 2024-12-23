from random import shuffle

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

transformations = []
for line in lines[:-2]:
    after, before = line.split(' => ')
    if before in transformations: raise Exception()
    transformations.append((before, after))

# greedy
start = lines[-1]
while True:
    shuffle(transformations)
    molecule = prev = start
    C = 0
    found = False
    while True:
        prev = molecule
        if molecule == 'e':
            found = True
            break
        for before, after in transformations:
            if before not in molecule:
                continue
            C += molecule.count(before)
            molecule = molecule.replace(before, after)
            break

        # cannot find
        if molecule == prev:
            break
    if found: break
print(C)
