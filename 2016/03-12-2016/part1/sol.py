with open('input.txt', 'r') as f:
    lines = list(map(lambda chunk: chunk.strip(), f.read().splitlines()))

num_possible = 0
for line in lines:
    a, b, c = map(int, line.split())
    if a >= b + c or b >= a + c or c >= a + b: continue
    num_possible += 1
print(num_possible)
