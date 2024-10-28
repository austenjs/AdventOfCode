def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    
    N = len(lines)
    counts = [0 for _ in range(N)]
    for i, line in enumerate(lines):
        points = calculate_point(line)
        counts[i] += 1
        for j in range(i + 1, min(N, i + points + 1)):
            counts[j] += counts[i]
    return sum(counts)

def calculate_point(string):
    record = string.split(':')[1].strip()
    winning_numbers, our_cards = record.split('|')
    winning_numbers = set(winning_numbers.split())

    points = 0
    for card in our_cards.split():
        if card in winning_numbers:
            points += 1
    return points

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
