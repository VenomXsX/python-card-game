# https://tkinter-docs.readthedocs.io/en/latest/index.html
from game.Window import Window
from game.Deck import Deck
from game.Slot import Slot

def main():
    deck = Deck()
    slots = []
    for i in range(7):
        slots.append(Slot(deck.getCards(i + 1)))
    
    drawer = Slot(deck.emptyDeck())
    window = Window()

if __name__ == "__main__":
    main()