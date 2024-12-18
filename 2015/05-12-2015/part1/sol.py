def check_nice(string):
    for ban_substring in ['ab', 'cd', 'pq', 'xy']:
        if ban_substring in string:
            return False

    vowels = 0
    have_repeating = False
    for i, char in enumerate(string):
        if char in 'aiueo': vowels += 1
        if i != 0 and char == string[i - 1]: have_repeating = True
    return have_repeating & (vowels >= 3)

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

num_nice_strings = 0
for string in lines:
    num_nice_strings += check_nice(string)
print(num_nice_strings)
