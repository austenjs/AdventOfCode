def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    
    ans = 0
    for line in lines:
        line = line.strip()
        ans += calculate_point(line)
    return ans

def calculate_point(string):
    record = string.split(':')[1].strip()
    winning_numbers, our_cards = record.split('|')
    winning_numbers = set(winning_numbers.split())

    points = 0
    for card in our_cards.split():
        if card in winning_numbers:
            if points == 0:
                points += 1
            else:
                points += points
    return points

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
