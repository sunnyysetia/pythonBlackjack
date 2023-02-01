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

        if self.suit == '♥️':
            self.string = '(' + self.rank + ' OF ' + 'HEARTS' + ')'
        elif self.suit == '♦️':
            self.string = '(' + self.rank + ' OF ' + 'DIAMONDS' + ')'
        elif self.suit == '♠️':
            self.string = '(' + self.rank + ' OF ' + 'SPADES' + ')'
        else:
            self.string = '(' + self.rank + ' OF ' + 'CLUBS' + ')'

class person:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.val = 0
        self.visual=['','','','','','','','','', '     ']

# Helper Functions

def createDeck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(card(rank,suit))
    
    return deck

def addToVisual(person,card):
    
    
    # person.visual[0] += "┌──────┐          "
    # person.visual[1] += "│{:<5} │          ".format(card.rank)
    # person.visual[2] += "├──────┤          "
    # person.visual[3] += "│      │          "
    # person.visual[4] += "│  {}   │          ".format(card.suit)
    # person.visual[5] += "│      │          "
    # person.visual[6] += "├──────┤          "
    # person.visual[7] += "│ {:>5}│          ".format(card.rank)
    # person.visual[8] += "└──────┘          "
    # person.visual[9] += "({} {})        ".format(card.rank, suit)
    person.visual[0] += "          ┌──────┐"
    person.visual[1] += "          │{:<5} │".format(card.rank)
    person.visual[2] += "          ├──────┤"
    person.visual[3] += "          │      │"
    person.visual[4] += "          │  {}   │".format(card.suit)
    person.visual[5] += "          │      │"
    person.visual[6] += "          ├──────┤"
    person.visual[7] += "          │ {:>5}│".format(card.rank)
    person.visual[8] += "          └──────┘"
    person.visual[9] += " {:^17}".format(card.string)

def dealCard(person, deck):
    no_of_cards_remaining = len(deck) -1
    randomIndex = random.randint(0, no_of_cards_remaining)

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

    # Add card to person's visual
    addToVisual(person,deck[randomIndex])
    
    # Remove card from deck
    del deck[randomIndex]
  
def printHands(dealer,player):
    print("============")
    for person in [dealer, player]:
        print("\033[4m{}'s hand\033[0m".format(person.name))
        print("Value: {}".format(person.val)) 

        for line in person.visual:
            print(line)

# Main Game
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
    dealCard(player,deck)

    printHands(dealer,player)

    # Initialise whether loser has been found
    player_lost = False
    dealer_lost = False

    while True: 
        if player.val == 21:
            if len(player.hand) == 1:
                print("You got Blackjack!!")
            break
        elif player.val > 21:
            print("You Bust!!")
            player_lost = True
            break
        else:
            choice = input("Would you like to hit or stand? (h/s): ")
            while choice != 'h' and choice != 's':
                print("Please input either 'h' or 's'")
                choice = input("Would you like to hit or stand? (h/s): ")
            if choice == 'h':
                dealCard(player,deck)
                printHands(dealer,player) 
            else:
                break

    while dealer.val <= 16:
        time.sleep(2)
        dealCard(dealer,deck)
        printHands(dealer,player)
        
    
    if dealer.val > 21 and player_lost == False:
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