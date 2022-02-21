from random import shuffle
from game.Card import Card

class Deck:
    symbols = ['heart', 'spade', 'clover', 'diamond']
    cards = []

    def __init__(self):
        for i in range(13):
            for symbol in self.symbols:
                self.cards.append(Card(i, symbol))
        shuffle(self.cards)


    def getCards(self, amount: int):
        return [self.cards.pop(i) for i in range(amount)]

    def emptyDeck(self):
        cards = [*self.cards]
        self.cards = []
        return cards