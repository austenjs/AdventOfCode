with open('input.txt', 'r') as f:
    string = f.read()

def look_and_say(string):
    cur = None
    count = None

    digits = []
    for char in string:
        if cur is None:
            cur = char
            count = 1
        elif cur == char:
            count += 1
        else:
            digits.append(str(count))
            digits.append(cur)
            cur = char
            count = 1
    digits.append(str(count))
    digits.append(cur)
    return ''.join(digits)

for _ in range(50):
    string = look_and_say(string)
print(len(string))
