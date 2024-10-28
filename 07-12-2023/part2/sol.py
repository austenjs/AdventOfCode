from collections import Counter

def solver(file_name):
    with open (file_name, 'r') as f:
        lines = f.read().splitlines()

    to_sort = []
    for line in lines:
        cards, bid = line.split()
        if 'J' in cards:
            to_sort.append([*process_joker(cards), int(bid)])
        else:
            to_sort.append([*process(cards), int(bid)])
    to_sort.sort()

    ans = 0
    for i, (*_, bid) in enumerate(to_sort):
        ans += (i + 1) * bid
    return ans

CARDS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
CARD_RANKS = {card : len(CARDS) - i for i, card in enumerate(CARDS)}

def process(cards):
    # Rankings
    ## high card 0
    ## one pair 1
    ## two pair 2
    ## three of a kind 3
    ## full house 4
    ## four of a kind 5
    ## five of a kind 6
    count = Counter(cards)
    card_ranks = [CARD_RANKS[card] for card in cards]
    if len(count) == 1:
        return (6, *card_ranks)
    elif len(count) == 2:
        return (max(count.values()) + 1, *card_ranks)
    elif len(count) == 3:
        return(max(count.values()), *card_ranks)
    return (5 - len(count), *card_ranks)

def process_joker(cards):
    count = Counter(cards)
    num_joker = count.pop('J', 0)
    card_ranks = [CARD_RANKS[card] for card in cards]

    if len(count) <= 1:
        # J = 1 -> {X : 4}
        # J = 2 -> {X : 3}
        # J = 3 -> {X : 2}
        # J = 4 -> {X : 1}
        return (6, *card_ranks)
    elif len(count) == 2:
        # J = 1 -> {X : 3, Y : 1}|{X : 2, Y : 2}|{X : 1, Y : 3}
        # J = 2 -> {X : 2, Y : 1}|{X : 1, Y: 2}
        # J = 3 -> {X : 1, Y : 1}
        return (max(count.values()) + num_joker + 1, *card_ranks)
    elif len(count) == 3:
        # J = 1 -> {X : 2, Y : 1, Z : 1}|{X : 1, Y : 2, Z : 1}|{X : 1, Y : 1, Z : 2}
        # J = 2 -> {X : 1, Y : 1, Z : 1}
        return (3, *card_ranks)
    else:
        # J = 1 -> {W : 1, X : 1, Y : 1, Z : 1}
        return (1, *card_ranks)

if __name__ == "__main__":
    file_name = "input.txt"
    print(solver(file_name))
