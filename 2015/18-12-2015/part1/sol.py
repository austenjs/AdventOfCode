def simulation(matrix):
    M, N = len(matrix), len(matrix[0])
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]

    new_matrix = [['.' for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            num_on_neighbors = 0
            for di, dj in neighbors:
                neigh_i, neigh_j = i + di, j + dj
                if neigh_i < 0 or neigh_i >= M:
                    continue
                if neigh_j < 0 or neigh_j >= N:
                    continue
                num_on_neighbors += (matrix[neigh_i][neigh_j] == '#')
            
            if matrix[i][j] == '#' and 2 <= num_on_neighbors <= 3:
                new_matrix[i][j] = '#'
            elif matrix[i][j] == '.' and num_on_neighbors == 3:
                new_matrix[i][j] = '#'
    return new_matrix

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

matrix = [list(line) for line in lines]
for _ in range(100):
    matrix = simulation(matrix)

total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        total += (matrix[i][j] == '#')
print(total)
