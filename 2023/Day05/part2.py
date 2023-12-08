class Mapping:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.ranges = []
    
    def __str__(self):
        return f"source: {self.source}, target: {self.target}"
    
    def add_range(self, dest, source, length):
        func = lambda num: dest + num - source if source <= num < source + length else None
        self.ranges.append(func)

    def evaluate(self, num):
        for func in self.ranges:
            if func(num) != None:
                return func(num)
            else:
                continue
        return num

filename = "input.txt"

seeds = []
mappings = []
with open(filename, 'r') as file:
    # read the seeds
    read_seeds = file.readline().strip().split(':')[1][1:]
    for seed in read_seeds.split(' '):
        seeds.append(int(seed))
    # get to the first map
    file.readline()
    # Now read in the maps
    for line in file:
        if line == '\n':
            # return clause
            mappings.append(mapping)
            continue
        if line.strip().split(' ')[1] == 'map:':
            tmp = line.strip().split(' ')[0]
            mapping = Mapping(tmp.split('-')[0], tmp.split('-')[2])
            continue
        dest, source, length = [int(num) for num in line.strip().split(' ')]
        mapping.add_range(dest, source, length)
    # last line is not \n, need to add last mapping
    mappings.append(mapping)

min_seed = float('inf')
for i in range(0, len(seeds), 2):
    print(i)
    for curr_seed in range(seeds[i], seeds[i] + seeds[i+1]):
        seed = curr_seed
        for mapping in mappings:
            seed = mapping.evaluate(seed)
        if seed < min_seed:
            min_seed = seed

print(min_seed)