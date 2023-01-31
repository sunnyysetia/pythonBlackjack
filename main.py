import random

def printCard(rank, suit):
    print("┌───────┐")
    print("│{}      │".format(rank))
    print("├───────┤")
    print("│       │")
    print("│   {}   │".format(suit))
    print("│       │")
    print("├───────┤")
    print("│      {}│".format(rank))
    print("└───────┘")

suits = ['♥️','♦️','♠️','♣️']
ranks = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']

printCard(random.choice(ranks),random.choice(suits))