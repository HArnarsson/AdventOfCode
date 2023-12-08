class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"left: {self.left}, right: {self.right}"

filename = "input.txt"

nodes = dict()

with open(filename, "r") as file:
    instructions = file.readline().strip()
    # skip empty line
    file.readline()
    for line in file:
        tmp = line.strip().split(' = ')
        currNode = tmp[0]
        left = tmp[1].split(',')[0][1:]
        right = tmp[1].split(', ')[1][:-1]
        nodes[currNode] = Node(left, right)

currNode = 'AAA'
counter = 0
i = 0
while currNode != 'ZZZ':
    instruction = instructions[i]
    if instruction == 'L':
        currNode = nodes[currNode].left
    else:
        currNode = nodes[currNode].right
    i = (i+1)%len(instructions)
    counter += 1

print(counter)