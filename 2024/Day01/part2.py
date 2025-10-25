from utils.file_io import get_lines
from typing import List

def main():
    lines = get_lines(None, False)
    sim_score = 0
    l1, l2 = get_list_and_hashmap(lines)
    for i in range(len(l1)):
        val = l1[i]
        if val in l2.keys():
            sim_score += val * l2[val]
    print(sim_score)

    
    

def get_list_and_hashmap(lines: List[str]):
    l1 = []
    l2 = dict()
    for line in lines:
        splits = line.split()
        l1.append(int(splits[0]))
        val = int(splits[1])
        if val not in l2.keys():
            l2[val] = 1
        else:
            l2[val] += 1
            
    return (l1, l2)

if __name__ == "__main__":
    main()