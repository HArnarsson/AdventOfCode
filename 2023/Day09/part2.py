filename = "input.txt"

sequences = []
with open(filename, 'r') as file:
    for line in file:
        sequences.append([int(num) for num in line.strip().split(' ')])

new_digits = []
tmp = sequences[0]
for i in range(len(sequences)):
    tmp = sequences[i]
    subsequences = []
    while tmp != len(tmp)*[0]:
        subsequences.append(tmp)
        tmp = [tmp[i+1]-tmp[i] for i in range(len(tmp)-1)]

    new_digit = 0
    for i in range(len(subsequences)-1, -1, -1):
        new_digit = subsequences[i][0] - new_digit
    new_digits.append(new_digit)

print(sum(new_digits))