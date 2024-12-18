with open('input.txt', 'r') as f:
    string = f.read()
left = string.count('(')
right = string.count(')')
print(left - right)
