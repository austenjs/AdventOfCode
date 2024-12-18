LIMITS = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    
    ans = 0
    for i, line in enumerate(lines):
        id_number = i + 1
        line = line.strip()
        if check_record(line):
            ans += id_number
    return ans

def check_record(string):
    record = string.split(':')[1].strip()
    for game in record.split(';'):
        game = game.strip()
        for revealed in game.split(','):
            revealed = revealed.strip()
            quantity, color = revealed.split(' ')

            quantity = int(quantity)
            if quantity > LIMITS[color]:
                return False
    return True

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
