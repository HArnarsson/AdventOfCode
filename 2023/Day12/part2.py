from itertools import combinations
from copy import deepcopy

# https://stackoverflow.com/questions/13009675/find-all-the-occurrences-of-a-character-in-a-string
def find_occurrences(string, character):
    return [i for i, letter in enumerate(string) if letter == character]

def remove_instance(lst, item):
    return [value for value in lst if value != item]

def ways(spring, group):
    question_marks = find_occurrences(spring, "?")
    damaged_springs = find_occurrences(spring, "#")
    m = len(damaged_springs)
    n = sum(group)
    possibilities = combinations(question_marks, n-m)
    outcomes = []
    for p in possibilities:
        tmp_string = deepcopy(list(spring))
        for hash in p:
            tmp_string[hash] = "#"
        tmp_string = "".join(tmp_string).replace("?", ".")
        outcomes.append(tmp_string)
    count = 0
    for outcome in outcomes:
        tmp = remove_instance(outcome.split("."), "")
        if len(tmp) != len(group):
            continue
        flag = True
        for i in range(len(tmp)):
            if len(tmp[i]) != group[i]:
                flag = False
                break
        count += int(flag)
    return count

filename = "input.txt"

springs = []
groups = []

EXTENSION = 5
with open(filename, "r") as file:
    for row in file:
        tmp = row.strip().split(" ")
        spring = ""
        for i in range(EXTENSION-1):
            spring += tmp[0]
            spring += "?"
        spring += tmp[0]
        springs.append(spring)
        groups.append(tmp[1].split(",")*EXTENSION)

print(springs[0])

for i in range(len(groups)):
    groups[i] = [int(num) for num in groups[i]]
# let k be the number of question marks
# let n be the total number of damaged springs
# let m be the number of damaged springs shown
# for each row, we have C(k, (n-m)) possibilities to
# place each damaged spring


tally = 0
i = 0
for spring, group in zip(springs, groups):
    print(i)
    tally += ways(spring, group)
    i+= 1
print(tally)
