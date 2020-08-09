'''

'''

from card import Card
from deck import Deck

class Player():

    def __init__(self, pocket):
        self.bank = pocket
        self.cardSum = 0
        self.playerCards = []

    def __str__(self):
        if len(self.playerCards) == 0:
            return f"Player has ${self.bank} with no cards {self.cardSum}"
        else:
            print(f"Player has -> ${self.bank}")
            for cards in self.playerCards:
                print(f"\t{cards}")
            print(f"Player card sum -> {self.cardSum}")
            return ""

    def takeCard(self, newCard):
        self.cardSum += newCard.value
        self.playerCards.append(newCard)