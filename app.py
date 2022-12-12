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

suits = ('Club', 'Jack', 'Spade', 'Hearts')

ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
         'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')

playing = True

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

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s: ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands!")
            playing = False
        else:
            print("Sorry! I did not understand that! Please enter only 'h' or 's': ")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" ")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("DEALERS BUSTS! PLAYER WINS!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS, PLAYER LOSES!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player ties! PUSH!")

# THE GAME BEGINS HERE!

while True:
    print("Welcome to BlackJack!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chip()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
    if player_hand.value <= 21:

        while dealer_hand.value <= 17:
            hit(deck, dealer_hand)
        
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
        
    print(f"\nPlayer Total Chips: {player_chips.total}")

    new_game = input("Would you like to play another hand? y or n?")
    
    if new_game == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break