import random
import time

# Define ranks & suits
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['♥️','♦️','♠️','♣️']

# Classes
class card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

class person:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.val = 0

# Helper Functions

def printCard(rank, suit):
    print("┌──────┐")
    print("│{:<5} │".format(rank))
    print("├──────┤")
    print("│      │")
    print("│  {}   │".format(suit))
    print("│      │")
    print("├──────┤")
    print("│ {:>5}│".format(rank))
    print("└──────┘")

def createDeck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(card(rank,suit))
    
    return deck

def printHands(dealer,player):
    for person in [dealer, player]:
        print("{}'s hand".format(person.name))
        print("Value: {}".format(person.val))

        # Print visual of hand
        for card in person.hand:
            printCard(card.rank,card.suit)   

def dealCard(person, deck):
    no_of_hand_remaining = len(deck) -1
    randomIndex = random.randint(0, no_of_hand_remaining)

    # Apend card to person's hand
    person.hand.append(deck[randomIndex])

    # Update person's value attribute
    rank = deck[randomIndex].rank
    if rank == 'A':
        if person.val <= 10:
            person.val += 11
        else:
            person.val += 1
    elif rank == 'J' or rank == 'Q' or rank == 'K':
        person.val += 10
    else:
        person.val += int(rank)

    # Remove card from deck
    del deck[randomIndex]
  
def blackjack():
    # Create new deck
    deck = createDeck()

    # Initialise dealer and player as person class
    dealer = person('Dealer')
    player = person('Player')

    # Initial hand out and print of hands
    dealCard(dealer,deck)
    dealCard(dealer,deck)
    dealCard(player,deck)

    printHands(dealer,player)

    # Initialise whether loser has been found
    player_lost = False
    dealer_lost = False

    while True:
        choice = input("Would you like to hit or stand? (h/s): ")
        if choice == 'h':
            dealCard(player,deck)
            printHands(dealer,player)
            if player.val == 21:
                break
            elif player.val > 21:
                print("You Bust!!")
                player_lost = True
                break
        else:
            break

    while dealer.val <= 16:
        dealCard(dealer,deck)
        printHands(dealer,player)
        time.sleep(1)
    
    if dealer.val > 21:
        print("Dealer Busts!!")
        dealer_lost = True

    # Print Winner
    if player_lost or dealer_lost:
        pass
    elif dealer.val > player.val:
        print("Dealer wins!!")
    elif dealer.val < player.val:
        print("Player wins!!")
    else:
        print("It's a tie!!")

blackjack()