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

N = len(gains)
perms = permutations(gains.keys())
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
