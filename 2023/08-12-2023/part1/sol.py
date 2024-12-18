from collections import defaultdict

def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    actions = [0 if char == 'L' else 1 for char in lines[0]]
    adj_list = defaultdict(list)
    for i in range(2, len(lines)):
        line = lines[i]
        source = line[:3]
        left = line[7:10]
        right = line[12:15]
        adj_list[source].append(left)
        adj_list[source].append(right)
    return find_steps(adj_list, actions)

def find_steps(adj_list, actions):
    ans = 0
    pointer = 0
    num_of_actions = len(actions)

    cur = 'AAA'
    while cur != 'ZZZ':
        cur = adj_list[cur][actions[pointer]]
        pointer = (pointer + 1) % num_of_actions
        ans += 1
    return ans

if __name__ == "__main__":
    file_name = "input.txt"
    print(solver(file_name))
