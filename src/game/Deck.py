from random import shuffle
from game.Card import Card

class Deck:
    symbols = ['heart', 'spade', 'clover', 'diamond']
    cards = []

    def __init__(self):
        for i in range(13):
            for symbol in self.symbols:
                self.cards.append(Card(i, symbol))
        self.shuffle()

    def shuffle(self):
        self.cards = shuffle(self.cards)

    #def getCards(self):