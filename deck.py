'''

'''
from card import Card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':0}


class Deck():
    
    def __init__(self):
        self.cardDeck = []

        for rank in ranks:
            for suit in suits:
                self.cardDeck.append(Card(suit,rank))

    def __str__(self):
        counter = 0
        for cards in self.cardDeck:
            counter += 1
            print("{} {}".format(counter,cards))
        return ""

    def shuffle(self):
        random.shuffle(self.cardDeck)

    def dealOne(self):
        return self.cardDeck.pop()