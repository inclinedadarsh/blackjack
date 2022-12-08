import random

value_dictionary = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}

suits = ['Club', 'Jack', 'Spade', 'Hearts']

ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
         'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value_dictionary[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''

        for card in self.cards:
            deck_comp += "\n" + card.__str__()
        return f"The deck has: {deck_comp}"
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        singe_card = self.cards.pop()
        return singe_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += value_dictionary[card.rank]

        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -=1

class Chip:
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide a valid integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have {} chips left!".format(chips.total))
            else: 
                break