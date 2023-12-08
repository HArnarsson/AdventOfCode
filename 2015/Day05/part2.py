def has_duplicate_pair(string):
    for i in range(len(string) - 1):
        pair = string[i:i+2]
        for j in range(i + 2, len(string) - 1):
            if pair == string[j:j+2]:
                return True
    return False

def has_pair_with_between(string):
    for i in range(len(string) - 2):
        if string[i] == string[i+2]:
            return True
    return False

def is_nice(string):
    return has_duplicate_pair(string) and has_pair_with_between(string)
 
filename = "input.txt"

strings = []
with open(filename, "r") as file:
    for line in file:
        strings.append(line)

counter = 0
for string in strings:
    counter += int(is_nice(string))

print(counter)