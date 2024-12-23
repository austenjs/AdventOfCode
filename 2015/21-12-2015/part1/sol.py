from itertools import combinations

WEAPONS = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

ARMORS = [
    (0, 0, 0), # no armor
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

RINGS = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]

def is_winning(damage, armor, BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR):
    hp = 100
    while hp > 0 and BOSS_HP > 0:
        BOSS_HP -= max(1, damage - BOSS_ARMOR)
        if BOSS_HP <= 0: break
        hp -= max(1, BOSS_DAMAGE - armor)
        if hp <= 0: break
    return BOSS_HP <= 0 and hp > 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

BOSS_HP = int(lines[0].split(': ')[1])
BOSS_DAMAGE = int(lines[1].split(': ')[1])
BOSS_ARMOR = int(lines[2].split(': ')[1])

min_coin = 99999
won = False
for weapon in WEAPONS:
    wcoin, wdamage, warmor = weapon
    for armor in ARMORS:
        acoin, adamage, aarmor = armor
        coin = wcoin + acoin
        damage = wdamage + adamage
        armor = warmor + aarmor
        if won and coin >= min_coin:
            continue
        elif is_winning(damage, armor, BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR):
            won = True
            min_coin = coin

        # RINGS
        for num_ring in range(1, 3):
            rings_combinations = combinations(RINGS, num_ring)
            for combination in rings_combinations:
                rcoin, rdamage, rarmor = map(sum, zip(*combination))
                if coin + rcoin >= min_coin:
                    continue
                elif is_winning(damage + rdamage, armor + rarmor, BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR):
                    won = True
                    min_coin = coin + rcoin
print(min_coin)
