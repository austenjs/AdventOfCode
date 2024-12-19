with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

ingredients = []
capacities = []
durabilities = []
flavors = []
textures = []
calories = []

for line in lines:
    ingredient, _, capacity, _, durability, _, flavor, _, texture, _, calorie = line.split()
    ingredient = ingredient[:-1]
    capacity = int(capacity[:-1])
    durability = int(durability[:-1])
    flavor = int(flavor[:-1])
    texture = int(texture[:-1])
    calorie = int(calorie)

    ingredients.append(ingredient)
    capacities.append(capacity)
    durabilities.append(durability)
    flavors.append(flavor)
    textures.append(texture)

possible_values = []
for a in range(101):
    leftover = 100 - a
    for b in range(leftover + 1):
        leftover2 = leftover - b
        for c in range(leftover2 + 1):
            d = leftover2 - c
            possible_values.append((a, b, c, d))

max_score = 0
for possible_value in possible_values:
    assert(sum(possible_value) == 100)
    total = 1
    capacity = 0
    for i, value in enumerate(capacities):
        capacity += possible_value[i] * value
    total *= max(0, capacity)

    durability = 0
    for i, value in enumerate(durabilities):
        durability += possible_value[i] * value
    total *= max(0, durability)

    texture = 0
    for i, value in enumerate(textures):
        texture += possible_value[i] * value
    total *= max(0, texture)

    flavor = 0
    for i, value in enumerate(flavors):
        flavor += possible_value[i] * value
    total *= max(0, flavor)

    if total > max_score:
        max_score = total

print(max_score)