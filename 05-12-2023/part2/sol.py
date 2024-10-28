file_name = 'input.txt'
with open(file_name, 'r') as f:
    lines = f.read().splitlines()

list_of_maps = [[] for _ in range(7)]
seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = list_of_maps

seeds = []
pointer = -1
for line in lines:
    if line == '':
        pointer += 1
        continue
    elif pointer == -1:
        pairs = list(map(int, line.split()[1:]))
        for i in range(len(pairs) // 2):
            seeds.append((pairs[2 * i], pairs[2 * i + 1]))

    try:
        target, source, num_range = list(map(int, line.split()))
    except:
        continue

    list_of_maps[pointer].append((source, num_range, target))

for magic_map in list_of_maps:
    magic_map.sort()

ans, cur_range = max(seeds)
for seed, range in seeds:
    to_explore = [(seed, range)]
    for magic_map in list_of_maps:
        new_frontier = []
        covered = []
        to_add = []
        for seed, range in to_explore:
            added = False
            for source, num_range, target in magic_map:
                if source <= seed < source + num_range:
                    added = True
                    new_start, new_range = (target + seed - source, min(range, num_range + source - seed))
                    if source + num_range < seed + range:
                        to_add.append((seed + new_range, seed + range - source - num_range))
                    new_frontier.append((new_start, new_range))
                    covered.append((seed, new_range))
                elif seed <= source < seed + range:
                    added = True
                    new_start, new_range = (target, min(num_range, range + seed - source))
                    new_frontier.append((new_start, new_range))
                    if seed != source:
                        to_add.append((seed, source - seed))
                    covered.append((source, seed + range - source))
            if not added:
                to_add.append((seed, range))

        if new_frontier:
            prevs = to_add
            prevs.sort()
            while True:
                cur_to_add = []
                for candidate in prevs:
                    to_add = True
                    for c in covered:
                        if c[0] <= candidate[0] < sum(c) and c[0] <= sum(candidate) - 1 < sum(c):
                            to_add = False
                        elif c[0] <= candidate[0] < sum(c):
                            to_add = False
                            cur_to_add.append((candidate[0], sum(c) - candidate[0]))
                        elif c[0] <= sum(candidate) - 1 < sum(c):
                            to_add = False
                            cur_to_add.append((c[0], sum(candidate) - c[0]))
                    if to_add:
                        cur_to_add.append(candidate)

                cur_to_add.sort()
                if cur_to_add == []:
                    break
                elif cur_to_add == prevs:
                    break
                prevs = cur_to_add
            new_frontier.extend(cur_to_add)
            to_explore = new_frontier
        
    if to_explore:
        ans = min(min(to_explore)[0], ans)
print(ans)
