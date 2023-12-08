class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.score = None
        self.bid = bid
        self.evaluate_hand()

    def __str__(self):
        return f"cards: {self.cards}, bid: {self.bid}"
    def check_five_of_a_kind(self):
        if len(set(self.cards)) == 1:
            self.score = 5  # Five of a kind
            return True
        return False

    def check_four_of_a_kind(self):
        for card in self.cards:
            if self.cards.count(card) == 4:
                self.score = 4  # Four of a kind
                return True
        return False

    def check_full_house(self):
        if len(set(self.cards)) == 2 and (self.cards.count(self.cards[0]) == 3 or self.cards.count(self.cards[0]) == 2):
            self.score = 3  # Full house
            return True
        return False

    def check_three_of_a_kind(self):
        for card in self.cards:
            if self.cards.count(card) == 3:
                self.score = 2  # Three of a kind
                return True
        return False

    def check_two_pair(self):
        counts = {card: self.cards.count(card) for card in set(self.cards)}
        if list(counts.values()).count(2) == 2 and list(counts.values()).count(1) == 1:
            self.score = 1  # Two pair
            return True
        return False

    def check_one_pair(self):
        for card in self.cards:
            if self.cards.count(card) == 2:
                self.score = 0  # One pair
                return True
        return False

    def check_high_card(self):
        if len(set(self.cards)) == 5:
            self.score = -1  # High card
            return True
        return False
        
    def evaluate_hand(self):
        if self.check_five_of_a_kind():
            return
        elif self.check_four_of_a_kind():
            return
        elif self.check_full_house():
            return
        elif self.check_three_of_a_kind():
            return
        elif self.check_two_pair():
            return
        elif self.check_one_pair():
            return
        elif self.check_high_card():
            return
        else:
            print('SNO Error')
            return
        
    def __lt__(self, other):
        def compare_cards(card1, card2):
            order = "23456789TJQKA"
            return order.index(card1) - order.index(card2)
        if self.score < other.score:
            return True
        if other.score < self.score:
            return False
        # Must be equal, check the cards sequentially
        for i in range(len(self.cards)):
            result = compare_cards(self.cards[i], other.cards[i])
            if result != 0:
                if result < 0:
                    return True
                else:
                    return False

filename = "input.txt"

hands = []
with open(filename, 'r') as file:
    for line in file:
        tmp = line.strip().split(' ')
        hands.append(Hand(tmp[0], int(tmp[1])))

hands.sort()
total_winnings = 0
for i in range(len(hands)):
    total_winnings += (i+1) * hands[i].bid
    
print(total_winnings)