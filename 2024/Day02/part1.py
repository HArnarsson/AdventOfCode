from utils.file_io import get_lines

def main():
    lines = get_lines(None, False)
    count = 0
    for line in lines:
        count += int(is_safe(line))

    print(count)


def is_safe(line: str):
    nums = [int(val) for val in line.split()]
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

