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
    num_of_actions = len(actions)
    cur_positions = [start for start in adj_list.keys() if start[-1] == 'A']
    num_starts = len(cur_positions)
    first_z = [None for _ in range(num_starts)]
    steps_to_z = [0 for _ in range(num_starts)]
    cycle_length = [0 for _ in range(num_starts)]

    for i, cur in enumerate(cur_positions):
        pointer = 0
        num_steps = 0
        while True:
            if cur[-1] == 'Z':
                if first_z[i] is None:
                    first_z[i] = cur
                    steps_to_z[i] = num_steps
                elif first_z[i] == cur:
                    cycle_length[i] = num_steps - steps_to_z[i]
                    break
            cur = adj_list[cur][actions[pointer]]
            pointer = (pointer + 1) % num_of_actions
            num_steps += 1
    
    # Find ans
    ans = 1
    for num in cycle_length:
        ans = lcm(ans, num)
    return ans

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a // gcd(a,b))* b 

if __name__ == "__main__":
    file_name = "input.txt"
    print(solver(file_name))
