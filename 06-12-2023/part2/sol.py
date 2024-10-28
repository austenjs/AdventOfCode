def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]
    race_time = int(''.join(times))
    race_distance = int(''.join(distances))
    
    lower_bound = find_lower_bound(race_time, race_distance)
    upper_bound = find_upper_bound(race_time, race_distance, lower_bound + 1)
    print(race_distance)
    print(f'LB: {lower_bound} | reach: {lower_bound * (race_time - lower_bound)} | reach distance: {lower_bound * (race_time - lower_bound) > race_distance}')
    print(f'UB: {upper_bound} | reach: {upper_bound * (race_time - upper_bound)} | reach distance: {upper_bound * (race_time - upper_bound) > race_distance}')
    return upper_bound - lower_bound

def find_lower_bound(race_time, race_distance):
    left, right = 1, race_time
    while left < right - 1:
        press = left + (right - left) // 2
        reach = press * (race_time - press)
        if reach > race_distance:
            right = press - 1
        else:
            left = press
    return right

def find_upper_bound(race_time, race_distance, lower_bound):
    left, right = lower_bound, race_time
    while left + 1 < right:
        press = left + (right - left) // 2
        reach = press * (race_time - press)
        if reach > race_distance:
            left = press
        else:
            right = press - 1
    return right

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
