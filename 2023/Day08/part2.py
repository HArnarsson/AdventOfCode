from math import prod

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"left: {self.left}, right: {self.right}"

def SieveOfEratosthenes(num):
    # alg for finding prime numbers
    prime = [True for _ in range(num+1)]
    p = 2
    while (p * p <= num):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            yield p

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

currNodes = [node for node in nodes.keys() if node[2] == 'A']
cycles = [0 for _ in range(len(currNodes))]
for i in range(len(currNodes)):
    currNode = currNodes[i]
    counter = 0
    it = 0
    while currNode[2] != 'Z':
        instruction = instructions[it]
        if instruction == 'L':
            currNode = nodes[currNode].left
        else:
            currNode = nodes[currNode].right
        it = (it+1)%len(instructions)
        counter += 1
    cycles[i] = counter

primes = list(SieveOfEratosthenes(max(cycles)+1))

lcm_factors = []
for prime in primes:
    while True:
        flag = False
        for i in range(len(cycles)):
            if cycles[i] % prime == 0:
                if flag == False: 
                    # Only want to append once for each iteration through cycle
                    lcm_factors.append(prime)
                cycles[i] /= prime
                flag = True
            else:
                continue
        if not flag:
            # None of the numbers divide anymore
            break
    if cycles == [1]*len(cycles):
        break

print(prod(lcm_factors))