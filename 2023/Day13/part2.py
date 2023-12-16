def count_equals(symm, rest):
    count = 0
    for i in range(len(symm)):
        for j in range(len(symm[0])):
            if symm[i][j] != rest[i][j]:
                count += 1
    return count

def transpose(pattern):
    ret = []
    for i in range(len(pattern[0])):
        line = []
        for j in range(len(pattern)):
            line.append(pattern[j][i])
        ret.append(line)

    return ret

def find_symmetry(pattern):
    i = 1
    while i < len(pattern):
        symm = pattern[:i]
        rest = pattern[i:]
        # normalize
        if len(symm) < len(rest):
            rest = rest[:len(symm)]
        elif len(rest) < len(symm):
            symm = symm[len(symm)-len(rest):]
        if count_equals(symm, rest[::-1]) == 1:
            return i
        i+= 1
    return 0

filename = "input.txt"

patterns = []
with open(filename, "r") as file:
    pattern = []
    for line in file:
        if line == "\n":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(list(line.strip()))
    patterns.append(pattern)

tally = 0
for pattern in patterns:
    if find_symmetry(pattern) == 0:
        tally += find_symmetry(transpose(pattern))
    else:
        tally += 100*find_symmetry(pattern)
print(tally)