with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

contestants = []
for line in lines:
    name, _, _, speed, _, _, fly_duration, _, _, _, _, _, _, rest_duration, _ = line.split()
    contestants.append((name, int(speed), int(fly_duration), int(rest_duration)))

winner = ''
max_distance = 0
TIME = 2503

for contestant in contestants:
    name, speed, fly_duration, rest_duration = contestant

    distance = 0
    distance_per_cycle = speed * fly_duration
    second_per_cycle = fly_duration + rest_duration
    distance += distance_per_cycle * (TIME // second_per_cycle)

    remainder = TIME % second_per_cycle
    if remainder > fly_duration:
        distance += distance_per_cycle
    else:
        distance += speed * remainder

    if distance > max_distance:
        winner = name
        max_distance = distance

    print(name, distance)

print(f'winner: {winner} | {max_distance} km')