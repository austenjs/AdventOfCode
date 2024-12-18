def check_nice(string):
    N = len(string)
    # first condition
    appear_twice = False
    seen = {}
    i = 0
    while i < N:
        cur = string[i:i + 2]
        if cur in seen and seen[cur][1] != i:
            appear_twice = True
            break
        if cur not in seen: seen[cur] = [i, i + 1]
        i += 1

    # second condition
    repeat = False
    for i in range(N):
        if i != 0 and i != N - 1 and string[i - 1] == string[i + 1]:
            repeat = True
            break
    return appear_twice and repeat

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

num_nice_strings = 0
for string in lines:
    num_nice_strings += check_nice(string)
print(num_nice_strings)
