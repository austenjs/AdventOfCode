from collections import defaultdict

with open('input.txt', 'r') as f:
    instructions = f.read().splitlines()

atoms = {}
dependencies = defaultdict(list)
for instruction in instructions:
    input_gate, output_gate = instruction.split(' -> ')
    if input_gate.isnumeric():
        atoms[output_gate] = int(input_gate)
    else:
        dependencies[output_gate] = input_gate

def traverse(variable):
    if variable in atoms:
        return atoms[variable]
    elif variable.isnumeric():
        return int(variable)

    dependency = dependencies[variable]
    tokens = dependency.split()
    if len(tokens) == 1:
        ans = traverse(tokens[0])
    elif len(tokens) == 2:
        ans = ~traverse(tokens[1])
    elif len(tokens) == 3:
        if tokens[1] == 'LSHIFT':
            left = traverse(tokens[0])
            right = traverse(tokens[2])
            ans = left << right
        elif tokens[1] == 'RSHIFT':
            left = traverse(tokens[0])
            right = traverse(tokens[2])
            ans = left >> right
        elif tokens[1] == 'AND':
            left = traverse(tokens[0])
            right = traverse(tokens[2])
            ans = left & right
        elif tokens[1] == 'OR':
            left = traverse(tokens[0])
            right = traverse(tokens[2])
            ans = left | right
        else:
            print(tokens[1])
            raise Exception
    else:
        print(tokens)
        raise Exception
    atoms[variable] = ans
    return ans

atoms['b'] = 46065
print(traverse('a'))
