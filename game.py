'''

'''

from card import Card
from deck import Deck
from player import Player
from dealer import Dealer
import random

# print(Deck())
# newPlayer = Player(0)
# newPlayer.takeCard(Card("Heart","Two"))
# newPlayer.takeCard(Card("Heart","Three"))
# newPlayer.takeCard(Card("Heart","Ace"))
# print(newPlayer)

# print(Deck())
# newDealer = Dealer()
# newDealer.takeCard(Card("Heart","Ace"))
# newDealer.takeCard(Card("Heart","Two"))
# print(newDealer)

player1 = Player(0)
dealer1 = Dealer()
newDeck = Deck()

def start(money):
    global player1
    global dealer1
    global newDeck

    play = True

    options = ["Hit", "hit", "HIT", "Stay", "stay", "STAY"]
    
    player1 = Player(money)
    dealer1 = Dealer()
    newDeck = Deck()
    newDeck.shuffle()
    
    bet = int(input("How much are you betting: "))

    while bet > player1.bank:
        bet = int(input("Insuficient balance try again: "))

    deal(2,True,True)

    print(dealer1)
    print(player1)

    while play:
        decide = input("Enter Hit or Stay???")
        while decide not in options:
            decide = input("Invalid entry, try again: ")

        if decide == "hit" or decide == "Hit" or decide == "HIT":
            deal(1,True,False)
            print(dealer1)
            print(player1)
            if player1.cardSum > 21:
                print("player losses")
                player1.bank -= bet
                print(f"You have ${player1.bank}")
                play = False
        if decide == "stay" or decide == "Stay" or decide == "STAY":
            # Deal dealer
            while True:
                deal(1,False,True)
                print(dealer1)
                print(player1)
                if dealer1.cardSum > 21:
                    print("player wins")
                    play = False
                    player1.bank += bet
                    print(f"You have ${player1.bank}")
                    break
                if dealer1.cardSum > player1.cardSum:
                    print("player loses")
                    play = False
                    player1.bank -= bet
                    print(f"You have ${player1.bank}")
                    break
    playAgain()

def deal(num,player,dealer):
    global player1
    global dealer1
    global newDeck
    
    aceValues = [1,11]
    
    if player:
        ace = 0
        for x in range(num):
            tempCard = newDeck.dealOne()
            if tempCard.rank == "Ace":
                ace = int(input("What value should your Ace be, 1 or 11"))
                while ace not in aceValues:
                    ace = int(input("Wrong value try again: "))
                    
            player1.takeCard(tempCard)
            player1.cardSum += ace
    if dealer:
        ace = 0
        for x in range(num):
            tempCard = newDeck.dealOne()
            if tempCard.rank == "Ace":
                ace = aceValues[random.randint(0,1)]

            dealer1.takeCard(tempCard)
            dealer1.cardSum += ace

def playAgain():
    yes = input("DO you want to play again Yes/No: ")

    while True:
        if yes in ["Yes", "yes", "YES"]:
            break
        elif yes in ["No", "no", "NO"]:
            print("Goodbye")
            return
        else:
            print("Invalid input try again")
    
    print()
    start(player1.bank)


        
start(100)