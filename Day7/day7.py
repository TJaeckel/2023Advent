# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 07:14:32 2023

@author: TJaeckel
"""
from enum import Enum
from sortedcontainers import SortedList
from collections import Counter


facevalues = {"T":"10", "J": "0", "Q": "12", "K":"13", "A":"14"}
handtypes = {"HIGH_CARD": 1, "ONE_PAIR" : 2, "TWO_PAIR" : 3, "THREE_KIND" : 4,
             "FULL_HOUSE" : 5, "FOUR_KIND" :6, "FIVE_KIND" : 7}


class Hand:
    cards = ""
    bet = 0
    handvalue = 0
    indcardvalue = []
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = int(bet)
        self.calcHand()

    
    def calcHand(self):
        mostcommon = Counter(self.cards).most_common(2)
        if self.cards == "JJJJJ":
            print("here")
        cardcount = mostcommon[0][1]
        if "J" in self.cards:
            if ("J" == mostcommon[0][0]) & (mostcommon[0][1] != 5):
                cardcount = mostcommon[1][1] + self.cards.count("J")
            elif mostcommon[0][1] != 5:
                cardcount += self.cards.count("J")
        if cardcount == 5:
            self.handvalue = handtypes["FIVE_KIND"]
        elif cardcount == 4:
            self.handvalue = handtypes["FOUR_KIND"]
        elif cardcount == 3:
            fullhouse = Counter(self.cards).most_common(2)
            if (cardcount == 3) & (fullhouse[1][1] == 2):
                self.handvalue = handtypes["FULL_HOUSE"]
            else:
                self.handvalue = handtypes["THREE_KIND"]
        elif cardcount == 2:
            twopair = Counter(self.cards).most_common(2)
            if (cardcount == 2) & (twopair[1][1] == 2):
                self.handvalue = handtypes["TWO_PAIR"]
            else:
                self.handvalue = handtypes["ONE_PAIR"]
        elif cardcount == 1:
            self.handvalue = handtypes["HIGH_CARD"]
        val = []
        for card in self.cards:
            if card in facevalues.keys():
                card = facevalues[card]
            val.append(int(card))
        self.indcardvalue = val
    
    def __lt__(self, other):
        if self.handvalue != other.handvalue:
            return self.handvalue < other.handvalue
        else:
            for x in range(0, len(self.indcardvalue)):
                if self.indcardvalue[x] != other.indcardvalue[x]:
                    return self.indcardvalue[x] < other.indcardvalue[x]
                

carddata = open(r"C:\Users\tonyj\OneDrive\Documents\Python Scripts\Advent 2023\Day7\input.txt").readlines()

cardhands = []

for cardhand in carddata:
    handbet = cardhand.split(" ")
    cardhands.append(Hand(handbet[0], handbet[1]))
handlist= []   
cardhands.sort()
multiplyer = 1
totalbet = 0
for card in cardhands:
    totalbet += card.bet * multiplyer
    multiplyer += 1
    handlist.append(card.cards)
print(totalbet)