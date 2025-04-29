with open('input.txt', 'r') as f:
    matrix = list(map(lambda chunk: chunk.strip().split(), f.read().splitlines()))

i, j = 0, 0
M, N = len(matrix), len(matrix[0])
num_possible = 0
while j < N:
    a = int(matrix[i][j])
    b = int(matrix[i + 1][j])
    c = int(matrix[i + 2][j])
    if a >= b + c or b >= a + c or c >= a + b: 
        pass
    else:
        num_possible += 1

    i += 3
    if i >= M:
        i = 0
        j += 1
print(num_possible)
