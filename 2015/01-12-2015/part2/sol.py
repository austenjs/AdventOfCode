with open('input.txt', 'r') as f:
    string = f.read()

floor = 0
for i, char in enumerate(string):
    if char == '(':
        floor += 1
    else:
        floor -= 1
    
    if floor == -1:
        print(i + 1)
        break
