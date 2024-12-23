import numpy as np

with open('input.txt', 'r') as f:
    line = f.read()

target = int(line)

BIG_NUM = 1000000
houses = np.zeros(BIG_NUM)
for i in range(1, BIG_NUM):
    houses[i:(i+1)*50:i] += 11 * i

print(np.nonzero(houses > target)[0][0])
