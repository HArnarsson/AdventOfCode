filename = "input.txt"

wires = {}

def get_signal(wire):
    if wire.isdigit():
        return int(wire)
    return wires[wire]

def execute_instruction(instruction):
    parts = instruction.split(' -> ')
    operation, output = parts[0], parts[1]

    if 'AND' in operation:
        wires[output] = get_signal(operation.split(' AND ')[0]) & get_signal(operation.split(' AND ')[1])
    elif 'OR' in operation:
        wires[output] = get_signal(operation.split(' OR ')[0]) | get_signal(operation.split(' OR ')[1])
    elif 'LSHIFT' in operation:
        wires[output] = get_signal(operation.split(' LSHIFT ')[0]) << int(operation.split(' LSHIFT ')[1])
    elif 'RSHIFT' in operation:
        wires[output] = get_signal(operation.split(' RSHIFT ')[0]) >> int(operation.split(' RSHIFT ')[1])
    elif 'NOT' in operation:
        wires[output] = ~get_signal(operation.split('NOT ')[1])
    else:
        wires[output] = get_signal(operation)

with open(filename, 'r') as file:
    for line in file:
        execute_instruction(line.strip())

