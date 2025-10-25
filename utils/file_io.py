import os
import inspect

def get_lines(filename, is_demo):
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))

    # Pick filename if not given
    if not filename:
        filename = "smallinput.txt" if is_demo else "input.txt"

    file_path = os.path.join(caller_dir, filename)

    # Read lines safely
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines