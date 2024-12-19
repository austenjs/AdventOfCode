with open('input.txt', 'r') as f:
    string = f.read()

total = 0
cur = []
for char in string:
    if char == '-':
        cur.append(char)
    elif char.isnumeric():
        cur.append(char)
    else:
        if cur:
            num = int(''.join(cur))
            total += num
            cur.clear()
print(total)
