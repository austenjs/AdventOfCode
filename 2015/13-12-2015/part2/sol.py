from collections import defaultdict
from itertools import permutations

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

gains = defaultdict(dict)

for line in lines:
    key, _, command, value, *_, target = line.split()
    target = target[:-1]
    if command == 'gain':
        gains[key][target] = int(value)
    elif command == 'lose':
        gains[key][target] = -int(value)
    else:
        raise Exception

people = list(gains.keys())
N = len(people)
# adding myself
for person in people:
    gains[person]['me'] = 0
    gains['me'][person] = 0
people.append('me')
N += 1

perms = permutations(people)
max_gain = 0
for perm in perms:
    total_gain = 0
    for i, key in enumerate(perm):
        left = i - 1 if i > 0 else N - 1
        right = i + 1 if i < N - 1 else 0
        total_gain += gains[key][perm[left]]
        total_gain += gains[key][perm[right]]
    max_gain = max(max_gain, total_gain)
print(max_gain)
