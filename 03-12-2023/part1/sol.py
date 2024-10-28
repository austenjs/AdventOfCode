from collections import defaultdict
import string


def solver(file_name):
    with open(file_name, 'r') as f:
        grid = f.read().splitlines()

    M, N = len(grid), len(grid[0])
    symbols = get_symbols(grid)
    ans = 0
    for i in range(len(grid)):
        j = 0
        while j < N:
            if grid[i][j] < '0' or grid[i][j] > '9':
                j += 1
                continue
            
            start = j
            while j < N and '0' <= grid[i][j] <= '9':
                j += 1

            exist_symbol = False
            for x in range(i - 1, i + 2):
                if exist_symbol:
                    break
                if x < 0 or x >= M:
                    continue
                if x not in symbols:
                    continue

                for y in range(start - 1, j + 1):
                    if y < 0 or y >= N:
                        continue

                    if y in symbols[x]:
                        exist_symbol = True
                        break

            if exist_symbol:
                ans += int(grid[i][start:j])
    return ans

def get_symbols(grid):
    symbols = defaultdict(set)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                continue
            elif grid[i][j] not in string.punctuation:
                continue
            symbols[i].add(j)
    return symbols

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
