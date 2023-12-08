filename = "input.txt"

winning_nums = []
cards = []
with open(filename, 'r') as file:
    for card in file:
        tmp = card.strip().split(":")[1]
        tmp = tmp.split("|")
        winners = tmp[0]
        guesses = tmp[1]
        winners = winners.strip().split(' ')
        winning_nums.append([int(num) for num in winners if num != ''])
        guesses = guesses.strip().split(' ')
        cards.append([int(num) for num in guesses if num != ''])

copies = {num: 1 for num in range(len(cards))}
for i in range(len(cards)):
    count = 0
    for num in winning_nums[i]:
        if num in cards[i]:
            count += 1
    k = 1
    while(k <= count):
        copies[i + k] += copies[i]
        k += 1
        
count = 0
for i in range(len(cards)):
    count += copies[i]
print(count)