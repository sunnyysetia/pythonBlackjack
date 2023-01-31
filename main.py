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

def dealCard(person, deck):
    no_of_cards_remaining = len(deck) -1
    randomIndex = random.randint(0, no_of_cards_remaining)

    # Apend card to person's cards
    person.cards.append(deck[randomIndex])

    # Append person's value attribute
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

    
    
class person:
    def __init__(self):
        self.cards = []
        self.val = 0

def blackjack():
    # Create new deck
    deck = createDeck()

    # Initialise dealer and player cards

    dealer = person()
    player = person()

    dealCard(dealer,deck)
    dealCard(dealer,deck)
    dealCard(player,deck)

    print("Dealer's Cards")
    print(dealer.val)
    printCards(dealer.cards)

    print("Player's Cards")
    print(player.val)
    printCards(player.cards)




blackjack()