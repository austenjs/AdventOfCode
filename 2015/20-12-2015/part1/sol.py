import math

with open('input.txt', 'r') as f:
    line = f.read()

target = int(line) // 10

def factor_sum(number):
    ans = 0
    for i in range(1, int(math.sqrt(number))):
        if number % i == 0:
            ans += i
            ans += number // i
    return ans

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
candidates = {1}
limit = target
for i, prime in enumerate(primes):
    new_candidates = set()
    for candidate in candidates:
        mul = candidate
        while mul * prime <= limit:
            mul *= prime
            new_candidates.add(mul)
    candidates = candidates.union(new_candidates)

for num in sorted(candidates):
    total = factor_sum(num)
    if total >= target:
        print(f'House num: ', num)
        break
