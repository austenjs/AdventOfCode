from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    total += len(line)
    
    i = 1
    N = len(line)
    chars = 0
    while i < N - 1:
        chars += 1
        if line[i] == '\\':
            if line[i + 1] == 'x':
                i += 4
            else:
                i += 2
        else:
            i += 1
    
    total -= chars
print(total)
