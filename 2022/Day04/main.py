raw_data = []

def is_contained(lst):
    if(lst[0] >= lst[2] and lst[1] <= lst[3]):
        return True
    if(lst[2] >= lst[0] and lst[3] <= lst[1]):
        return True
    return False

def overlaps(lst):
    # if((lst[0] >= lst[2] and lst[0] <= lst[3]) or (lst[1] >= lst[2] and lst[1] <= lst[3])):
    #     return True
    # if((lst[2] >= lst[0] and lst[2] <= lst[1]) or (lst[3] >= lst[0] and lst[3] <= lst[1])):
    #     return True
    # return False
    if(min((lst[1], lst[3])) < max(lst[0], lst[2])):
        return False
    return True

with open("Day04/input.txt", "r") as file:
    for line in file:
        temp = line.split('-')
        middle = temp[1].split(',')
        temp =  [temp[0]] + middle + [temp[2][:-1]]
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        raw_data.append(temp)

sum1 = 0
for i in range(len(raw_data)):
    sum1 += is_contained(raw_data[i])

print(f'Part 1 answer: {sum1}')

sum2 = 0
for i in range(len(raw_data)):
    sum2 += overlaps(raw_data[i])

print(f'Part 2 answer: {sum2}')
