from utils.file_io import get_lines
from typing import List
def main():
    lines = get_lines(None, False)
    count = 0
    for line in lines:
        combos = generate_combos(line)
        count += any([is_safe(combo) for combo in combos])
            

    print(count)

def generate_combos(line: str):
    combos = []
    nums = [int(val) for val in line.split()]
    for i in range(len(nums)):
        copy = nums.copy()
        copy.pop(i)
        combos.append(copy)

    print(combos)
    return combos
def is_safe(nums: List[int]):
    last = nums[0]
    if nums[1] > last:
        asc = True
    elif nums[1] < last:
        asc = False
    else: 
        return False
    
    for val in nums[1:]:
        if val > last and not asc:
            return False
        elif val < last and asc:
            return False
        
        if abs(val - last) > 3 or abs(val - last) < 1:
            return False
        
        last = val
        
        
    return True
if __name__ == "__main__":
    main()

