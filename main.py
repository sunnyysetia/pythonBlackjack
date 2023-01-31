import random

ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
suits = ['♥️','♦️','♠️','♣️']


def printCard(rank, suit):
    print("┌───────┐")
    print("│{:<5}  │".format(rank))
    print("├───────┤")
    print("│       │")
    print("│   {}   │".format(suit))
    print("│       │")
    print("├───────┤")
    print("│  {:>5}│".format(rank))
    print("└───────┘")


class card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit


def createDeck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(card(rank,suit))
    
    return deck

def printCards(deck):
    for card in deck:
        printCard(card.rank,card.suit)

def dealCard(who, deck):
    no_of_cards_remaining = len(deck) -1
    randomIndex = random.randint(0, no_of_cards_remaining)
    who.append(deck[randomIndex])
    del deck[randomIndex]




def blackjack():
    # Create new deck
    deck = createDeck()

    # Initialise dealer and player cards
    dealerCards=[]
    playerCards=[]

    dealCard(dealerCards,deck)
    dealCard(dealerCards,deck)
    dealCard(playerCards,deck)

    print("Dealer's Cards")
    printCards(dealerCards)

    print("Player's Cards")
    printCards(playerCards)



# deck = createDeck()

# print(len(deck))
blackjack()