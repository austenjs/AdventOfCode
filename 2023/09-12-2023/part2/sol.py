def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    ans = 0
    for line in lines:
        input = list(map(int, reversed(line.split())))
        ans += find_extrapolation(input)
    return ans

def find_extrapolation(numbers):
    diff = []
    for i in range(1, len(numbers)):
        diff.append(numbers[i] - numbers[i - 1])
    
    if len(set(diff)) == 1:
        return numbers[-1] + diff[-1]
    return numbers[-1] + find_extrapolation(diff)

if __name__ == "__main__":
    file_name = "input.txt"
    print(solver(file_name))
