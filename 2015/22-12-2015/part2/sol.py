from copy import deepcopy

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

BOSS_HP = int(lines[0].split(': ')[1])
BOSS_DAMAGE = int(lines[1].split(': ')[1])

class Effect:
    def __init__(self, type, duration):
        self.type = type
        self.duration = duration

    def __hash__(self):
        return hash((self.type, self.duration))

    def __eq__(self, other):
        return self.type == other.type and self.duration == other.duration

# hp, mana, manaused, bosshp, effect
states = {(50, 500, 0, BOSS_HP, ())}

types = {'SHIELD', 'POISON', 'RECHARGE'}

won = False
min_mana = 9999
turn = 0
while states:
    new_states = set()
    for state in states:
        hp, mana, manaused, boss_hp, effects = state
        assert(len(effects) <= 3)
        for effect in effects: assert(effect.duration > 0)
        assert(mana >= 0)
        assert(hp > 0)

        # hard mode
        if turn == 0:
            hp -= 1
            if hp <= 0:
                continue

        # cast effects
        exist = set()
        for effect in effects:
            if effect.type == 'POISON': boss_hp -= 3
            elif effect.type == 'RECHARGE': mana += 101
            elif effect.type != 'SHIELD' : raise Exception()
            assert(effect.type not in exist)
            if effect.duration > 1: exist.add(effect.type)

        # due to poison
        if boss_hp <= 0:
            won = True
            min_mana = min(min_mana, manaused)
            continue

        # update effects
        new_effects = tuple()
        for effect in effects:
            effect.duration -= 1
            if effect.duration <= 0: continue
            new_effects += (Effect(effect.type, effect.duration), )

        if turn == 1:
            boss_damage = BOSS_DAMAGE - 7 if 'SHIELD' in exist else BOSS_DAMAGE
            new_hp = hp - boss_damage
            if new_hp <= 0: continue
            new_states.add((new_hp, mana, manaused, boss_hp, deepcopy(new_effects)))
        else:
            # attack
            if mana >= 53:
                new_states.add((hp, mana - 53, manaused + 53, boss_hp - 4, deepcopy(new_effects)))

            # drain
            if mana >= 73:
                new_states.add((hp + 2, mana - 73, manaused + 73, boss_hp - 2, deepcopy(new_effects)))

            # shield
            if 'SHIELD' not in exist and mana >= 113:
                new_states.add((hp, mana - 113, manaused + 113, boss_hp, deepcopy(new_effects) + (Effect('SHIELD', 6), )))

            # poison
            if 'POISON' not in exist and mana >= 173: 
                new_states.add((hp, mana - 173, manaused + 173, boss_hp, deepcopy(new_effects) + (Effect('POISON', 6), )))

            # recharge
            if 'RECHARGE' not in exist and mana >= 229: 
                new_states.add((hp, mana - 229, manaused + 229, boss_hp, deepcopy(new_effects) + (Effect('RECHARGE', 5), )))        
    turn = 1 - turn
    states = new_states
print(min_mana)
