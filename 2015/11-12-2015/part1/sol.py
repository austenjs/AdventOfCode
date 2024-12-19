with open('input.txt', 'r') as f:
    string = f.read()

def check_first(string):
    N = len(string)
    for i in range(N - 2):
        first = ord(string[i])
        second = ord(string[i + 1])
        third = ord(string[i + 2])
        if first + 1 == second and second + 1 == third:
            return True
    return False

def check_second(string):
    chars = set(string)
    if 'i' in chars:
        return False
    if 'o' in chars:
        return False
    if 'l' in chars:
        return False
    return True

def check_third(string):
    N = len(string)
    pairs = set()
    for i in range(N - 1):
        if string[i] == string[i + 1]:
            pairs.add(string[i:i+2])
    return len(pairs) >= 2

N = len(string)
while True:
    first_flag = check_first(string)
    second_flag = check_second(string)
    third_flag = check_third(string)
    if first_flag and second_flag and third_flag:
        print('final password:', string)
        exit()

    if not second_flag:
        for i in range(N - 1, -1, -1):
            if string[i] in 'iol':
                string = string[:i] + chr(ord(string[i]) + 1) + 'a' * (N - i - 1)
                break

    # increment one-by-one
    chars = list(string)
    pointer2 = N - 1
    while True:
        char = chars[pointer2]
        if char == 'z':
            chars[pointer2] = 'a'
            pointer2 -= 1
        else:
            chars[pointer2] = chr(ord(char) + 1)
            break
    string = ''.join(chars)
