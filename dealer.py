'''

'''

from card import Card
from deck import Deck
from player import Player

class Dealer():
     
    def __init__(self):
        self.cardSum = 0
        self.dealerCards = []

    def __str__(self):
        if len(self.dealerCards) == 0:
            return f"Dealer has no cards"
        else:
            print(f"Dealer has -> ")
            print(f"\t{self.dealerCards[-1]}  {self.dealerCards[-1].value}")
            return ""

    def takeCard(self, newCard):
        self.cardSum += newCard.value
        self.dealerCards.append(newCard)