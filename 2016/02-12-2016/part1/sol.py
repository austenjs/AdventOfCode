with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

codes = []
cur = 5
for line in lines:
    for instruct in line:
        if instruct == 'U':
            if cur <= 3: continue
            cur -= 3
        elif instruct == 'D':
            if cur >= 7: continue
            cur += 3
        elif instruct == 'L':
            if cur in {1, 4, 7}: continue
            cur -= 1
        elif instruct == 'R':
            if cur in {3, 6, 9}: continue
            cur += 1
    codes.append(cur)
print(''.join(map(str, codes)))
