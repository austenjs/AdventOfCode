file_name = 'input.txt'
with open(file_name, 'r') as f:
    lines = f.read().splitlines()

list_of_maps = [[] for _ in range(7)]
seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = list_of_maps

pointer = -1
for line in lines:
    if line == '':
        pointer += 1
        continue
    elif pointer == -1:
        seeds = list(map(int, line.split()[1:]))
        continue
    
    try:
        target, source, num_range = list(map(int, line.split()))
    except:
        continue

    list_of_maps[pointer].append((source, num_range, target))

for magic_map in list_of_maps:
    magic_map.sort()

ans = max(seeds)
for seed in seeds:
    for magic_map in list_of_maps:
        for source, num_range, target in magic_map:
            if source <= seed < source + num_range:
                seed = target + seed - source
                break
    ans = min(seed, ans)
print(ans)
