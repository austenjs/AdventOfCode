def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
    return solve(times, distances)

def solve(times, distances):
    ans = 1
    for i, time in enumerate(times):
        target = distances[i]
        combinations = 0
        for press in range(1, target):
            reach = press * (time - press)
            if reach > target:
                combinations += 1
        ans *= combinations
    return ans

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
