import regex as re
from utils.file_io import get_input

def main():
    file_content = get_input()
    matches = re.finditer(pattern=r"mul\((\d+)\,(\d+)\)|do\(\)|don't\(\)", string=file_content)
    sum = 0
    add_to = True
    for match in matches:
        text = match.group(0)
        if text == "do()":
            add_to = True
        elif text == "don't()":
            add_to = False
        else:
            if add_to: 
                sum += int(match.group(1)) * int(match.group(2))
    print(sum)

if __name__ == "__main__":
    main()

