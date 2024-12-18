EXPANSION_RATE = 2

def find_galaxies(grid, M, N):
    coords = []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '#':
                coords.append((i, j))
    return coords

def find_expanded_rows(grid, M, N):
    expanded_rows = set()
    for i in range(M):
        count = 0
        for j in range(N):
            count += grid[i][j] == '#'

        if count == 0:
            expanded_rows.add(i)
    return expanded_rows

def find_expanded_cols(grid, M, N):
    expanded_cols = set()
    for j in range(N):
        count = 0
        for i in range(M):
            count += grid[i][j] == '#'

        if count == 0:
            expanded_cols.add(j)
    return expanded_cols

def manhattan_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def solver(file_name):
    grid = []
    with open(file_name, 'r') as f:
        for line in f.read().splitlines():
            grid.append(list(line))
    
    M, N = len(grid), len(grid[0])
    galaxy_coords = find_galaxies(grid, M, N)
    expanded_rows = find_expanded_rows(grid, M, N)
    expanded_cols = find_expanded_cols(grid, M, N)

    sum_distances = 0
    number_of_galaxies = len(galaxy_coords)
    for i, coord1 in enumerate(galaxy_coords):
        for j in range(i + 1, number_of_galaxies):
            coord2 = galaxy_coords[j]
            if coord1 == coord2:
                continue

            distance = manhattan_distance(coord1, coord2)
            for row in expanded_rows:
                if coord1[0] <= row <= coord2[0] or coord2[0] <= row <= coord1[0]:
                    distance += EXPANSION_RATE - 1
            
            for col in expanded_cols:
                if coord1[1] <= col <= coord2[1] or coord2[1] <= col <= coord1[1]:
                    distance += EXPANSION_RATE - 1

            sum_distances += distance
    return sum_distances

if __name__ == "__main__":
    file_name = "input.txt"
    print(solver(file_name))
