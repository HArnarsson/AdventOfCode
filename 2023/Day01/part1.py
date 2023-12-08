filename = "input.txt"

inputs = []
with open(filename, "r") as file:
    for line in file:
        inputs.append(line)

outputs = []
for i in inputs:
    nums = []
    for j in range(len(i)):
        if i[j].isnumeric():
            nums.append(i[j])
    outputs.append(int(nums[0] + nums[-1]))

summa = 0
for num in outputs:
    summa += num
print(summa)