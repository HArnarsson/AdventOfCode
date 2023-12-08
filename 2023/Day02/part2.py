class Round:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'red: {red}, green: {green}, blue: {blue}'
        
    def power(self):
        return self.red*self.blue*self.green


def is_legal(round: Round):
    return round.red <= 12 and round.green <= 13 and round.blue <= 14

filename = "input.txt"

games = []
with open(filename, 'r') as file:
    for line in file:
        games.append(line.strip())

processed_games = []
for game in games:
    round_data = game.split(":")[1].strip().split('; ')
    rounds = []
    for round in round_data:
        cubes = round.split(',')
        red = green = blue = 0
        for cube in cubes:
            tmp = cube.strip().split(' ')
            if tmp[1] == 'blue':
                blue = int(tmp[0])
            if tmp[1] == 'red':
                red = int(tmp[0])
            if tmp[1] == 'green':
                green = int(tmp[0])
        rounds.append(Round(red, green, blue))
    processed_games.append(rounds)

summa = 0
for game in processed_games:
    min_red = 0
    min_green = 0
    min_blue = 0
    for round in game:
        if round.red > min_red:
            min_red = round.red
        if round.green > min_green:
            min_green = round.green
        if round.blue > min_blue:
            min_blue = round.blue
    min_round = Round(min_red, min_green, min_blue)
    summa += min_round.power()

print(summa)
