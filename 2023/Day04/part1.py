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

tally = 0
for i in range(len(cards)):
    pts = 0
    for num in winning_nums[i]:
        if num in cards[i]:
            pts += 1
    if pts != 0:
        tally += 2**(pts-1)

print(tally)