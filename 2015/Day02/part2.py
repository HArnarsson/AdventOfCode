def get_ribbon(box):
    l, w, h = box
    ribbon = l*w*h
    box.remove(max(box))
    ribbon += 2*sum(box)
    return ribbon

filename = "input.txt"

boxes = []
with open(filename, "r") as file:
    for line in file:
        temp = line.split('x')
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        boxes.append(temp)

total_ribbon = 0
for box in boxes:
    total_ribbon += get_ribbon(box)

print(total_ribbon)