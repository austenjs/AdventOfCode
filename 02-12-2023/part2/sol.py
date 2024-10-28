def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    
    ans = 0
    for line in lines:
        line = line.strip()
        ans += find_min_power(line)
    return ans

def find_min_power(string):
    record = string.split(':')[1].strip()
    min_number_cubes = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }

    for game in record.split(';'):
        game = game.strip()
        for revealed in game.split(','):
            revealed = revealed.strip()
            quantity, color = revealed.split(' ')

            new_quantity = int(quantity)
            old_quantity = min_number_cubes[color]
            min_number_cubes[color] = max(old_quantity, new_quantity)
    
    ans = 1
    for value in min_number_cubes.values():
        ans *= value
    return ans

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
