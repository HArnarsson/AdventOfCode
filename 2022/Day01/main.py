import heapq as heapq

elves = []

with open('Day01/input.txt') as f:
    lines = f.readlines()

elf = 0
for i in range(len(lines)):
    if(lines[i]) == "\n":
        elves.append(elf)
        elf = 0
    else:
        elf += int(lines[i][0:len(lines[i])-1])

print("Part 1 answer: ")
print(max(elves))

print("Part 2 answer: ")
print(sum(heapq.nlargest(3, elves)))
