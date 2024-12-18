from hashlib import md5

with open('input.txt', 'r') as f:
    code = f.read()

num = 1
while True:
    string = f'{code}{num}'
    hexa = md5(string.encode()).hexdigest()
    if hexa[:5] == '00000':
        print(num)
        break
    num += 1
