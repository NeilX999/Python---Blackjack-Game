import GameEvents
import GameFunctionality


# Player and Dealer's cards inventory
player = []
dealer = []


"""
Initialize card values

Cards - 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
"""
cards = [2, 3, 4, 5, 6, 7, 8, 9]


# Default values for Jack, Queen, King and Ace
Jack = 10.1
Queen = 10.2
King = 10.3
Ace = 11.1
Ace_values = [1, 11]

cards.append(Jack)
cards.append(Queen)
cards.append(King)
cards.append(Ace)


def show_cards():
    print(player)


GameEvents.Card_Dealing(cards, player, dealer)
