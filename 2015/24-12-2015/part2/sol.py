from itertools import combinations

def product(lst):
    ans = 1
    for item in lst:
        ans *= item
    return ans

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

weights = sorted(int(line) for line in lines)

N = len(weights)
total_sum = sum(weights)
assert(total_sum % 4 == 0)
first_compartment = total_sum // 4

min_legroom = 9999
min_quantum_entanglement = 10**20
for i in range(1, N):
    if i > min_legroom: break
    for combination in combinations(weights, i):
        if sum(combination) != first_compartment:
            continue
        min_legroom = i
        min_quantum_entanglement = min(min_quantum_entanglement, product(combination))
print(min_quantum_entanglement)
