import random
import BlackjackSetup
import GameFunctionality


"""
Dealing out the cards to the player and the dealer

@param key_name - Check the value of TempValue
@param object_assign - Append key_name into the player and dealer's inventory
"""
def value_assigner(key_name, object_assign = []):
    if key_name == 10.1 or key_name == 10.2 or key_name == 10.3:
        key_name = int(key_name)
        object_assign.append(key_name)
    
    elif key_name == 11.1:
        object_assign.append(random.choice(BlackjackSetup.Ace_values))
       
    else:
        object_assign.append(key_name)


"""
@param object_Name1 - Needs object's name for calculations
@param object_Name2 - refer object_Name1
"""
def Card_Dealing(deck_of_cards, object_Name1, object_Name2):
    for i in range(2):
        temp_card = random.choice(deck_of_cards)
        value_assigner(temp_card, object_Name1)
        temp_card = random.choice(deck_of_cards)
        value_assigner(temp_card, object_Name2)


def CardCounter(object_assign = []):
    temp_result = 0
    for card_num in range(0, len(object_assign)):
        temp_result = temp_result + object_assign[card_num]


# Compares the player's cards value with the dealer's cards
def Card_Comparison(object_assign1, object_assign2):
    temp_result = temp_result2 = 0
    for card_num in range(0, len(object_assign1)):
        temp_result = temp_result + object_assign1[card_num]

    for card_num2 in range(0, len(object_assign2)):
        temp_result2 = temp_result2 + object_assign2[card_num2]

    if temp_result < 21 and temp_result2 < 21:
        if temp_result > temp_result2:
            print("Dealer wins!")
        elif temp_result < temp_result2:
            print("Player wins!")

    elif temp_result == 21 and temp_result2 == 21:
        print("It's a draw :(")

    elif temp_result < 21 and temp_result2 == 21:
        print("Player wins!")

    elif temp_result == 21 and temp_result2 < 21:
        print("Dealer wins!")

    elif temp_result > 21 and temp_result2 > 21:
        print("Nobody wins :(")

    elif temp_result < 21 and temp_result2 > 21:
        print("Dealer wins!")
    
    elif temp_result > 21 and temp_result2 < 21:
        print("Player wins!")

    elif temp_result == temp_result2:
        print("It's a draw")


# The Dealer
def dealer_AI():
    temp = 0
    for i in range(1):
        dealer_cards = random.choice(BlackjackSetup.cards)
        value_assigner(dealer_cards, BlackjackSetup.dealer)
        for temp_card in range(0, len(BlackjackSetup.dealer)):
            temp = temp + BlackjackSetup.dealer[temp_card]
        if temp >= 17 and temp <= 21:
            Card_Comparison(BlackjackSetup.dealer, BlackjackSetup.player)
            break
        elif temp < 16:
            continue
        elif temp == 21:
            Card_Comparison(BlackjackSetup.dealer, BlackjackSetup.player)
            break
        elif temp > 21:
            Card_Comparison(BlackjackSetup.dealer, BlackjackSetup.player)
            break