import random
class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def __str__(self):
        return "{} of {}".format(self.suit,self.value)

class Deck:
    suits=["Hearts", "Diamonds", "Clubs", "Spades"]
    values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.cards=[]
        for suit in Deck.suits:
            for value in Deck.values:
                card=Card(suit,value)
                self.cards.append(card)
        random.shuffle(self.cards)
    def shuffle(self):
        self.cards=[]
        for suit in Deck.suits:
            for value in Deck.values:
                card=Card(suit,value)
                self.cards.append(card)
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return "No cards left in the deck!"
        return self.cards.pop()

    def __str__(self):
        return f"no of cards remaining in deck = {len(self.cards)}"

obj=Deck()
print(obj)
card1=obj.deal()
print(card1)
print(obj)
card2=obj.deal()
print(card2)
obj2=Deck()
print(obj2)