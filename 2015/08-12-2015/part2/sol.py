from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    total -= len(line)
    
    chars = 0
    for i, char in enumerate(line):
        if char in ["\"", "'", '\\']:
            chars += 1
        chars += 1
    
    total += chars + 2
print(total)
