from game.Card import Card

class Slot:
    cards = []
    isGameSlot: bool

    def __init__(self, cards = [], isGameSlot: bool = True):
        self.cards = cards
        self.isGameSlot = isGameSlot

    def addCard(self, card: Card):
        # TODO: Add card validation
        self.cards.append(card)