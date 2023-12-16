def transpose(pattern):
    ret = []
    for i in range(len(pattern[0])):
        line = []
        for j in range(len(pattern)):
            line.append(pattern[j][i])
        ret.append(line)

    return ret

def find_symmetry(pattern):
    symm = [pattern[0]]
    count = 1
    flag = False
    while True:
        for i in range(len(symm)):
            if len(symm) + i >= len(pattern):
                flag = True
                continue
            if symm[len(symm)-1-i] == pattern[len(symm) +i]:
                flag = True
                continue
            else:
                symm.append(pattern[count])
                count += 1
                flag = False
                break
        if flag:
            if len(symm) == len(pattern):
                return 0
            else:
                return count
        


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