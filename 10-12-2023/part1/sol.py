BANNED = {
    (0, 1): {'|', 'L', 'F'},
    (0, -1): {'|', '7', 'J'},
    (1, 0): {'-', '7', 'F'},
    (-1, 0): {'-', 'J', 'L'}
}

def solver(file_name):
    with open(file_name, 'r') as f:
        grid = f.read().splitlines()

    M, N = len(grid), len(grid[0])
    start = find_start(grid, M, N)

    ans = 0
    moves = {
        '-' : [(0, 1), (0, -1)],
        '|' : [(1, 0), (-1, 0)],
        'L' : [(-1, 0), (0, 1)],
        'J' : [(-1, 0), (0, -1)],
        '7' : [(1, 0), (0, -1)],
        'F' : [(1, 0), (0, 1)]
    }
    possible_S = list(moves.values())
    for move in possible_S:
        moves['S'] = [move[0]]
        ans = max(ans, find_longest_loop(grid, start, M, N, moves))
    return ans

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

if __name__ == "__main__":
    file_name = 'input.txt'
    print(solver(file_name))
