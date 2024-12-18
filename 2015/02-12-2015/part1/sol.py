with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    l, w, h = map(eval, line.split('x'))
    lw, wh, hl = l * w, w * h, h * l
    total += 2 * (lw + wh + hl) + min(lw, wh, hl)
print(total)
