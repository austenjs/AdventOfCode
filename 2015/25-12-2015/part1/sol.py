code = 20151125
MULTIPLIER_CONST = 252533
REMAINDER_CONSTANT = 33554393

target_x, target_y = 2978 - 1, 3083 - 1 # 0-based indices
x, y = 0, 0
N = 1

while x != target_x or y != target_y:
    code *= MULTIPLIER_CONST
    code %= REMAINDER_CONSTANT

    if x == 0:
        x = N
        y = 0
        N += 1
    else:
        x -= 1
        y += 1
print(code)
