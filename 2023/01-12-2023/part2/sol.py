NUMBER_STRINGS_PAIR = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9')                    
]

def solver(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()

    ans = 0
    for line in lines:
        line = line.strip()
        ans += find_calibration_value(line)
    return ans

def find_calibration_value(string):
    digits = []
    for i, char in enumerate(string):
        if "0" <= char <= "9":
            digits.append(char)
            continue

        for key, value in NUMBER_STRINGS_PAIR:
            start_index = max(i - len(key) + 1, 0)
            end_index = i + 1
            if string[start_index:end_index] == key:
                digits.append(value)
                break

    return int(digits[0] + digits[-1])

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
