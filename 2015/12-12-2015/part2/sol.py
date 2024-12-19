with open('input.txt', 'r') as f:
    string = f.read()

def dfs(item):
    if type(item) == int:
        return item
    elif type(item) == str:
        return 0
    elif type(item) == list:
        total = 0
        for elem in item:
            total += dfs(elem)
        return total
    elif type(item) == dict:
        total = 0
        for elem in item.values():
            if elem == 'red':
                return 0
            total += dfs(elem)
        return total

print(dfs(eval(string)))
