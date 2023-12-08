def get_paper(box):
    l, w, h = box
    paper = 2*l*w + 2*w*h + 2*h*l
    paper += min(l*w, w*h, h*l)
    return paper

filename = "input.txt"

boxes = []
with open(filename, "r") as file:
    for line in file:
        temp = line.split('x')
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        boxes.append(temp)

total_paper = 0
for box in boxes:
    total_paper += get_paper(box)

print(total_paper)

