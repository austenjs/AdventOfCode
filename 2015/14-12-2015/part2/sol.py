from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

contestants = []
for line in lines:
    name, _, _, speed, _, _, fly_duration, _, _, _, _, _, _, rest_duration, _ = line.split()
    contestants.append((name, int(speed), int(fly_duration), int(rest_duration), int(fly_duration) + int(rest_duration)))

TIME = 2503
positions = defaultdict(int)
cycles = defaultdict(int)
points = defaultdict(int)

for t in range(1, TIME + 1):
    for contestant in contestants:
        name, speed, fly_duration, rest_duration, cycle_duration = contestant
        if cycles[name] < fly_duration: positions[name] += speed
        cycles[name] += 1
        if cycles[name] >= cycle_duration: cycles[name] = 0

    winners = []
    cur_pos = 0
    for name, pos in positions.items():
        if pos > cur_pos:
            winners = [name]
            cur_pos = pos
        elif pos == cur_pos:
            winners.append(name)
    for winner in winners: points[winner] += 1

print(points)
