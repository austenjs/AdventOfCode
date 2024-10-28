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
    for char in string:
        if "0" <= char <= "9":
            digits.append(char)
    return int(digits[0] + digits[-1])

if __name__ == '__main__':
    file_name = 'input.txt'
    print(solver(file_name))
