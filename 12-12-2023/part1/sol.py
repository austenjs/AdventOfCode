def generate(raw_spring, max_broken):
    allow_change = max_broken - sum((char == '#' for char in raw_spring))

    N = len(raw_spring)
    ans = []
    to_modify = list(raw_spring)

    def backtrack(cur, allow_change, to_modify):
        if allow_change == 0:
            ans.append(to_modify.copy())
            return
        elif cur >= N:
            return

        if to_modify[cur] in {'.', '#'}:
            return backtrack(cur + 1, allow_change, to_modify)

        to_modify[cur] = '#'
        backtrack(cur + 1, allow_change - 1, to_modify)        
        to_modify[cur] = '.'
        backtrack(cur + 1, allow_change, to_modify)
        to_modify[cur] = '?'
    
    backtrack(0, allow_change, to_modify)
    return ans   

def match(possibility, records):
    for i in range(len(possibility)):
        if possibility[i] == '?':
            possibility[i] = '.'
    
    possibility = ''.join(possibility)
    values = list(map(len, possibility.split('.')))
    pointer = 0
    for val in values:
        if val == 0:
            continue
        if pointer >= len(records):
            return False
        if val != records[pointer]:
            return False
        pointer += 1
    return True

def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    ans = 0
    for line in lines:
        raw_spring, raw_record = line.split()
        record = list(map(int, raw_record.split(',')))

        cur_ans = 0
        for pos in generate(raw_spring, sum(record)):
            if match(pos, record):
                cur_ans += 1
        ans += cur_ans
        print(f'Test: {line} | Sol: {cur_ans}')
    return ans

if __name__ == "__main__":
    file_name = "input.txt"
    print(solver(file_name))
