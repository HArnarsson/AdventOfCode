def is_spelled(var):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return var in numbers

filename = "input.txt"

inputs = []
with open(filename, "r") as file:
    for line in file:
        inputs.append(line)

outputs = []
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
mapping = dict(zip(numbers, [str(i) for i in range(1, 10)]))
for i in inputs:
    nums = []
    for j in range(len(i)):
        if i[j].isnumeric():
            nums.append(i[j])
        else:
            # The longest number is three, which is of length 5
            # The shortest number is one, which is of length 3
            for k in range(2, 6):
                if j+k < len(i):
                    if is_spelled(i[j: j+k]):
                        nums.append(mapping[i[j:j+k]])
    outputs.append(int(nums[0] + nums[-1]))

summa = 0
for num in outputs:
    summa += num
print(summa)