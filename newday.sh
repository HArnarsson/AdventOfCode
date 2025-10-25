#!/bin/bash
# Usage: ./newday.sh YYYY XX
# Example: ./newday.sh 2024 05
# This creates 2024/Day05/ with input.txt, smallinput.txt, part1.py, part2.py

# --- Validate input ---
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <year> <day>"
    exit 1
fi

year="$1"
day="$2"

# --- Verify that the year directory exists ---
if [ ! -d "$year" ]; then
    echo "Error: Directory '$year' does not exist."
    exit 1
fi

# --- Create DayXX directory ---
daydir="$year/Day$(printf '%02d' "$day")"

if [ -d "$daydir" ]; then
    echo "Error: $daydir already exists."
    exit 1
fi

mkdir -p "$daydir" || { echo "Failed to create directory: $daydir"; exit 1; }

# --- Create empty input files ---
touch "$daydir/input.txt" "$daydir/smallinput.txt"

# --- Template content for Python files ---
py_template='def main():
    

    return

if __name__ == "__main__":
    main()
'

# --- Create part1.py and part2.py ---
echo "$py_template" > "$daydir/part1.py"
echo "$py_template" > "$daydir/part2.py"

# --- Success message ---
echo "✅ Created $daydir with input.txt, smallinput.txt, part1.py, and part2.py"
