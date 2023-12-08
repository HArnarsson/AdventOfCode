def has_three_vowels(string):
    vowel_counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char in vowels:
            vowel_counter += 1
    if vowel_counter >= 3:
        return True
    return False

def has_two_in_a_row(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False

def does_not_have_bad(string):
    flag = True
    if 'ab' in string:
        flag = False
    if 'cd' in string:
        flag = False
    if 'pq' in string:
        flag = False
    if 'xy' in string:
        flag = False
    return flag
    

def is_nice(string):
    return has_three_vowels(string) and has_two_in_a_row(string) and does_not_have_bad(string)

filename = "input.txt"

strings = []
with open(filename, "r") as file:
    for line in file:
        strings.append(line)

counter = 0
for string in strings:
    counter += int(is_nice(string))

print(counter)