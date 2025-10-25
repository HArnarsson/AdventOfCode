from utils.file_io import get_lines
from typing import List

def main():
    lines = get_lines(None, False)
    dist = 0
    l1, l2 = get_lists(lines)
    l1.sort()
    l2.sort()

    assert len(l1) == len(l2)

    for i in range(len(l1)):
        dist += abs(l1[i] - l2[i])
    
    print(dist)
    

def get_lists(lines: List[str]):
    l1 = []
    l2 = []
    for line in lines:
        splits = line.split()
        l1.append(int(splits[0]))
        l2.append(int(splits[1]))
    return (l1, l2)

if __name__ == "__main__":
    main()