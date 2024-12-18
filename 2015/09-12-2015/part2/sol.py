from itertools import permutations
from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

distances = defaultdict(dict)
names = set()
for line in lines:
    city1, _, city2, _, distance = line.split()
    names.add(city1)
    names.add(city2)
    distance = int(distance)
    distances[city1][city2] = distance
    distances[city2][city1] = distance

N = len(names)
paths = permutations(names)
max_cost = 0
for path in paths:
    cost = 0
    for i in range(N - 1):
        cost += distances[path[i]][path[i + 1]]
    max_cost = max(cost, max_cost)
print(max_cost)
