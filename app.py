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
    'Jack': 11,
    'Queen': 12,
    'King': 13
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
