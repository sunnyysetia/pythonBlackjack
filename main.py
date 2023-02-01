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
def createHiddenCard():
    hiddenCard = [
        "          ┌──────┐",
        "          │{:<5} │".format('?'),
        "          ├──────┤",
        "          │      │",
        "          │  {}  │".format('??'),
        "          │      │",
        "          ├──────┤",
        "          │ {:>5}│".format('?'),
        "          └──────┘",
        " {:^17}".format('?? OF ????')
    ]
    return hiddenCard

def createDeck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(card(rank,suit))
    
    return deck

def addToVisual(person,card):
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
    card = random.choice(deck)

    # Apend card to person's hand
    person.hand.append(card)

    # Update person's value attribute
    rank = card.rank
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
    addToVisual(person,card)
    
    # Remove card from deck
    deck.remove(card)
  
def printHands(dealer,player, hiddenCard):
    print("============")
    for person in [dealer, player]:
        print("\033[4m{}'s hand\033[0m".format(person.name))
        print("Value: \033[1m{}\033[0m".format(person.val)) 

        if len(dealer.hand) == 1 and person == dealer:
            for i in range(0,9):
                print(person.visual[i] + hiddenCard[i])
        else:
            for line in person.visual:
                print(line)

# Main Game
def blackjack():
    # Create new deck
    deck = createDeck()
    hiddenCard = createHiddenCard()

    # Initialise dealer and player as person class
    dealer = person('Dealer')
    player = person('Player')

    # Initial hand out and print of hands
    dealCard(dealer,deck)
    dealCard(player,deck)
    dealCard(player,deck)

    printHands(dealer,player, hiddenCard)

    # Initialise whether loser has been found
    player_lost = False
    dealer_lost = False

    #initialise whether player has blackjack.
    blackjack = False

    while True: 
        if player.val == 21:
            if len(player.hand) == 2:
                blackjack = True
                print("You got Blackjack!!")
            break
        elif player.val > 21:
            print("\033[1mYou Bust!!\033[0m")
            player_lost = True
            break
        else:
            choice = input("Would you like to hit or stand? (h/s): ")
            while choice != 'h' and choice != 's':
                print("Please input either 'h' or 's'")
                choice = input("Would you like to hit or stand? (h/s): ")
            if choice == 'h':
                dealCard(player,deck)
                printHands(dealer,player, hiddenCard) 
            else:
                break

    while dealer.val <= 16 and blackjack==False:
        print("\033[3mDealer is drawing card..\033[0m")
        time.sleep(2)
        dealCard(dealer,deck)
        printHands(dealer,player, hiddenCard)
        
    
    if dealer.val > 21 and player_lost == False:
        print("\033[1mDealer Busts!!\033[0m")
        dealer_lost = True

    # Print Winner
    if player_lost:
        print("\033[1mDealer wins!!\033[0m")
    elif dealer_lost:
        print("\033[1mPlayer wins!!\033[0m")
    elif dealer.val > player.val:
        print("\033[1mDealer wins!!\033[0m")
    elif dealer.val < player.val:
        print("\033[1mPlayer wins!!\033[0m")
    else:
        print("\033[1mIt's a tie!!\033[0m")


blackjack()