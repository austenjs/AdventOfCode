BANNED = {
    (0, 1): {'|', 'L', 'F'},
    (0, -1): {'|', '7', 'J'},
    (1, 0): {'-', '7', 'F'},
    (-1, 0): {'-', 'J', 'L'}
}

def find_longest_loop(grid, start, M, N, moves):
    visited = set()
    stack = [(start, 0, None)]
    ans = 0
    while stack:
        coord, step, prev = stack.pop()
        x, y = coord
        symbol = grid[x][y]
        if symbol == 'S':
            if prev:
                ans = max(ans, step // 2)
                continue
        elif coord in visited:
            continue
        elif symbol == '.':
            continue

        visited.add(coord)
        for dx, dy in moves[symbol]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= M:
                continue
            elif new_y < 0 or new_y >= N:
                continue
            elif (new_x, new_y) == prev:
                continue
            
            next_symbol = grid[new_x][new_y]
            if next_symbol in BANNED[(dx, dy)]:
                continue

            stack.append(((new_x, new_y), step + 1, coord))
    return ans

def find_start(grid, M, N):
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'S':
                return (i, j)
    return (-1, -1)

def get_right(x, y, dx, dy, toggle):
    if toggle:
        return x - dx, y - dy
    return x + dx, y + dy

def find_enclosed(grid, cycle_path, M, N):
    cycle_path = set(cycle_path)

    ans = 0
    for i in range(M):
        to_add = False
        for j in range(N):
            if (i, j) in cycle_path and grid[i][j] in {'|', 'L', 'J'}:
                to_add = not to_add

            if grid[i][j] == '.' and to_add:
                ans += 1
                grid[i][j] = 'I'
    for line in grid:
        print(''.join(line))

    return ans

def flood_fill(x, y, grid, M, N, cycle_path):
    if x < 0 or x >= M:
        return 0
    elif y < 0 or y >= N:
        return 0
    elif (x, y) in cycle_path:
        return 0
    elif grid[x][y] != '.':
        return 0

    ans = 1
    grid[x][y] = 'I'
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ans += flood_fill(x + dx, y + dy, grid, M, N, cycle_path)
    return ans

def find_loop_paths(grid, start, M, N, moves):
    visited = set()
    stack = [(start, None)]
    parents = {}

    while stack:
        coord, prev = stack.pop()
        x, y = coord
        symbol = grid[x][y]
        if symbol == 'S':
            if prev: break
        elif coord in visited:
            continue
        elif symbol == '.':
            continue

        visited.add(coord)
        for dx, dy in moves[symbol]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= M:
                continue
            elif new_y < 0 or new_y >= N:
                continue
            elif (new_x, new_y) == prev:
                continue
            
            next_symbol = grid[new_x][new_y]
            if next_symbol in BANNED[(dx, dy)]:
                continue

            parents[(new_x, new_y)] = coord
            stack.append(((new_x, new_y), coord))
    paths = [start]
    coord = parents[start]
    while coord != start:
        paths.append(coord)
        coord = parents[coord]
    return paths

def solver(file_name):
    grid = []
    with open(file_name, 'r') as f:
        for line in f.read().splitlines():
            grid.append(list(line))

    M, N = len(grid), len(grid[0])
    start = find_start(grid, M, N)

    moves = {
        '-' : [(0, 1), (0, -1)],
        '|' : [(1, 0), (-1, 0)],
        'L' : [(-1, 0), (0, 1)],
        'J' : [(-1, 0), (0, -1)],
        '7' : [(1, 0), (0, -1)],
        'F' : [(1, 0), (0, 1)]
    }
    best_pipe = ''
    max_length = 0
    possible_S = list(moves.items())

    for pipe, move in possible_S:
        moves['S'] = [move[0]]
        cur = find_longest_loop(grid, start, M, N, moves)
        if cur > max_length:
            best_pipe, max_length = pipe, cur

    moves['S'] = [moves[best_pipe][0]]
    cycle_path = find_loop_paths(grid, start, M, N, moves)
    for i in range(M):
        for j in range(N):
            if (i, j) in cycle_path:
                continue
            elif (i, j) == start:
                grid[i][j] = best_pipe
                continue
            grid[i][j] = '.'
    
    return find_enclosed(grid, cycle_path, M, N)

if __name__ == "__main__":
    file_name = 'input.txt'
    print(solver(file_name))
