import random
import BlackjackSetup


def hit(object_assign = []):
     for i in range(1):
          Amount = random.choice(BlackjackSetup.cards)
          if Amount == 11.1:
              Amount = random.choice(BlackjackSetup.Ace_values)
              object_assign.append(Amount)
              print("The next card is a {0}".format(Amount))

          elif Amount == 10.1 or Amount == 10.2 or Amount == 10.3:
                Amount = int(Amount)
                object_assign.append(Amount)
                print("The next card is a {0}".format(Amount))

          else:
                object_assign.append(Amount)
                print("The next card is a {0}".format(Amount))
     Amount = None

    